package main

import (
	"bufio"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"io"
	"net"
	"time"

	"sksrv/pkg/codec"
	"sksrv/pkg/comm"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8886")
	if err != nil {
		fmt.Printf("Dial error: %v\n", err)
		return
	}
	defer conn.Close()

	codec := &codec.JsonCodec{}

	// 发送认证消息(与服务端匹配一致)
	authInfo := comm.AuthInfo{Token: "aaaxxx"}
	authData, _ := json.Marshal(authInfo)
	authMsg := &comm.Message{
		Type:     comm.AuthMsg,
		Data:     authData,
		CreateAt: time.Now(),
	}

	if err := sendMessage(conn, codec, authMsg); err != nil {
		fmt.Printf("Auth error: %v\n", err)
		return
	}

	// 读取认证响应
	authResp, err := readMessage(conn, codec)
	if err != nil {
		fmt.Printf("Read auth response error: %v\n", err)
		return
	}
	fmt.Printf("Auth response: %s\n", string(authResp.Data))

	// 发送心跳
	go func() {
		ticker := time.NewTicker(comm.BeatInterval)
		defer ticker.Stop()

		for {
			select {
			case <-ticker.C:
				heartbeatMsg := &comm.Message{
					Type:     comm.BeatMsg,
					CreateAt: time.Now(),
				}

				if err := sendMessage(conn, codec, heartbeatMsg); err != nil {
					fmt.Printf("Send heartbeat error: %v\n", err)
					return
				}
			default:
				continue
			}
		}
	}()

	// 发送数据消息
	messages := []string{"Hello", "World", "Golang TCP Server Demo ..................."}
	for _, msg := range messages {
		dataMsg := &comm.Message{
			Type:     comm.DataMsg,
			Data:     []byte(msg),
			CreateAt: time.Now(),
		}

		if err := sendMessage(conn, codec, dataMsg); err != nil {
			fmt.Printf("Send message error: %v\n", err)
			return
		}

		// 读取响应
		resp, err := readMessage(conn, codec)
		if err != nil {
			fmt.Printf("Read response error: %v\n", err)
			return
		}

		fmt.Printf("Server response: %s\n", string(resp.Data))
		time.Sleep(1 * time.Second)
	}
}

func sendMessage(conn net.Conn, codec codec.Codec, msg *comm.Message) error {
	// 编码消息
	data, err := codec.Encode(msg)
	if err != nil {
		return err
	}

	// 写入消息长度
	length := make([]byte, comm.MsgLength)
	binary.BigEndian.PutUint32(length, uint32(len(data)))
	if _, err := conn.Write(length); err != nil {
		return err
	}

	// 写入消息内容
	if _, err := conn.Write(data); err != nil {
		return err
	}

	return nil
}

func readMessage(conn net.Conn, codec codec.Codec) (*comm.Message, error) {
	reader := bufio.NewReader(conn)

	// 读取消息长度
	lengthBuf := make([]byte, comm.MsgLength)
	if _, err := io.ReadFull(reader, lengthBuf); err != nil {
		return nil, err
	}

	length := binary.BigEndian.Uint32(lengthBuf)

	// 读取消息内容
	data := make([]byte, length)
	if _, err := io.ReadFull(reader, data); err != nil {
		return nil, err
	}

	// 解码消息
	return codec.Decode(data)
}
