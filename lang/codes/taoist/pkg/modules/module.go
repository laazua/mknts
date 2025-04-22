package module

import "taoist/pkg/ssh"

type Module interface {
	Execute(ssh *ssh.SSHClient) (string, error)
}

// command 模块
type Command struct {
	Arg string `yaml:"arg"`
}

func (c *Command) Execute(sc *ssh.SSHClient) (string, error) {
	result, err := sc.RunCommand(c.Arg)
	if err != nil {
		return "", err
	}
	return result, nil
}

// Copy模块
type Copy struct {
	Src string `yaml:"src"`
	Dst string `yaml:"dst"`
}

func (c *Copy) Execute(sc *ssh.SSHClient) (string, error) {
	return "", nil
}
