package main

import (
	"encoding/binary"
	"fmt"
	"log/slog"
	"net"
)

func main() {
	// 连接到服务器
	conn, err := net.Dial("tcp", "localhost:8044")
	if err != nil {
		slog.Error("Connect Server Error", slog.String("error", err.Error()))
		return
	}
	defer conn.Close()

	// 构造消息1
	message1 := []byte("Hello, this is message 1")
	length1 := uint32(len(message1))

	// 构造消息2
	message2 := []byte("Hello, this is message 2")
	length2 := uint32(len(message2))

	// 发送消息1
	binary.Write(conn, binary.BigEndian, length1)
	conn.Write(message1)

	// 发送消息2
	binary.Write(conn, binary.BigEndian, length2)
	conn.Write(message2)

	fmt.Println("Messages sent")
}
