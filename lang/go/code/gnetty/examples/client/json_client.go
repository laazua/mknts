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

// JSON 客户端示例
// 启动：go run examples/client/json_client.go
func jsonMain(address string) {
	client := bootstrap.NewClientBootstrap()

	jsonEncoder := codec.JSONEncoder{}
	jsonDecoder := codec.JSONDecoder{}

	client.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[JSONClient] Connected to server")
				fmt.Println("Enter JSON data and press Enter")
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[JSONClient] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码响应
					parsed, err := jsonDecoder.Decode(data)
					if err != nil {
						fmt.Printf("[JSONClient] Decode error: %v\n", err)
						return
					}

					// 格式化输出
					responseJSON, _ := json.MarshalIndent(parsed, "", "  ")
					fmt.Printf("[Server Response]:\n%s\n", string(responseJSON))
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	fmt.Println("Type JSON and press Enter (Ctrl+C to exit)")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input := scanner.Text()
		if input == "" {
			continue
		}

		// 验证 JSON 格式
		var data interface{}
		err := json.Unmarshal([]byte(input), &data)
		if err != nil {
			fmt.Printf("Invalid JSON: %v\n", err)
			continue
		}

		// 编码并发送
		encoded, err := jsonEncoder.Encode(data)
		if err != nil {
			fmt.Printf("Encode error: %v\n", err)
			continue
		}

		// 添加换行符
		err = client.Write(append(encoded, '\n'))
		if err != nil {
			fmt.Printf("Send error: %v\n", err)
			break
		}

		time.Sleep(100 * time.Millisecond)
	}

	client.Close()
}
