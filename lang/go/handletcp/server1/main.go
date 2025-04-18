package main

import (
	"bufio"
	"encoding/binary"
	"fmt"
        "io"
	"net"
	"sync"
)

const (
	headerSize = 4 // 假设消息头部为4个字节，表示消息长度
)

func handleConnection(conn net.Conn) {
	defer conn.Close()

	reader := bufio.NewReader(conn)

	for {
		// 读取消息头部
		headerBytes := make([]byte, headerSize)
		if _, err := io.ReadFull(reader, headerBytes); err != nil {
			fmt.Println("Error reading header:", err)
			return
		}

		// 解析消息长度
		messageLength := binary.BigEndian.Uint32(headerBytes)

		// 读取消息体
		messageBody := make([]byte, messageLength)
		if _, err := io.ReadFull(reader, messageBody); err != nil {
			fmt.Println("Error reading message body:", err)
			return
		}

		// 将消息发送回客户端
		if _, err := conn.Write(messageBody); err != nil {
			fmt.Println("Error writing message:", err)
			return
		}
	}
}

func main() {
	// 启动TCP服务器
	listener, err := net.Listen("tcp", ":8888")
	if err != nil {
		fmt.Println("Error listening:", err)
		return
	}
	defer listener.Close()

	fmt.Println("Server started. Listening on :8888")

	// 使用WaitGroup来处理并发任务
	var wg sync.WaitGroup

	for {
		// 接受客户端连接
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}

		// 对每个连接启动一个goroutine来处理
		wg.Add(1)
		go func() {
			defer wg.Done()
			handleConnection(conn)
		}()
	}

	// 等待所有goroutine完成
	wg.Wait()
}

