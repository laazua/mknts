package main

import (
    "encoding/binary"
    "fmt"
    "net"
    "sync"
    "time"
)

const (
    serverAddr = "localhost:8888"
    numClients = 10
    numMessagesPerClient = 5
    headerSize = 4
)

func sendMessage(conn net.Conn, message []byte) error {
    // 计算消息长度
    messageLength := uint32(len(message))
    time.Sleep(time.Second * 2)

    // 写入消息头部（消息长度）
    header := make([]byte, headerSize)
    binary.BigEndian.PutUint32(header, messageLength)
    if _, err := conn.Write(header); err != nil {
        return err
    }

    // 写入消息体
    if _, err := conn.Write(message); err != nil {
        return err
    }

    return nil
}

func clientRoutine(clientNum int, wg *sync.WaitGroup) {
    defer wg.Done()

    // 连接到服务器
    conn, err := net.Dial("tcp", serverAddr)
    if err != nil {
        fmt.Printf("Client %d: Error connecting to server: %v\n", clientNum, err)
        return
    }
    defer conn.Close()

    for i := 0; i < numMessagesPerClient; i++ {
        message := []byte(fmt.Sprintf("Client %d: Message %d\n", clientNum, i+1))
        if err := sendMessage(conn, message); err != nil {
            fmt.Printf("Client %d: Error sending message: %v\n", clientNum, err)
            return
        }

        // 读取服务器的响应并打印
        response := make([]byte, len(message))
        if _, err := conn.Read(response); err != nil {
            fmt.Printf("Client %d: Error reading response: %v\n", clientNum, err)
            return
        }
        fmt.Printf("Client %d: Received response: %s", clientNum, response)
    }
}

func main() {
    var wg sync.WaitGroup

    // 启动多个客户端
    for i := 0; i < numClients; i++ {
        wg.Add(1)
        go clientRoutine(i+1, &wg)
    }

    // 等待所有客户端完成
    wg.Wait()
}

