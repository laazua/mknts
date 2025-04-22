package code

import (
	"encoding/binary"
	"fmt"
	"net"
	"os"
)

func cMain() {
	// 连接到Agent的地址和端口
	host := "localhost"
	port := "8888"
	addr := host + ":" + port

	conn, err := net.Dial("tcp", addr)
	if err != nil {
		fmt.Println("Error connecting:", err)
		os.Exit(1)
	}
	defer conn.Close()

	// 要发送的消息
	message := `{"name": "zhangsan", "address": "chengdu"}`

	// 封包：在消息前添加消息长度前缀
	prefix := make([]byte, 4)
	binary.BigEndian.PutUint32(prefix, uint32(len(message)))
	packet := append(prefix, []byte(message)...)

	// 发送封包后的消息
	_, err = conn.Write(packet)
	if err != nil {
		fmt.Println("Error sending message:", err)
		return
	}

	fmt.Println("Message sent:", message)
}
