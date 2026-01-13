package comm

import (
	"bufio"
	"bytes"
	"context"
	"fmt"
	"io"
	"os"
	"os/exec"
	"strings"
	"sync"
	"syscall"
	"time"
)

// CommandResult 命令执行结果
type CommandResult struct {
	Stdout   string
	Stderr   string
	ExitCode int
	Success  bool
	Err      error
	Duration time.Duration
}

// CommandOptions 命令执行选项
type CommandOptions struct {
	Timeout     time.Duration     // 超时时间
	WorkDir     string            // 工作目录
	Env         map[string]string // 环境变量
	Async       bool              // 是否异步执行
	Input       string            // 标准输入
	CaptureFunc func(line string) // 实时输出捕获函数
}

// CommandExecutor 命令执行器
type CommandExecutor struct {
	mutex sync.Mutex
}

// NewCommandExecutor 创建新的命令执行器
func NewCommandExecutor() *CommandExecutor {
	return &CommandExecutor{}
}

// RunCommand 执行命令（基础方法）
func (ce *CommandExecutor) RunCommand(cmdStr string, args []string, opts ...*CommandOptions) *CommandResult {

	ce.mutex.Lock()
	defer ce.mutex.Unlock()

	startTime := time.Now()
	result := &CommandResult{}

	// 创建命令
	ctx := context.Background()
	var cancel context.CancelFunc

	// 处理选项
	var options *CommandOptions
	if len(opts) > 0 && opts[0] != nil {
		options = opts[0]
	} else {
		options = &CommandOptions{}
	}

	// 设置超时
	if options.Timeout > 0 {
		ctx, cancel = context.WithTimeout(context.Background(), options.Timeout)
		defer cancel()
	}

	// 创建exec.Command
	var cmd *exec.Cmd
	if ctx == context.Background() {
		cmd = exec.Command(cmdStr, args...)
	} else {
		cmd = exec.CommandContext(ctx, cmdStr, args...)
	}

	// 设置工作目录
	if options.WorkDir != "" {
		cmd.Dir = options.WorkDir
	}

	// 设置环境变量
	if len(options.Env) > 0 {
		env := os.Environ()
		for k, v := range options.Env {
			env = append(env, fmt.Sprintf("%s=%s", k, v))
		}
		cmd.Env = env
	}

	// 设置标准输入
	if options.Input != "" {
		cmd.Stdin = strings.NewReader(options.Input)
	}

	// 捕获输出
	var stdoutBuf, stderrBuf bytes.Buffer
	var stdoutPipe, stderrPipe io.ReadCloser
	var err error

	if options.CaptureFunc != nil {
		// 实时捕获输出
		stdoutPipe, err = cmd.StdoutPipe()
		if err != nil {
			result.Err = fmt.Errorf("create stdout pipe failed: %v", err)
			return result
		}

		stderrPipe, err = cmd.StderrPipe()
		if err != nil {
			result.Err = fmt.Errorf("create stderr pipe failed: %v", err)
			return result
		}
	} else {
		// 标准输出捕获
		cmd.Stdout = &stdoutBuf
		cmd.Stderr = &stderrBuf
	}

	// 启动命令
	if err := cmd.Start(); err != nil {
		result.Err = err
		return result
	}

	// 处理实时输出
	if options.CaptureFunc != nil {
		var wg sync.WaitGroup
		wg.Add(2)

		go func() {
			defer wg.Done()
			ce.captureOutput(stdoutPipe, &stdoutBuf, options.CaptureFunc)
		}()

		go func() {
			defer wg.Done()
			ce.captureOutput(stderrPipe, &stderrBuf, options.CaptureFunc)
		}()

		wg.Wait()
	}

	// 等待命令完成
	err = cmd.Wait()
	result.Duration = time.Since(startTime)

	// 获取输出
	result.Stdout = stdoutBuf.String()
	result.Stderr = stderrBuf.String()

	// 获取退出码
	if err != nil {
		if exitErr, ok := err.(*exec.ExitError); ok {
			if status, ok := exitErr.Sys().(syscall.WaitStatus); ok {
				result.ExitCode = status.ExitStatus()
			}
			result.Err = exitErr
		} else {
			result.Err = err
		}
	} else {
		result.ExitCode = 0
		result.Success = true
	}

	// 检查是否超时
	if result.Err != nil && ctx.Err() == context.DeadlineExceeded {
		result.Err = fmt.Errorf("command timed out after %v: %v", options.Timeout, result.Err)
	}

	return result
}

