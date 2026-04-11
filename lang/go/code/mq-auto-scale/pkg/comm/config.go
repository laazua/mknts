// comm/config.go
package comm

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"
)

// Config 配置管理结构体
type Config struct {
	data map[string]any
}

var defaultConfig *Config

func init() {
	defaultConfig = &Config{
		data: make(map[string]any),
	}
}

// NewConfig 创建新的配置实例
func NewConfig() *Config {
	return &Config{
		data: make(map[string]any),
	}
}

// LoadEnv 加载.env文件到默认配置
func LoadEnv(filename string) error {
	return defaultConfig.LoadEnv(filename)
}

// LoadDefaultEnv 加载默认的.env文件
func LoadDefaultEnv() error {
	return defaultConfig.LoadEnv(".env")
}

// Env 获取默认配置实例（全局配置）
func Env() *Config {
	return defaultConfig
}

// LoadEnv 加载.env文件到当前配置实例
func (c *Config) LoadEnv(filename string) error {
	file, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	return c.parseReader(file)
}

// parseReader 从reader解析配置，支持多行值
func (c *Config) parseReader(reader io.Reader) error {
	scanner := bufio.NewScanner(reader)

	var currentKey string
	var currentValue strings.Builder
	var inMultiline bool
	var multilineType string   // "list" or "object"
	var squareBracketCount int // 专门用于跟踪方括号
	var braceCount int         // 专门用于跟踪花括号
	lineNum := 0

	for scanner.Scan() {
		lineNum++
		line := scanner.Text()

		// 处理多行值
		if inMultiline {
			// 添加换行符（除了第一行）
			if currentValue.Len() > 0 {
				currentValue.WriteString("\n")
			}
			currentValue.WriteString(line)

			// 更新括号计数
			squareBracketCount += strings.Count(line, "[") - strings.Count(line, "]")
			braceCount += strings.Count(line, "{") - strings.Count(line, "}")

			// 检查是否结束
			if multilineType == "list" && squareBracketCount == 0 && braceCount == 0 {
				// 列表结束，且没有未闭合的花括号
				inMultiline = false
				fullValue := currentValue.String()
				parsedValue, err := c.parseValue(fullValue)
				if err != nil {
					return fmt.Errorf("line %d: failed to parse multiline value for key '%s': %v", lineNum, currentKey, err)
				}
				c.data[currentKey] = parsedValue
			} else if multilineType == "object" && braceCount == 0 {
				inMultiline = false
				fullValue := currentValue.String()
				parsedValue, err := c.parseValue(fullValue)
				if err != nil {
					return fmt.Errorf("line %d: failed to parse multiline value for key '%s': %v", lineNum, currentKey, err)
				}
				c.data[currentKey] = parsedValue
			}
			continue
		}

		// 处理普通行
		line = strings.TrimSpace(line)

		// 跳过空行和注释
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}

		// 检查是否是多行值的开始
		eqIndex := strings.Index(line, "=")
		if eqIndex == -1 {
			return fmt.Errorf("line %d: invalid format: missing '='", lineNum)
		}

		key := strings.TrimSpace(line[:eqIndex])
		value := strings.TrimSpace(line[eqIndex+1:])

		if key == "" {
			return fmt.Errorf("line %d: empty key", lineNum)
		}

		// 检查是否是多行值的开始
		// 情况1: 以 [ 开头但没有匹配的 ]
		// 情况2: 以 { 开头但没有匹配的 }
		// 情况3: 以 [ 开头且后面跟着换行（value为空或只是[）
		if strings.HasPrefix(value, "[") && !strings.HasSuffix(value, "]") {
			inMultiline = true
			currentKey = key
			currentValue.Reset()
			currentValue.WriteString(value)
			multilineType = "list"
			squareBracketCount = strings.Count(value, "[") - strings.Count(value, "]")
			braceCount = strings.Count(value, "{") - strings.Count(value, "}")
			continue
		} else if strings.HasPrefix(value, "{") && !strings.HasSuffix(value, "}") {
			inMultiline = true
			currentKey = key
			currentValue.Reset()
			currentValue.WriteString(value)
			multilineType = "object"
			squareBracketCount = strings.Count(value, "[") - strings.Count(value, "]")
			braceCount = strings.Count(value, "{") - strings.Count(value, "}")
			continue
		} else if strings.HasPrefix(value, "[") && strings.HasSuffix(value, "]") {
			// 单行列表，直接解析
			parsedValue, err := c.parseValue(value)
			if err != nil {
				return fmt.Errorf("line %d: %v", lineNum, err)
			}
			c.data[key] = parsedValue
			continue
		}

		// 单行值，直接解析
		parsedValue, err := c.parseValue(value)
		if err != nil {
			return fmt.Errorf("line %d: %v", lineNum, err)
		}
		c.data[key] = parsedValue
	}

	// 检查未完成的多行值
	if inMultiline {
		return fmt.Errorf("unclosed multiline value for key '%s'", currentKey)
	}

	return scanner.Err()
}

