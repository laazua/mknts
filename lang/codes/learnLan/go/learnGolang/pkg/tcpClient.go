// tcp client
package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"net"
)

// 编码消息
func EncodeMessage(message string) ([]byte, error) {
	// 读取消息长度,转换成int32类型(占4字节)
	length := int32(len(message))
	buffer := new(bytes.Buffer)

	// 写入消息头
	if err := binary.Write(buffer, binary.LittleEndian, length); err != nil {
		return nil, err
	}

	// 写入消息实体
	if err := binary.Write(buffer, binary.LittleEndian, []byte(message)); err != nil {
		return nil, err
	}

	return buffer.Bytes(), nil
}

func main() {
	if conn, err := net.Dial("tcp", "0.0.0.0:8888"); err != nil {
		return
	} else {
		defer conn.Close()
		for i := 0; i < 10; i++ {
			msg := `hello, ni hao.`
			if data, err := EncodeMessage(msg); err != nil {
				fmt.Println("encode message error:", err)
				return
			} else {
				conn.Write(data)
			}
		}
	}
}
