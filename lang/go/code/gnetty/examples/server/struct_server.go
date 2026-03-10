package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 用户结构体
type User struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
}

// 响应结构体
type Response struct {
	Code    int         `json:"code"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// 结构体服务器示例
// 启动：go run examples/server/struct_server.go
// 接收 JSON 格式的用户数据并返回响应
func structMain() {
	server := bootstrap.NewServerBootstrap()

	// 创建编码解码器
	encoder := codec.NewStructEncoder(4)
	decoder := codec.NewStructDecoder(4)

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[StructServer] Client connected: %s\n", ctx.GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码为 User 结构体
					var user User
					err := decoder.DecodeToStruct(data, &user)
					if err != nil {
						fmt.Printf("[StructServer] Decode error: %v\n", err)

						// 返回错误响应
						errResp := Response{
							Code:    500,
							Message: "Decode failed",
						}
						respData, _ := encoder.Encode(errResp)
						ctx.Write(respData)
						return
					}

					fmt.Printf("[StructServer] Received user: ID=%d, Name=%s, Age=%d\n",
						user.ID, user.Name, user.Age)

					// 处理数据并返回响应
					resp := Response{
						Code:    200,
						Message: "User received successfully",
						Data: map[string]interface{}{
							"received_user": user,
							"processed_at":  "2026-03-10T10:30:00Z",
						},
					}

					respData, err := encoder.Encode(resp)
					if err != nil {
						fmt.Printf("[StructServer] Encode error: %v\n", err)
						return
					}

					ctx.Write(respData)
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[StructServer] Client disconnected: %s\n", ctx.GetID())
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(":9010")
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Struct Server started on :9010")
	fmt.Println("Expected format: {\"id\": 1, \"name\": \"Alice\", \"age\": 25}")
	select {}
}
