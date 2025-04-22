package main

import (
	"fmt"
	"os"
	"os/exec"
	"plugin"
)

// 定义插件接口
type PluginInterface interface {
	Execute(args ...string) error
}

// 加载插件
func loadPlugin(path string) (PluginInterface, error) {
	plug, err := plugin.Open(path)
	if err != nil {
		return nil, err
	}

	sym, err := plug.Lookup("Plugin")
	if err != nil {
		return nil, err
	}

	pluginInstance, ok := sym.(PluginInterface)
	if !ok {
		return nil, fmt.Errorf("unexpected type from module symbol")
	}
	return pluginInstance, nil
}

// 执行外部命令
func executeCommand(command string, args ...string) error {
	cmd := exec.Command(command, args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

func main() {
	// 加载并执行 Golang 插件
	pluginPath := "plugins/demo.so"
	p, err := loadPlugin(pluginPath)
	if err != nil {
		fmt.Println("加载插件失败:", err)
		return
	}

	err = p.Execute("Hello", "from", "plugin")
	if err != nil {
		fmt.Println("插件执行失败:", err)
		return
	}

	// 执行 shell 命令
	err = executeCommand("sh", "-c", "cmd/test.sh")
	if err != nil {
		fmt.Println("Shell 命令执行失败:", err)
		return
	}

	// 执行 Python 脚本
	err = executeCommand("python3", "cmd/test.py")
	if err != nil {
		fmt.Println("Python 脚本执行失败:", err)
		return
	}

	// 执行 Golang 编译的二进制文件
	err = executeCommand("cmd/main")
	if err != nil {
		fmt.Println("二进制文件执行失败:", err)
		return
	}
}

