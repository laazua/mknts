package main

import (
	"io"
	"log"
	"net"
)

func main() {
	// 监听本地端口
	listener, err := net.Listen("tcp", ":8081")
	if err != nil {
		log.Fatalf("Error starting server: %v", err)
	}
	defer listener.Close()

	log.Println("TCP proxy server listening on :8080")

	for {
		// 接受新的连接
		clientConn, err := listener.Accept()
		if err != nil {
			log.Printf("Error accepting connection: %v", err)
			continue
		}

		go handleConnection(clientConn)
	}
}

func handleConnection(clientConn net.Conn) {
	defer clientConn.Close()

	// 连接到目标服务器
	targetConn, err := net.Dial("tcp", "192.168.165.88:8081") // 目标地址和端口
	if err != nil {
		log.Printf("Error connecting to target: %v", err)
		return
	}
	defer targetConn.Close()

	// 使用 goroutine 同时转发数据
	go io.Copy(targetConn, clientConn) // 将客户端数据转发到目标服务器
	io.Copy(clientConn, targetConn)     // 将目标服务器的数据转发回客户端
}
