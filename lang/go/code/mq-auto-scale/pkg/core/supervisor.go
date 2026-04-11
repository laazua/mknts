// supervisor管理
package core

import (
	"bytes"
	"encoding/xml"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"sync"
	"time"
)

// SupervisorConfig Supervisor RPC 配置
type SupervisorConfig struct {
	URL       string // XML-RPC 地址，如 http://localhost:9001/RPC2
	Username  string
	Password  string
	Timeout   time.Duration
	ConfigDir string // Supervisor 配置文件目录
}

// ProgramConfig 程序配置信息
type ProgramConfig struct {
	ConfigPath   string // 配置文件路径
	ProgramName  string // 程序名称
	CurrentCount int    // 当前 numprocs 值
	MinCount     int    // 最小进程数
	MaxCount     int    // 最大进程数
	QueueName    string // 对应的队列名称（从配置中读取或自动映射）
}

// XML-RPC 结构体定义
type methodCall struct {
	XMLName    xml.Name     `xml:"methodCall"`
	MethodName string       `xml:"methodName"`
	Params     methodParams `xml:"params"`
}

type methodParams struct {
	Param []methodParam `xml:"param"`
}

type methodParam struct {
	Value rpcValue `xml:"value"`
}

type rpcValue struct {
	Int     *int       `xml:"int"`
	I4      *int       `xml:"i4"`
	String  *string    `xml:"string"`
	Boolean *bool      `xml:"boolean"`
	Struct  *rpcStruct `xml:"struct"`
	Array   *rpcArray  `xml:"array"`
}

type rpcStruct struct {
	Member []rpcMember `xml:"member"`
}

type rpcMember struct {
	Name  string   `xml:"name"`
	Value rpcValue `xml:"value"`
}

type rpcArray struct {
	Data struct {
		Value []rpcValue `xml:"value"`
	} `xml:"data"`
}

type methodResponse struct {
	XMLName xml.Name      `xml:"methodResponse"`
	Params  *methodParams `xml:"params"`
	Fault   *rpcFault     `xml:"fault"`
}

type rpcFault struct {
	Value rpcValue `xml:"value"`
}

// ProcessInfo 进程信息
type ProcessInfo struct {
	Name        string
	Group       string
	State       int // 0: stopped, 10: starting, 20: running, 100: stopped
	Description string
	PID         int
	ExitStatus  int
}

// SupervisorManage Supervisor XML-RPC 客户端
type SupervisorManage struct {
	config     *SupervisorConfig
	client     *http.Client
	mu         sync.Mutex
	programs   map[string]*ProgramConfig // 程序名称 -> 配置
	programsMu sync.RWMutex
}

// NewSupervisorManage 创建 Supervisor 客户端
func NewSupervisorManage(config *SupervisorConfig) *SupervisorManage {
	if config.Timeout == 0 {
		config.Timeout = 10 * time.Second
	}

	// 设置默认配置文件目录
	if config.ConfigDir == "" {
		config.ConfigDir = "/etc/supervisor/conf.d"
	}

	manager := &SupervisorManage{
		config:   config,
		client:   &http.Client{Timeout: config.Timeout},
		programs: make(map[string]*ProgramConfig),
	}

	// 加载所有程序配置
	if err := manager.loadAllPrograms(); err != nil {
		// fmt.Printf("Warning: failed to load programs: %v\n", err)
		slog.Warn("failed to load programs", "error", err)
	}

	return manager
}

// loadAllPrograms 加载所有程序配置
func (c *SupervisorManage) loadAllPrograms() error {
	files, err := filepath.Glob(filepath.Join(c.config.ConfigDir, "*.ini"))
	if err != nil {
		return fmt.Errorf("failed to glob config files: %w", err)
	}

	for _, file := range files {
		programConfig, err := c.parseProgramConfig(file)
		if err != nil {
			// fmt.Printf("Warning: failed to parse %s: %v\n", file, err)
			slog.Warn("failed to parse program config", "file", file, "error", err)
			continue
		}

		c.programsMu.Lock()
		c.programs[programConfig.ProgramName] = programConfig
		c.programsMu.Unlock()

		// fmt.Printf("Loaded program: %s (config: %s, current: %d, min: %d, max: %d)\n",
		// 	programConfig.ProgramName, file, programConfig.CurrentCount,
		// 	programConfig.MinCount, programConfig.MaxCount)
		slog.Info("Loaded program", "name", programConfig.ProgramName, "config", file,
			"current", programConfig.CurrentCount, "min", programConfig.MinCount, "max", programConfig.MaxCount)
	}

	return nil
}

