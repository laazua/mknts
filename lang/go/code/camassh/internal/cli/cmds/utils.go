package cmds

import (
	"bufio"
	"camassh/internal/sshx"
	"fmt"
	"os"
	"strings"
	"syscall"
	"unsafe"
)

func getPassword(prompt string) (string, error) {
	// 显示提示信息
	fmt.Print(prompt)

	// 获取终端原始模式
	var oldState syscall.Termios
	if _, _, err := syscall.Syscall6(
		syscall.SYS_IOCTL,
		uintptr(syscall.Stdin),
		uintptr(syscall.TCGETS),
		uintptr(unsafe.Pointer(&oldState)),
		0, 0, 0,
	); err != 0 {
		return "", err
	}

	// 设置终端为不回显模式
	newState := oldState
	newState.Lflag &^= syscall.ECHO
	if _, _, err := syscall.Syscall6(
		syscall.SYS_IOCTL,
		uintptr(syscall.Stdin),
		uintptr(syscall.TCSETS),
		uintptr(unsafe.Pointer(&newState)),
		0, 0, 0,
	); err != 0 {
		return "", err
	}

	// 读取密码
	reader := bufio.NewReader(os.Stdin)
	password, err := reader.ReadString('\n')
	if err != nil {
		return "", err
	}

	// 恢复终端设置
	if _, _, err := syscall.Syscall6(
		syscall.SYS_IOCTL,
		uintptr(syscall.Stdin),
		uintptr(syscall.TCSETS),
		uintptr(unsafe.Pointer(&oldState)),
		0, 0, 0,
	); err != 0 {
		return "", err
	}

	// 换行并返回清理后的密码
	fmt.Println()
	return strings.TrimSpace(password), nil
}

func strToInt(s string, defaultVal int) int {
	var i int
	_, err := fmt.Sscanf(s, "%d", &i)
	if err != nil {
		return defaultVal
	}
	return i
}

func getSshClient() (*sshx.Client, error) {
	var name, ipAddress, port string
	fmt.Print("请输入SSH登录IP地址: ")
	fmt.Scan(&ipAddress)
	fmt.Print("请输入SSH登录端口: ")
	fmt.Scan(&port)
	fmt.Print("请输入SSH登录用户: ")
	fmt.Scan(&name)
	// 安全的输入密码方式
	password, err := getPassword("请输入SSH登录密码: ")
	if err != nil {
		return nil, err
	}
	// 配置SSH连接
	sshConfig := &sshx.Config{
		Host:     strings.TrimSpace(ipAddress),
		Port:     strToInt(strings.TrimSpace(port), 22),
		Username: strings.TrimSpace(name),
		Password: strings.TrimSpace(password),
	}
	// 创建客户端
	client, err := sshx.NewClient(sshConfig)
	if err != nil {
		return nil, err
	}
	return client, nil
}
