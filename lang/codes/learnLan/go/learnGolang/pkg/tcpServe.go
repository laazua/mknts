// tcp server
package main

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"net"
)

// 解码消息
func DecodeMessage(reader *bufio.Reader) (string, error) {
	// 读取消息长度
	lengthByte, _ := reader.Peek(4) // 读取前4个字节的数据
	lengthBuff := bytes.NewBuffer(lengthByte)

	// buffered返回缓冲中现有的可读取的字节数
	var length int32
	if err := binary.Read(lengthBuff, binary.LittleEndian, &length); err != nil || int32(reader.Buffered()) < length+4 {
		return "", err
	}

	// 读取实际消息中的数据
	pack := make([]byte, int(4+length))
	if _, err := reader.Read(pack); err != nil {
		return "", err
	}
	return string(pack[4:]), nil
}

func process(conn net.Conn) {
	defer conn.Close()
	reader := bufio.NewReader(conn)
	for {
		if msg, err := DecodeMessage(reader); err == io.EOF || err != nil {
			fmt.Println("decode message error:", err)
			break
		} else {
			fmt.Println(msg)
		}
	}
}

func main() {
	if listen, err := net.Listen("tcp", "0.0.0.0:8888"); err != nil {
		return
	} else {
		defer listen.Close()
		for {
			if conn, err := listen.Accept(); err != nil {
				fmt.Println("accept failed, error:", err)
				continue
			} else {
				go process(conn)
			}
		}
	}
}