// parseProgramConfig 解析程序配置文件
func (c *SupervisorManage) parseProgramConfig(configPath string) (*ProgramConfig, error) {
	content, err := os.ReadFile(configPath)
	if err != nil {
		return nil, fmt.Errorf("failed to read config file: %w", err)
	}

	config := &ProgramConfig{
		ConfigPath:   configPath,
		CurrentCount: 1,
		MinCount:     1,
		MaxCount:     20,
	}

	// 提取 program 名称
	programRe := regexp.MustCompile(`\[program:([^\]]+)\]`)
	matches := programRe.FindStringSubmatch(string(content))
	if len(matches) >= 2 {
		config.ProgramName = matches[1]
	} else {
		return nil, fmt.Errorf("program name not found in config")
	}

	// 提取 numprocs
	numprocsRe := regexp.MustCompile(`numprocs\s*=\s*(\d+)`)
	if matches := numprocsRe.FindStringSubmatch(string(content)); len(matches) >= 2 {
		fmt.Sscanf(matches[1], "%d", &config.CurrentCount)
	}

	// 提取队列名称（从 command 或 directory 中推断）
	commandRe := regexp.MustCompile(`command\s*=\s*(.+)`)
	if matches := commandRe.FindStringSubmatch(string(content)); len(matches) >= 2 {
		config.QueueName = c.extractQueueName(matches[1])
	}

	// 提取自定义的 minprocs 和 maxprocs（如果有）
	minRe := regexp.MustCompile(`minprocs\s*=\s*(\d+)`)
	if matches := minRe.FindStringSubmatch(string(content)); len(matches) >= 2 {
		fmt.Sscanf(matches[1], "%d", &config.MinCount)
	}

	maxRe := regexp.MustCompile(`maxprocs\s*=\s*(\d+)`)
	if matches := maxRe.FindStringSubmatch(string(content)); len(matches) >= 2 {
		fmt.Sscanf(matches[1], "%d", &config.MaxCount)
	}

	return config, nil
}

// extractQueueName 从命令中提取队列名称
func (c *SupervisorManage) extractQueueName(command string) string {
	// 根据实际情况提取队列名称
	// 示例：./yii messages/pull 可能会提取 "messages"
	parts := strings.Fields(command)
	for i, part := range parts {
		if strings.Contains(part, "pull") && i > 0 {
			return parts[i-1]
		}
	}
	return "default"
}

// GetAllPrograms 获取所有程序配置
func (c *SupervisorManage) GetAllPrograms() map[string]*ProgramConfig {
	c.programsMu.RLock()
	defer c.programsMu.RUnlock()

	result := make(map[string]*ProgramConfig)
	for k, v := range c.programs {
		result[k] = v
	}
	return result
}

// GetProgramConfig 获取指定程序配置
func (c *SupervisorManage) GetProgramConfig(programName string) (*ProgramConfig, error) {
	c.programsMu.RLock()
	defer c.programsMu.RUnlock()

	if config, ok := c.programs[programName]; ok {
		return config, nil
	}
	return nil, fmt.Errorf("program %s not found", programName)
}

// UpdateConsumerCount 更新指定程序的消费者数量
func (c *SupervisorManage) UpdateConsumerCount(programName string, targetCount int) error {
	// 1. 获取程序配置
	programConfig, err := c.GetProgramConfig(programName)
	if err != nil {
		return fmt.Errorf("failed to get program config: %w", err)
	}

	// 2. 验证目标数量
	if targetCount < programConfig.MinCount {
		targetCount = programConfig.MinCount
		fmt.Printf("Target count adjusted to min: %d\n", targetCount)
	}
	if targetCount > programConfig.MaxCount {
		targetCount = programConfig.MaxCount
		fmt.Printf("Target count adjusted to max: %d\n", targetCount)
	}

	if programConfig.CurrentCount == targetCount {
		return nil
	}

	fmt.Printf("Updating %s consumer count from %d to %d\n",
		programName, programConfig.CurrentCount, targetCount)

	// 3. 更新配置文件
	if err := c.updateConfigFile(programConfig.ConfigPath, targetCount); err != nil {
		return fmt.Errorf("failed to update config file: %w", err)
	}

	// 4. 重新加载配置
	if err := c.reloadConfig(); err != nil {
		return fmt.Errorf("failed to reload config: %w", err)
	}

	// 5. 重启程序组
	if err := c.restartProgramGroup(programName); err != nil {
		return fmt.Errorf("failed to restart program group: %w", err)
	}

	// 6. 更新内存中的配置
	programConfig.CurrentCount = targetCount

	return nil
}

// updateConfigFile 更新配置文件中的 numprocs
func (c *SupervisorManage) updateConfigFile(configPath string, targetCount int) error {
	content, err := os.ReadFile(configPath)
	if err != nil {
		return fmt.Errorf("failed to read config file: %w", err)
	}

	// 替换 numprocs 值
	re := regexp.MustCompile(`(numprocs\s*=\s*)(\d+)`)
	newContent := re.ReplaceAllString(string(content), fmt.Sprintf("${1}%d", targetCount))

	// 写回文件
	if err := os.WriteFile(configPath, []byte(newContent), 0644); err != nil {
		return fmt.Errorf("failed to write config file: %w", err)
	}

	fmt.Printf("Config file updated: %s, numprocs set to %d\n", configPath, targetCount)
	return nil
}

