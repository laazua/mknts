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

// 广播客户端示例（聊天室客户端）
// 启动：go run examples/client/broadcast_client.go
// 可以启动多个客户端实例
func broadcastMain(address string) {
	// 创建客户端启动器
	client := bootstrap.NewClientBootstrap()

	// 设置 Channel 初始化函数
	client.SetHandler(func(ch *channel.Channel) {
		// 创建简单处理器
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[Chat Client] Connected to chat room")
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[Chat Client] Disconnected from chat room")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("%s", string(data))
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
	fmt.Println("Connected to chat room. Type messages to send (Ctrl+C to exit)")
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
