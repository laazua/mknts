package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// Echo 服务器示例
// 启动：go run examples/server/echo_server.go
// 测试：telnet localhost 8080
func echoMain(address string) {
	// 创建服务器启动器
	server := bootstrap.NewServerBootstrap()

	// 设置 Channel 初始化函数
	server.SetHandler(func(ch *channel.Channel) {
		// 创建简单处理器
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[%s] Client connected\n", ctx.Channel().GetID())
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[%s] Client disconnected\n", ctx.Channel().GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[%s] Received: %s", ctx.Channel().GetID(), string(data))
					// 回显数据
					ctx.Channel().Write(data)
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	// 绑定端口
	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Echo Server started on " + address)
	fmt.Println("Test: telnet localhost 8080")
	select {}
}