// parseLine 解析单行配置（保留用于向后兼容）
func (c *Config) parseLine(line string) error {
	// 这个方法保留用于单行解析，但现在主要使用parseReader
	eqIndex := strings.Index(line, "=")
	if eqIndex == -1 {
		return fmt.Errorf("invalid format: missing '='")
	}

	key := strings.TrimSpace(line[:eqIndex])
	value := strings.TrimSpace(line[eqIndex+1:])

	if key == "" {
		return fmt.Errorf("empty key")
	}

	parsedValue, err := c.parseValue(value)
	if err != nil {
		return err
	}

	c.data[key] = parsedValue
	return nil
}

// parseValue 根据值的格式解析不同类型
func (c *Config) parseValue(value string) (interface{}, error) {
	value = strings.TrimSpace(value)

	// 移除引号（仅当整个字符串被引号包围时）
	if len(value) >= 2 {
		if (value[0] == '"' && value[len(value)-1] == '"') ||
			(value[0] == '\'' && value[len(value)-1] == '\'') {
			return value[1 : len(value)-1], nil
		}
	}

	// 解析列表
	if strings.HasPrefix(value, "[") && strings.HasSuffix(value, "]") {
		return c.parseList(value)
	}

	// 解析对象
	if strings.HasPrefix(value, "{") && strings.HasSuffix(value, "}") {
		return c.parseObject(value)
	}

	// 解析布尔值
	lowerValue := strings.ToLower(value)
	if lowerValue == "true" {
		return true, nil
	}
	if lowerValue == "false" {
		return false, nil
	}

	// 解析数字
	if num, err := c.parseNumber(value); err == nil {
		return num, nil
	}

	return value, nil
}

// parseList 解析列表
func (c *Config) parseList(listStr string) ([]interface{}, error) {
	// 去除外层的方括号
	content := strings.TrimSpace(listStr[1 : len(listStr)-1])
	if content == "" {
		return []interface{}{}, nil
	}

	var items []interface{}
	parts := c.splitByComma(content)

	for _, part := range parts {
		trimmed := strings.TrimSpace(part)
		if trimmed == "" {
			continue
		}
		item, err := c.parseValue(trimmed)
		if err != nil {
			return nil, err
		}
		items = append(items, item)
	}

	return items, nil
}

// parseObject 解析对象
func (c *Config) parseObject(objStr string) (map[string]interface{}, error) {
	// 去除外层的大括号
	content := strings.TrimSpace(objStr[1 : len(objStr)-1])
	if content == "" {
		return map[string]interface{}{}, nil
	}

	obj := make(map[string]interface{})
	pairs := c.splitByComma(content)

	for _, pair := range pairs {
		pair = strings.TrimSpace(pair)
		if pair == "" {
			continue
		}

		colonIdx := c.findColonOutsideQuotes(pair)
		if colonIdx == -1 {
			return nil, fmt.Errorf("invalid object format: missing ':' in '%s'", pair)
		}

		key := strings.TrimSpace(pair[:colonIdx])
		value := strings.TrimSpace(pair[colonIdx+1:])

		// 移除键的引号
		key = strings.Trim(key, "\"'")

		parsedValue, err := c.parseValue(value)
		if err != nil {
			return nil, err
		}

		obj[key] = parsedValue
	}

	return obj, nil
}

