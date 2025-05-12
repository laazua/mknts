package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// 监听端口
	listener, err := net.Listen("tcp", ":8089")
	if err != nil {
		fmt.Println("Error starting server:", err)
		os.Exit(1)
	}
	defer listener.Close()
	fmt.Println("Server is listening on port 8089...")

	for {
		// 接受连接
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
	fmt.Println("Client connected:", conn.RemoteAddr())

	// 使用 bufio.NewScanner 读取数据
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println("Received:", line)
		// 可以在这里处理接收到的行
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading from connection:", err)
	}
}
