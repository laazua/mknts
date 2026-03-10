package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// JSON 服务器示例
// 启动：go run examples/server/json_server.go
// 接收任意 JSON 数据并回复
func jsonMain() {
	server := bootstrap.NewServerBootstrap()

	// 创建 JSON 编码解码器
	jsonDecoder := codec.JSONDecoder{}
	jsonEncoder := codec.JSONEncoder{}

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[JSONServer] Client connected: %s\n", ctx.GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码 JSON
					parsed, err := jsonDecoder.Decode(data)
					if err != nil {
						fmt.Printf("[JSONServer] JSON decode error: %v\n", err)
						return
					}

					fmt.Printf("[JSONServer] Received JSON: %v\n", parsed)

					// 构造响应
					response := map[string]interface{}{
						"status":  "success",
						"message": "JSON received",
						"echo":    parsed,
					}

					// 编码响应
					respData, err := jsonEncoder.Encode(response)
					if err != nil {
						fmt.Printf("[JSONServer] JSON encode error: %v\n", err)
						return
					}

					// 添加换行符便于读取
					ctx.Write(append(respData, '\n'))
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[JSONServer] Client disconnected: %s\n", ctx.GetID())
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(":9011")
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("JSON Server started on :9011")
	fmt.Println("Expected format: {\"key1\": \"value1\", \"key2\": 123}")
	select {}
}
