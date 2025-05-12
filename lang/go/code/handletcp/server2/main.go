package main

import (
    "bufio"
    "encoding/binary"
    "fmt"
    "net"
)

const (
    headerSize = 4 // 假设消息头部为4个字节，表示消息长度
    maxConcurrentConnections = 2 // 最大并发连接数
)

func handleConnection(conn net.Conn, sem chan struct{}) {
    defer conn.Close()

    // 释放信号量
    defer func() { <-sem }()

    reader := bufio.NewReader(conn)

    for {
        // 读取消息头部
        headerBytes := make([]byte, headerSize)
        if _, err := reader.Read(headerBytes); err != nil {
            fmt.Println("Error reading header:", err)
            return
        }

        // 解析消息长度
        messageLength := binary.BigEndian.Uint32(headerBytes)

        // 读取消息体
        messageBody := make([]byte, messageLength)
        if _, err := reader.Read(messageBody); err != nil {
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
    // 创建带缓冲的通道，用于限制并发连接数
    sem := make(chan struct{}, maxConcurrentConnections)

    // 启动TCP服务器
    listener, err := net.Listen("tcp", ":8888")
    if err != nil {
        fmt.Println("Error listening:", err)
        return
    }
    defer listener.Close()

    fmt.Println("Server started. Listening on :8888")

    for {
        // 接受客户端连接
        conn, err := listener.Accept()
        if err != nil {
            fmt.Println("Error accepting connection:", err)
            continue
        }

        // 获取信号量
        sem <- struct{}{}

        // 处理连接
        go handleConnection(conn, sem)
    }
}