// splitByComma 智能分割字符串，考虑括号和引号（增强版）
func (c *Config) splitByComma(s string) []string {
	var result []string
	var current strings.Builder
	depth := 0
	inQuotes := false
	quoteChar := rune(0)

	for i, ch := range s {
		switch {
		case !inQuotes && (ch == '"' || ch == '\''):
			inQuotes = true
			quoteChar = ch
			current.WriteRune(ch)
		case inQuotes && ch == quoteChar:
			inQuotes = false
			quoteChar = 0
			current.WriteRune(ch)
		case !inQuotes && (ch == '[' || ch == '{'):
			depth++
			current.WriteRune(ch)
		case !inQuotes && (ch == ']' || ch == '}'):
			depth--
			current.WriteRune(ch)
		case !inQuotes && ch == ',' && depth == 0:
			result = append(result, current.String())
			current.Reset()
		default:
			current.WriteRune(ch)
		}

		// 处理最后一个字符
		if i == len(s)-1 && current.Len() > 0 {
			result = append(result, current.String())
		}
	}

	// 清理每个部分的空格
	for i := range result {
		result[i] = strings.TrimSpace(result[i])
	}

	return result
}

// findColonOutsideQuotes 查找不在引号内的冒号位置
func (c *Config) findColonOutsideQuotes(s string) int {
	inQuotes := false
	quoteChar := rune(0)
	depth := 0

	for i, ch := range s {
		switch {
		case !inQuotes && (ch == '"' || ch == '\''):
			inQuotes = true
			quoteChar = ch
		case inQuotes && ch == quoteChar:
			inQuotes = false
			quoteChar = 0
		case !inQuotes && (ch == '[' || ch == '{'):
			depth++
		case !inQuotes && (ch == ']' || ch == '}'):
			depth--
		case !inQuotes && ch == ':' && depth == 0:
			return i
		}
	}
	return -1
}

// parseNumber 解析数字
func (c *Config) parseNumber(s string) (interface{}, error) {
	// 尝试解析为整数
	if intVal, err := strconv.ParseInt(s, 10, 64); err == nil {
		// 检查是否在int32范围内
		if intVal >= -2147483648 && intVal <= 2147483647 {
			return int(intVal), nil
		}
		return intVal, nil
	}

	// 尝试解析为无符号整数
	if uintVal, err := strconv.ParseUint(s, 10, 64); err == nil {
		return uintVal, nil
	}

	// 尝试解析为浮点数
	if floatVal, err := strconv.ParseFloat(s, 64); err == nil {
		return floatVal, nil
	}

	return nil, fmt.Errorf("not a number")
}

// ========== 配置获取方法 ==========