// call 调用 XML-RPC 方法
func (c *SupervisorManage) call(method string, args ...any) (any, error) {
	c.mu.Lock()
	defer c.mu.Unlock()

	// 构建 XML-RPC 请求体
	request, err := c.buildXMLRPCRequest(method, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to build request: %w", err)
	}

	req, err := http.NewRequest("POST", c.config.URL, bytes.NewReader(request))
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}

	req.Header.Set("Content-Type", "text/xml")
	if c.config.Username != "" {
		req.SetBasicAuth(c.config.Username, c.config.Password)
	}

	resp, err := c.client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("failed to execute request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	return c.parseXMLRPCResponse(resp.Body)
}

// buildXMLRPCRequest 构建XML-RPC请求
func (c *SupervisorManage) buildXMLRPCRequest(method string, args ...any) ([]byte, error) {
	call := methodCall{
		MethodName: method,
		Params: methodParams{
			Param: make([]methodParam, len(args)),
		},
	}

	for i, arg := range args {
		val := c.buildRPCValue(arg)
		call.Params.Param[i] = methodParam{Value: val}
	}

	return xml.MarshalIndent(call, "", "  ")
}

// buildRPCValue 构建 RPC 值
func (c *SupervisorManage) buildRPCValue(v any) rpcValue {
	result := rpcValue{}

	switch typedVal := v.(type) {
	case int:
		result.Int = &typedVal
	case string:
		result.String = &typedVal
	case bool:
		result.Boolean = &typedVal
	default:
		str := fmt.Sprintf("%v", v)
		result.String = &str
	}

	return result
}

// parseXMLRPCResponse 解析XML-RPC响应
func (c *SupervisorManage) parseXMLRPCResponse(body io.Reader) (any, error) {
	var response methodResponse
	decoder := xml.NewDecoder(body)
	if err := decoder.Decode(&response); err != nil {
		return nil, fmt.Errorf("failed to decode response: %w", err)
	}

	// 检查是否有fault
	if response.Fault != nil {
		return nil, c.parseFault(response.Fault)
	}

	// 没有参数返回
	if response.Params == nil || len(response.Params.Param) == 0 {
		return nil, nil
	}

	// 返回第一个参数的值
	return c.extractRPCValue(response.Params.Param[0].Value), nil
}

// parseFault 解析错误信息
func (c *SupervisorManage) parseFault(fault *rpcFault) error {
	if fault == nil {
		return nil
	}

	val := c.extractRPCValue(fault.Value)
	if faultMap, ok := val.(map[string]interface{}); ok {
		if faultCode, ok := faultMap["faultCode"]; ok {
			if faultString, ok := faultMap["faultString"]; ok {
				return fmt.Errorf("XML-RPC fault %v: %v", faultCode, faultString)
			}
		}
	}

	return fmt.Errorf("unknown XML-RPC fault: %v", fault)
}

// extractRPCValue 从rpcValue中提取Go值
func (c *SupervisorManage) extractRPCValue(val rpcValue) any {
	if val.Int != nil {
		return *val.Int
	}
	if val.I4 != nil {
		return *val.I4
	}
	if val.String != nil {
		return *val.String
	}
	if val.Boolean != nil {
		return *val.Boolean
	}
	if val.Struct != nil {
		result := make(map[string]any)
		for _, m := range val.Struct.Member {
			result[m.Name] = c.extractRPCValue(m.Value)
		}
		return result
	}
	if val.Array != nil {
		result := make([]any, len(val.Array.Data.Value))
		for i, v := range val.Array.Data.Value {
			result[i] = c.extractRPCValue(v)
		}
		return result
	}
	return nil
}

// reloadConfig 重新加载 Supervisor 配置
func (c *SupervisorManage) reloadConfig() error {
	_, err := c.call("supervisor.reloadConfig")
	if err != nil {
		return fmt.Errorf("failed to reload config: %w", err)
	}

	// 等待配置生效
	time.Sleep(2 * time.Second)
	return nil
}

// restartProgramGroup 重启程序组
func (c *SupervisorManage) restartProgramGroup(groupName string) error {
	// 停止所有进程
	_, err := c.call("supervisor.stopProcessGroup", groupName)
	if err != nil {
		// 忽略停止错误，可能组不存在或已停止
		fmt.Printf("Warning: stopProcessGroup error for %s: %v\n", groupName, err)
	}

	// 等待进程停止
	time.Sleep(3 * time.Second)

	// 启动所有进程
	_, err = c.call("supervisor.startProcessGroup", groupName)
	if err != nil {
		return fmt.Errorf("failed to start process group: %w", err)
	}

	fmt.Printf("Program group %s restarted successfully\n", groupName)
	return nil
}

