package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 用户结构体
type User struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
}

// 响应结构体
type Response struct {
	Code    int         `json:"code"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// 结构体客户端示例
// 启动：go run examples/client/struct_client.go
func structMain(address string) {
	client := bootstrap.NewClientBootstrap()

	encoder := codec.NewStructEncoder(4)
	decoder := codec.NewStructDecoder(4)

	client.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[StructClient] Connected to server")
				fmt.Println("Enter user data as JSON: {\"id\": 1, \"name\": \"Alice\", \"age\": 25}")
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[StructClient] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码响应
					var resp Response
					err := decoder.DecodeToStruct(data, &resp)
					if err != nil {
						fmt.Printf("[StructClient] Decode error: %v\n", err)
						return
					}

					fmt.Printf("[StructClient] Response Code: %d, Message: %s\n", resp.Code, resp.Message)
					if resp.Data != nil {
						dataJSON, _ := json.MarshalIndent(resp.Data, "", "  ")
						fmt.Printf("[StructClient] Response Data:\n%s\n", string(dataJSON))
					}
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	// 读取用户输入
	fmt.Println("Type user JSON and press Enter (Ctrl+C to exit)")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input := scanner.Text()
		if input == "" {
			continue
		}

		// 解析 JSON 到 User 结构体
		var user User
		err := json.Unmarshal([]byte(input), &user)
		if err != nil {
			fmt.Printf("Invalid JSON: %v\n", err)
			continue
		}

		// 编码并发送
		data, err := encoder.Encode(user)
		if err != nil {
			fmt.Printf("Encode error: %v\n", err)
			continue
		}

		err = client.Write(data)
		if err != nil {
			fmt.Printf("Send error: %v\n", err)
			break
		}

		time.Sleep(100 * time.Millisecond)
	}

	client.Close()
}
