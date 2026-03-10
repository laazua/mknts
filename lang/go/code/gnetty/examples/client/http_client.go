package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// HTTP 客户端示例
// 启动：go run examples/client/http_client.go
func httpMain(address string) {
	// 创建客户端启动器
	client := bootstrap.NewClientBootstrap()

	// 设置 Channel 初始化函数
	client.SetHandler(func(ch *channel.Channel) {
		// 创建简单处理器
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[HTTP Client] Connected to server")

				// 发送 HTTP GET 请求
				httpRequest := "GET / HTTP/1.1\r\n" +
					"Host: localhost:8888\r\n" +
					"Connection: close\r\n" +
					"\r\n"

				ctx.Channel().Write([]byte(httpRequest))
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[HTTP Client] Connection closed")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[HTTP Response]\n%s", string(data))
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	// 连接到服务器
	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	// 保持连接
	select {}
}
