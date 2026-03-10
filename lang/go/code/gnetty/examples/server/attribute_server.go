package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// Channel 属性存储示例
// 启动：go run examples/server/attribute_server.go
// 测试：telnet localhost 9002
func attributeMain(address string) {
	server := bootstrap.NewServerBootstrap()

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				// 初始化 Channel 属性
				ctx.Channel().SetAttr("messageCount", 0)
				ctx.Channel().SetAttr("isAuthenticated", false)
				fmt.Printf("[Attribute] Channel %s initialized\n", ctx.Channel().GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					command := string(data)

					// 获取当前的消息计数
					count := ctx.Channel().GetAttr("messageCount").(int)
					count++
					ctx.Channel().SetAttr("messageCount", count)

					// 根据命令处理
					var response string
					switch string(data[:len(data)-1]) {
					case "login":
						ctx.Channel().SetAttr("isAuthenticated", true)
						auth := ctx.Channel().GetAttr("isAuthenticated").(bool)
						response = fmt.Sprintf("Login success. Authenticated: %v\n", auth)

					case "info":
						count := ctx.Channel().GetAttr("messageCount").(int)
						auth := ctx.Channel().GetAttr("isAuthenticated").(bool)
						response = fmt.Sprintf("Count: %d, Auth: %v\n", count, auth)

					case "logout":
						ctx.Channel().SetAttr("isAuthenticated", false)
						response = "Logout success\n"

					default:
						response = fmt.Sprintf("Message #%d: %s", count, command)
					}

					ctx.Channel().Write([]byte(response))
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Attribute Server started on " + address)
	fmt.Println("Commands: login, info, logout")
	select {}
}
