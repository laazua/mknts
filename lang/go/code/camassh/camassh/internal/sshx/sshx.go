// Package sshx 提供简洁的SSH客户端功能
package sshx

import (
	"bytes"
	"fmt"
	"io"
	"time"

	"golang.org/x/crypto/ssh"
)

// Client SSH客户端
type Client struct {
	client *ssh.Client
}

// CommandResult 命令执行结果
type CommandResult struct {
	Stdout   string
	Stderr   string
	ExitCode int
}

type Config struct {
	Host       string
	Port       int
	Username   string
	Password   string
	Timeout    int
	PrivateKey []byte
}

// NewClient 创建SSH客户端连接
func NewClient(config *Config) (*Client, error) {
	var authMethods []ssh.AuthMethod

	// 密码认证
	if config.Password != "" {
		authMethods = append(authMethods, ssh.Password(config.Password))
	}

	// 密钥认证
	if len(config.PrivateKey) > 0 {
		signer, err := ssh.ParsePrivateKey(config.PrivateKey)
		if err != nil {
			return nil, fmt.Errorf("parse private key failed: %w", err)
		}
		authMethods = append(authMethods, ssh.PublicKeys(signer))
	}

	if len(authMethods) == 0 {
		return nil, fmt.Errorf("no authentication method provided")
	}

	sshConfig := &ssh.ClientConfig{
		User:            config.Username,
		Auth:            authMethods,
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		Timeout:         30 * time.Second,
	}

	if config.Port == 0 {
		config.Port = 22
	}

	address := fmt.Sprintf("%s:%d", config.Host, config.Port)
	client, err := ssh.Dial("tcp", address, sshConfig)
	if err != nil {
		return nil, fmt.Errorf("ssh dial failed: %w", err)
	}

	return &Client{client: client}, nil
}

// NewClientWithKeyFile 从文件读取私钥创建客户端
func NewClientWithKeyFile(config *Config) (*Client, error) {
	// 这里简化处理，实际使用时需要读取文件
	return NewClient(config)
}

// Close 关闭连接
func (c *Client) Close() error {
	if c.client != nil {
		return c.client.Close()
	}
	return nil
}

// Run 执行命令并返回结果
func (c *Client) Run(cmd string) (*CommandResult, error) {
	session, err := c.client.NewSession()
	if err != nil {
		return nil, err
	}
	defer session.Close()

	var stdout, stderr bytes.Buffer
	session.Stdout = &stdout
	session.Stderr = &stderr

	err = session.Run(cmd)
	exitCode := 0
	if err != nil {
		if exitErr, ok := err.(*ssh.ExitError); ok {
			exitCode = exitErr.ExitStatus()
		} else {
			return nil, err
		}
	}

	return &CommandResult{
		Stdout:   stdout.String(),
		Stderr:   stderr.String(),
		ExitCode: exitCode,
	}, nil
}

// RunWithPty 使用PTY执行命令（支持交互式程序）
func (c *Client) RunWithPty(cmd string, rows, cols int) (*CommandResult, error) {
	session, err := c.client.NewSession()
	if err != nil {
		return nil, err
	}
	defer session.Close()

	modes := ssh.TerminalModes{
		ssh.ECHO:          0,
		ssh.TTY_OP_ISPEED: 14400,
		ssh.TTY_OP_OSPEED: 14400,
	}

	if err := session.RequestPty("xterm", rows, cols, modes); err != nil {
		return nil, fmt.Errorf("request pty failed: %w", err)
	}

	var stdout, stderr bytes.Buffer
	session.Stdout = &stdout
	session.Stderr = &stderr

	err = session.Run(cmd)
	if err != nil {
		return nil, err
	}

	return &CommandResult{
		Stdout: stdout.String(),
		Stderr: stderr.String(),
	}, nil
}

// Stream 流式执行命令（实时输出）
func (c *Client) Stream(cmd string, stdoutWriter, stderrWriter io.Writer) error {
	session, err := c.client.NewSession()
	if err != nil {
		return err
	}
	defer session.Close()

	session.Stdout = stdoutWriter
	session.Stderr = stderrWriter

	return session.Run(cmd)
}

// Shell 启动交互式Shell
func (c *Client) Shell(stdin io.Reader, stdout, stderr io.Writer) error {
	session, err := c.client.NewSession()
	if err != nil {
		return err
	}
	defer session.Close()

	session.Stdin = stdin
	session.Stdout = stdout
	session.Stderr = stderr

	modes := ssh.TerminalModes{
		ssh.ECHO:          1,
		ssh.ECHOCTL:       0,
		ssh.TTY_OP_ISPEED: 14400,
		ssh.TTY_OP_OSPEED: 14400,
	}

	if err := session.RequestPty("xterm", 40, 80, modes); err != nil {
		return err
	}

	if err := session.Shell(); err != nil {
		return err
	}

	return session.Wait()
}

// RunMultiple 批量执行命令
func (c *Client) RunMultiple(commands []string) ([]*CommandResult, error) {
	results := make([]*CommandResult, len(commands))

	for i, cmd := range commands {
		result, err := c.Run(cmd)
		if err != nil {
			return results, fmt.Errorf("command '%s' failed: %w", cmd, err)
		}
		results[i] = result
	}

	return results, nil
}

// TestConnection 测试连接是否可用
func (c *Client) TestConnection() error {
	result, err := c.Run("echo test")
	if err != nil {
		return err
	}

	if result.Stdout != "test\n" {
		return fmt.Errorf("unexpected output: %s", result.Stdout)
	}

	return nil
}
