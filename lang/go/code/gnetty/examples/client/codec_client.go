package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 编码解码器客户端示例
// 启动：go run examples/client/codec_client.go
func codecMain(address string) {
	// 创建客户端启动器
	client := bootstrap.NewClientBootstrap()

	// 创建编码器和解码器
	encoder := codec.NewLengthFieldEncoder(4)
	decoder := codec.NewLengthFieldDecoder(4)

	// 设置 Channel 初始化函数
	client.SetHandler(func(ch *channel.Channel) {
		// 创建简单处理器
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[Codec Client] Connected to server")
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[Codec Client] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码
					decoded, err := decoder.Decode(data)
					if err != nil {
						fmt.Printf("[Decode Error] %v\n", err)
						return
					}

					if decodedData, ok := decoded.([]byte); ok {
						fmt.Printf("[Server Response] %s\n", string(decodedData))
					}
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	// 连接到服务器
	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	// 读取用户输入并发送
	fmt.Println("Type message and press Enter (Ctrl+C to exit)")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		msg := scanner.Text()
		// 编码
		encoded, err := encoder.Encode(msg)
		if err != nil {
			fmt.Printf("[Encode Error] %v\n", err)
			continue
		}

		err = client.Write(encoded)
		if err != nil {
			fmt.Printf("Failed to send: %v\n", err)
			break
		}
		time.Sleep(100 * time.Millisecond)
	}

	client.Close()
}
