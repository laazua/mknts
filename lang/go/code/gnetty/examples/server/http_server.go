package main

import (
	"fmt"
	"log"
	"strings"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// 简单的 HTTP 服务器示例
// 启动：go run examples/server/http_server.go
// 测试：curl http://localhost:8888/
func httpMain(address string) {
	server := bootstrap.NewServerBootstrap()

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					request := string(data)

					// 简单的 HTTP 请求解析
					lines := strings.Split(request, "\r\n")
					if len(lines) > 0 {
						fmt.Printf("[HTTP] Request: %s\n", lines[0])

						// 构造 HTTP 响应
						response := "HTTP/1.1 200 OK\r\n" +
							"Content-Type: text/html\r\n" +
							"Content-Length: 21\r\n" +
							"Connection: close\r\n" +
							"\r\n" +
							"<h1>Welcome!</h1>\r\n"

						ctx.Channel().Write([]byte(response))
					}
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[HTTP] Connection closed: %s\n", ctx.Channel().GetID())
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("HTTP Server started on " + address)
	fmt.Println("Test: curl http://localhost:8888/")
	select {}
}
