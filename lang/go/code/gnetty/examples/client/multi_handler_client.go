package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// 多处理器链客户端示例
// 启动：go run examples/client/multi_handler_client.go
func handlerMain(address string) {
	// 创建客户端启动器
	client := bootstrap.NewClientBootstrap()

	// 设置 Channel 初始化函数
	client.SetHandler(func(ch *channel.Channel) {
		// 创建简单处理器
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[Multi Handler Client] Connected to server")
				fmt.Println("Send messages, they will be converted to uppercase on server")
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[Multi Handler Client] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[Server Response] %s", string(data))
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
		msg := scanner.Bytes()
		err := client.Write(append(msg, '\n'))
		if err != nil {
			fmt.Printf("Failed to send: %v\n", err)
			break
		}
		time.Sleep(100 * time.Millisecond)
	}

	client.Close()
}