// RunMultipleCommands 执行多条命令
func (ce *CommandExecutor) RunMultipleCommands(cmds []string, opts ...*CommandOptions) *CommandResult {
	combinedCmd := strings.Join(cmds, " && ")
	return ce.RunShell(combinedCmd, opts...)
}

// captureOutput 捕获输出
func (ce *CommandExecutor) captureOutput(pipe io.ReadCloser, buf *bytes.Buffer, captureFunc func(string)) {
	reader := bufio.NewReader(pipe)
	for {
		line, err := reader.ReadString('\n')
		if line != "" {
			buf.WriteString(line)
			if captureFunc != nil {
				captureFunc(strings.TrimSuffix(line, "\n"))
			}
		}
		if err != nil {
			break
		}
	}
}

// RunShell 执行shell命令
func (ce *CommandExecutor) RunShell(shellCmd string, opts ...*CommandOptions) *CommandResult {
	return ce.RunCommand("/bin/bash", []string{"-c", shellCmd}, opts...)
}

// RunShellWithOutput 执行shell命令并返回输出
func (ce *CommandExecutor) RunShellWithOutput(shellCmd string, opts ...*CommandOptions) (string, error) {
	result := ce.RunShell(shellCmd, opts...)
	if result.Err != nil {
		return "", fmt.Errorf("command failed: %v, stderr: %s", result.Err, result.Stderr)
	}
	return strings.TrimSpace(result.Stdout), nil
}

// RunWithTimeout 带超时的命令执行
func (ce *CommandExecutor) RunWithTimeout(cmdStr string, args []string, timeout time.Duration) *CommandResult {
	return ce.RunCommand(cmdStr, args, &CommandOptions{Timeout: timeout})
}

// RunWithEnv 带环境变量的命令执行
func (ce *CommandExecutor) RunWithEnv(cmdStr string, args []string, env map[string]string) *CommandResult {
	return ce.RunCommand(cmdStr, args, &CommandOptions{Env: env})
}

// RunAsync 异步执行命令
func (ce *CommandExecutor) RunAsync(cmdStr string, args []string, opts ...*CommandOptions) (*exec.Cmd, error) {
	options := &CommandOptions{Async: true}
	if len(opts) > 0 && opts[0] != nil {
		options = opts[0]
		options.Async = true
	}

	cmd := exec.Command(cmdStr, args...)

	if options.WorkDir != "" {
		cmd.Dir = options.WorkDir
	}

	if len(options.Env) > 0 {
		env := os.Environ()
		for k, v := range options.Env {
			env = append(env, fmt.Sprintf("%s=%s", k, v))
		}
		cmd.Env = env
	}

	// 设置输出
	if options.CaptureFunc != nil {
		stdoutPipe, err := cmd.StdoutPipe()
		if err != nil {
			return nil, err
		}
		stderrPipe, err := cmd.StderrPipe()
		if err != nil {
			return nil, err
		}

		go ce.captureOutput(stdoutPipe, &bytes.Buffer{}, options.CaptureFunc)
		go ce.captureOutput(stderrPipe, &bytes.Buffer{}, options.CaptureFunc)
	}

	if err := cmd.Start(); err != nil {
		return nil, err
	}

	return cmd, nil
}

// IsCommandAvailable 检查命令是否可用
func (ce *CommandExecutor) IsCommandAvailable(cmd string) bool {
	_, err := exec.LookPath(cmd)
	return err == nil
}

// GetExitCode 获取命令退出码（辅助函数）
func GetExitCode(err error) int {
	if err == nil {
		return 0
	}
	if exitErr, ok := err.(*exec.ExitError); ok {
		if status, ok := exitErr.Sys().(syscall.WaitStatus); ok {
			return status.ExitStatus()
		}
	}
	return -1
}
