### socket

- 使用 encoding/gob 包对数据序列化

```
package core

import (
	"encoding/gob"
	"fmt"
	"net"
)

// Message 结构体定义
type Message struct {
	Content string
}

func StartServer() {
	// 监听端口
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println("Error listening:", err)
		return
	}
	defer listener.Close()

	fmt.Println("Server listening on :8080")

	for {
		// 等待客户端连接
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			return
		}

		// 处理客户端连接
		go handleClient(conn)
	}
}

func handleClient(conn net.Conn) {
	// 创建编码器和解码器
	encoder := gob.NewEncoder(conn)
	decoder := gob.NewDecoder(conn)

	// 发送消息给客户端
	message := Message{Content: "Hello, client!"}
	encoder.Encode(message)

	// 接收来自客户端的消息
	var receivedMessage Message
	decoder.Decode(&receivedMessage)
	fmt.Println("Received message from client:", receivedMessage.Content)

	conn.Close()
}

func Client() {
	// 连接到服务器
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}
	defer conn.Close()

	// 创建编码器和解码器
	encoder := gob.NewEncoder(conn)
	decoder := gob.NewDecoder(conn)

	// 接收来自服务器的消息
	var receivedMessage Message
	decoder.Decode(&receivedMessage)
	fmt.Println("Received message from server:", receivedMessage.Content)

	// 发送消息给服务器
	message := Message{Content: "Hello, server!"}
	encoder.Encode(message)
}

```

- 服务端使用

```
package main

func main() {
	StartServer()
}
```

- 客户端使用

```
package main

func main() {
    Client()
}
```