// GetRunningConsumerCount 获取指定程序当前运行的消费者进程数量
func (c *SupervisorManage) GetRunningConsumerCount(programName string) (int, error) {
	processes, err := c.GetAllProcessInfo()
	if err != nil {
		return 0, err
	}

	count := 0
	for _, p := range processes {
		if p.Group == programName && p.State == 20 { // 20 = RUNNING
			count++
		}
	}

	return count, nil
}

// GetAllRunningConsumerCounts 获取所有程序运行的消费者进程数量
func (c *SupervisorManage) GetAllRunningConsumerCounts() (map[string]int, error) {
	processes, err := c.GetAllProcessInfo()
	if err != nil {
		return nil, err
	}

	counts := make(map[string]int)
	for _, p := range processes {
		if p.State == 20 { // 20 = RUNNING
			counts[p.Group]++
		}
	}

	return counts, nil
}

// GetProcessInfo 获取进程信息
func (c *SupervisorManage) GetProcessInfo(name string) (*ProcessInfo, error) {
	result, err := c.call("supervisor.getProcessInfo", name)
	if err != nil {
		return nil, err
	}
	return c.parseProcessInfo(result), nil
}

// GetAllProcessInfo 获取所有进程信息
func (c *SupervisorManage) GetAllProcessInfo() ([]ProcessInfo, error) {
	result, err := c.call("supervisor.getAllProcessInfo")
	if err != nil {
		return nil, err
	}
	return c.parseProcessList(result), nil
}

// parseProcessInfo 解析进程信息
func (c *SupervisorManage) parseProcessInfo(data any) *ProcessInfo {
	processMap, ok := data.(map[string]any)
	if !ok {
		return &ProcessInfo{Name: "unknown", State: 0}
	}

	info := &ProcessInfo{}

	if name, ok := processMap["name"].(string); ok {
		info.Name = name
	}
	if group, ok := processMap["group"].(string); ok {
		info.Group = group
	}
	if state, ok := processMap["state"].(int); ok {
		info.State = state
	}
	if description, ok := processMap["description"].(string); ok {
		info.Description = description
	}
	if pid, ok := processMap["pid"].(int); ok {
		info.PID = pid
	}
	if exitStatus, ok := processMap["exitstatus"].(int); ok {
		info.ExitStatus = exitStatus
	}

	return info
}

// parseProcessList 解析进程列表
func (c *SupervisorManage) parseProcessList(data any) []ProcessInfo {
	processList, ok := data.([]any)
	if !ok {
		return []ProcessInfo{}
	}

	result := make([]ProcessInfo, 0, len(processList))
	for _, item := range processList {
		if processMap, ok := item.(map[string]any); ok {
			info := ProcessInfo{}

			if name, ok := processMap["name"].(string); ok {
				info.Name = name
			}
			if group, ok := processMap["group"].(string); ok {
				info.Group = group
			}
			if state, ok := processMap["state"].(int); ok {
				info.State = state
			}
			if description, ok := processMap["description"].(string); ok {
				info.Description = description
			}
			if pid, ok := processMap["pid"].(int); ok {
				info.PID = pid
			}
			if exitStatus, ok := processMap["exitstatus"].(int); ok {
				info.ExitStatus = exitStatus
			}

			result = append(result, info)
		}
	}

	return result
}

// GetSupervisorVersion 获取Supervisor版本
func (c *SupervisorManage) GetSupervisorVersion() (string, error) {
	result, err := c.call("supervisor.getSupervisorVersion")
	if err != nil {
		return "", err
	}

	if version, ok := result.(string); ok {
		return version, nil
	}
	return "", nil
}

// GetState 获取Supervisor状态
func (c *SupervisorManage) GetState() (int, string, error) {
	result, err := c.call("supervisor.getState")
	if err != nil {
		return 0, "", err
	}

	stateMap, ok := result.(map[string]any)
	if !ok {
		return 0, "", fmt.Errorf("unexpected response format")
	}

	stateCode := 0
	stateName := ""

	if code, ok := stateMap["statecode"].(int); ok {
		stateCode = code
	}
	if name, ok := stateMap["statename"].(string); ok {
		stateName = name
	}

	return stateCode, stateName, nil
}

// RefreshPrograms 刷新程序配置（当配置文件发生变化时调用）
func (c *SupervisorManage) RefreshPrograms() error {
	c.programsMu.Lock()
	defer c.programsMu.Unlock()

	// 清空现有配置
	c.programs = make(map[string]*ProgramConfig)

	// 重新加载
	return c.loadAllPrograms()
}
