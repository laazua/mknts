package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// 连接到服务器
	conn, err := net.Dial("tcp", "localhost:8089")
	if err != nil {
		fmt.Printf("Error connecting to server: %v", err)
		return
	}
	defer conn.Close()
	fmt.Println("Connected to server at localhost:8080")

	//line := "xxxxxxxxxxxxxxxxx"
	// 创建一个扫描器从标准输入读取数据
	scanner := bufio.NewScanner(os.Stdin)
	// 读取用户输入
	scanner.Scan()
	line := scanner.Text()

	// 发送输入到服务器
	_, err = conn.Write([]byte(line + "\n"))
	if err != nil {
		fmt.Printf("Error sending message: %v", err)
		return
	}

	fmt.Println("Exiting...")
}
