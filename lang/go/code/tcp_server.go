package code

import (
	"encoding/binary"
	"fmt"
	"io"
	"net"
	"os"
)

func sMain() {
	host := "localhost"
	port := "8888"
	addr := host + ":" + port

	listener, err := net.Listen("tcp", addr)
	if err != nil {
		fmt.Println("Error listening:", err)
		os.Exit(1)
	}
	defer listener.Close()
	fmt.Println("Agent listening on " + addr)

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			os.Exit(1)
		}

		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
	for {
		// 读取消息长度前缀
		var lengthBuf [4]byte
		_, err := conn.Read(lengthBuf[:])
		if err == io.EOF {
			return
		}
		if err != nil {
			fmt.Println("Error reading message length:", err)
			return
		}
		length := binary.BigEndian.Uint32(lengthBuf[:])

		// 读取消息内容
		buf := make([]byte, length)
		_, err = conn.Read(buf)
		if err != nil {
			fmt.Println("Error reading message content:", err)
			return
		}

		// 执行操作
		fmt.Printf("Received command: %s\n", string(buf))
	}
}