// Get 获取配置值
func (c *Config) Get(key string, defaults ...interface{}) interface{} {
	if val, exists := c.data[key]; exists {
		return val
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return nil
}

// Str 获取字符串
func (c *Config) Str(key string, defaults ...string) string {
	val := c.Get(key)
	if str, ok := val.(string); ok {
		return str
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return ""
}

// Int 获取整数
func (c *Config) Int(key string, defaults ...int) int {
	val := c.Get(key)
	switch v := val.(type) {
	case int:
		return v
	case int64:
		return int(v)
	case float64:
		return int(v)
	case string:
		if i, err := strconv.Atoi(v); err == nil {
			return i
		}
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return 0
}

// Int64 获取64位整数
func (c *Config) Int64(key string, defaults ...int64) int64 {
	val := c.Get(key)
	switch v := val.(type) {
	case int64:
		return v
	case int:
		return int64(v)
	case float64:
		return int64(v)
	case string:
		if i, err := strconv.ParseInt(v, 10, 64); err == nil {
			return i
		}
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return 0
}

// Float 获取浮点数
func (c *Config) Float(key string, defaults ...float64) float64 {
	val := c.Get(key)
	switch v := val.(type) {
	case float64:
		return v
	case int:
		return float64(v)
	case int64:
		return float64(v)
	case string:
		if f, err := strconv.ParseFloat(v, 64); err == nil {
			return f
		}
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return 0.0
}

// Bool 获取布尔值
func (c *Config) Bool(key string, defaults ...bool) bool {
	val := c.Get(key)
	if b, ok := val.(bool); ok {
		return b
	}
	if len(defaults) > 0 {
		return defaults[0]
	}
	return false
}

// Duration 获取时间间隔（支持多种格式）
// 支持格式：
// - 秒数（数字）：30 表示 30秒
// - 带单位的字符串："30s", "5m", "1h", "100ms"
// - 完整格式："1h30m", "1h30m15s"
func (c *Config) Duration(key string, defaults ...time.Duration) time.Duration {
	val := c.Get(key)

	// 尝试直接获取Duration类型
	if d, ok := val.(time.Duration); ok {
		return d
	}

	// 尝试从数字转换（作为秒数）
	if num, ok := val.(int); ok {
		return time.Duration(num) * time.Second
	}
	if num, ok := val.(int64); ok {
		return time.Duration(num) * time.Second
	}
	if num, ok := val.(float64); ok {
		// 修复：使用浮点数转换为纳秒，避免精度丢失
		return time.Duration(num * float64(time.Second))
	}

	// 尝试从字符串解析
	if str, ok := val.(string); ok {
		// 先尝试解析为数字（秒数）
		if seconds, err := strconv.ParseFloat(str, 64); err == nil {
			return time.Duration(seconds * float64(time.Second))
		}

		// 尝试使用time.ParseDuration解析
		if d, err := time.ParseDuration(str); err == nil {
			return d
		}
	}

	// 返回默认值
	if len(defaults) > 0 {
		return defaults[0]
	}
	return 0
}

// DurationDefault 获取时间间隔（必须提供默认值）
// 这是一个便捷方法，确保总是返回有效的Duration
func (c *Config) DurationDefault(key string, defaultValue time.Duration) time.Duration {
	return c.Duration(key, defaultValue)
}

// List 获取列表
func (c *Config) List(key string) []interface{} {
	val := c.Get(key)
	if list, ok := val.([]interface{}); ok {
		return list
	}
	return []interface{}{}
}

// StrList 获取字符串列表
func (c *Config) StrList(key string) []string {
	val := c.Get(key)
	if list, ok := val.([]interface{}); ok {
		result := make([]string, 0, len(list))
		for _, item := range list {
			if str, ok := item.(string); ok {
				result = append(result, str)
			}
		}
		return result
	}
	return []string{}
}

// IntList 获取整数列表
func (c *Config) IntList(key string) []int {
	val := c.Get(key)
	if list, ok := val.([]interface{}); ok {
		result := make([]int, 0, len(list))
		for _, item := range list {
			switch v := item.(type) {
			case int:
				result = append(result, v)
			case int64:
				result = append(result, int(v))
			case float64:
				result = append(result, int(v))
			}
		}
		return result
	}
	return []int{}
}

// DurationList 获取时间间隔列表
func (c *Config) DurationList(key string) []time.Duration {
	val := c.Get(key)
	if list, ok := val.([]interface{}); ok {
		result := make([]time.Duration, 0, len(list))
		for _, item := range list {
			// 尝试从数字转换
			switch v := item.(type) {
			case int:
				result = append(result, time.Duration(v)*time.Second)
			case int64:
				result = append(result, time.Duration(v)*time.Second)
			case float64:
				// 修复：使用浮点数转换为纳秒，避免精度丢失
				result = append(result, time.Duration(v*float64(time.Second)))
			case string:
				// 尝试解析字符串
				if d, err := time.ParseDuration(v); err == nil {
					result = append(result, d)
				} else if seconds, err := strconv.ParseFloat(v, 64); err == nil {
					result = append(result, time.Duration(seconds*float64(time.Second)))
				}
			case time.Duration:
				result = append(result, v)
			}
		}
		return result
	}
	return []time.Duration{}
}

// Obj 获取对象
func (c *Config) Obj(key string) map[string]interface{} {
	val := c.Get(key)
	if obj, ok := val.(map[string]interface{}); ok {
		return obj
	}
	return map[string]interface{}{}
}

// Has 检查键是否存在
func (c *Config) Has(key string) bool {
	_, exists := c.data[key]
	return exists
}

// Set 设置配置值
func (c *Config) Set(key string, value interface{}) {
	c.data[key] = value
}

// All 获取所有配置
func (c *Config) All() map[string]interface{} {
	return c.data
}

// Keys 获取所有键名
func (c *Config) Keys() []string {
	keys := make([]string, 0, len(c.data))
	for k := range c.data {
		keys = append(keys, k)
	}
	return keys
}
