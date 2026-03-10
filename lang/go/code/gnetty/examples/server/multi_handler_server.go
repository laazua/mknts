package main

import (
	"fmt"
	"log"
	"strings"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// 多处理器链示例
// 启动：go run examples/server/multi_handler_server.go
// 测试：telnet localhost 9000
func handlerMain(address string) {
	server := bootstrap.NewServerBootstrap()

	server.SetHandler(func(ch *channel.Channel) {
		// 处理器1：日志记录
		logHandler := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[LogHandler] Channel active: %s\n", ctx.Channel().GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[LogHandler] Receive %d bytes\n", len(data))
				}
				ctx.Next(msg)
			})

		// 处理器2：数据转换（转换为大写）
		transformHandler := handler.NewSimpleInboundHandler().
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					upper := strings.ToUpper(string(data))
					fmt.Printf("[TransformHandler] Transform: %s -> %s\n", string(data), upper)
					ctx.Next([]byte(upper))
				}
			})

		// 处理器3：业务处理（回显）
		businessHandler := handler.NewSimpleInboundHandler().
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[BusinessHandler] Echo back: %s\n", string(data))
					ctx.Channel().Write(data)
				}
			})

		// 添加处理器链
		ch.GetPipeline().
			AddLast(logHandler).
			AddLast(transformHandler).
			AddLast(businessHandler)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Multi Handler Server started on " + address)
	fmt.Println("Test: telnet localhost " + strings.Split(address, ":")[1])
	select {}
}
