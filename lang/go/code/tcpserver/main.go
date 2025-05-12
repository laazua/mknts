package main

import (
	"encoding/binary"
	"fmt"
	"io"
	"log/slog"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", ":8044")
	if err != nil {
		slog.Error("Sever Listen Error", slog.String("error", err.Error()))
		return
	}
	defer listener.Close()

	slog.Info("Server Listen on", slog.String("address", ":8044"))
	// 处理客户端连接
	for {
		conn, err := listener.Accept()
		if err != nil {
			slog.Error("Server Accept Error", slog.String("error", err.Error()))
			continue
		}
		go handleConn(conn)
	}
}

func handleConn(conn net.Conn) {
	defer conn.Close()
	buffer := make([]byte, 10240) // 创建缓存区,用于读取conn数据
	for {
		slog.Info("Remote Client", slog.String("address", conn.RemoteAddr().String()))
		// 读取前4字节
		_, err := io.ReadFull(conn, buffer[:4])
		if err != nil && err != io.EOF {
			slog.Error("Read Conn Header Error", slog.String("error", err.Error()))
			return
		}
		if err == io.EOF {
			break
		}
		// 获取消息体长度
		msgLen := binary.BigEndian.Uint32(buffer[:4])
		// 读取消息体数据
		_, err = io.ReadFull(conn, buffer[:msgLen])
		if err != nil {
			slog.Error("Read Conn Message Body Error", slog.String("error", err.Error()))
			return
		}
		// 输出接收到的消息
		fmt.Printf("Received: %s\n", string(buffer[:msgLen]))
	}
}
