package ssh

import (
	"bytes"
	"fmt"
	"time"

	"golang.org/x/crypto/ssh"
)

type SSHClient struct {
	Host     string
	Port     int
	User     string
	Password string
}

type Option func(s *SSHClient)

func WithHost(host string) Option {
	return func(s *SSHClient) {
		s.Host = host
	}
}

func WithPort(port int) Option {
	return func(s *SSHClient) {
		s.Port = port
	}
}

func WithUser(user string) Option {
	return func(s *SSHClient) {
		s.User = user
	}
}

func WithPassword(password string) Option {
	return func(s *SSHClient) {
		s.Password = password
	}
}

func NewSsh(options ...Option) *SSHClient {
	client := &SSHClient{
		Port: 22,
	}
	for _, option := range options {
		option(client)
	}
	return client
}

// RunCommand 通过 SSH 执行命令并返回结果
func (client *SSHClient) RunCommand(cmd string) (string, error) {
	config := &ssh.ClientConfig{
		User: client.User,
		Auth: []ssh.AuthMethod{
			ssh.Password(client.Password),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		Timeout:         5 * time.Second,
	}

	address := fmt.Sprintf("%s:%d", client.Host, client.Port)
	conn, err := ssh.Dial("tcp", address, config)
	if err != nil {
		return "", fmt.Errorf("无法连接到 %s: %v", client.Host, err)
	}
	defer conn.Close()

	session, err := conn.NewSession()
	if err != nil {
		return "", fmt.Errorf("创建SSH会话失败: %v", err)
	}
	defer session.Close()

	var stdout, stderr bytes.Buffer
	session.Stdout = &stdout
	session.Stderr = &stderr

	if err := session.Run(cmd); err != nil {
		return "", fmt.Errorf("执行命令失败: %v, 错误: %s", err, stderr.String())
	}

	return stdout.String(), nil
}
