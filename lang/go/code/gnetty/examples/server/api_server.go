package main

import (
	"fmt"
	"log"
	"time"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 请求结构体
type Request struct {
	Action string                 `json:"action"`
	Params map[string]interface{} `json:"params"`
}

// 响应结构体
type APIResponse struct {
	RequestID string      `json:"request_id"`
	Status    string      `json:"status"`
	Code      int         `json:"code"`
	Message   string      `json:"message"`
	Data      interface{} `json:"data,omitempty"`
	Timestamp string      `json:"timestamp"`
}

// 简单的 API 服务器示例
// 启动：go run examples/server/api_server.go
func apiMain(address string) {
	server := bootstrap.NewServerBootstrap()

	encoder := codec.NewStructEncoder(4)
	decoder := codec.NewStructDecoder(4)

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[APIServer] Client connected: %s\n", ctx.GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码请求
					var req Request
					err := decoder.DecodeToStruct(data, &req)
					if err != nil {
						fmt.Printf("[APIServer] Decode error: %v\n", err)
						return
					}

					fmt.Printf("[APIServer] Received action: %s, params: %v\n", req.Action, req.Params)

					// 处理不同的 action
					var respData interface{}
					var statusCode int
					var message string

					switch req.Action {
					case "query_user":
						statusCode = 200
						message = "User query success"
						respData = map[string]interface{}{
							"user_id": 123,
							"name":    "Alice",
							"email":   "alice@example.com",
						}

					case "create_order":
						statusCode = 201
						message = "Order created successfully"
						respData = map[string]interface{}{
							"order_id": "ORD-2026-001",
							"total":    99.99,
							"items":    2,
						}

					case "update_profile":
						statusCode = 200
						message = "Profile updated"
						respData = req.Params

					case "list_items":
						statusCode = 200
						message = "Items retrieved"
						respData = []map[string]interface{}{
							{"id": 1, "name": "Item 1"},
							{"id": 2, "name": "Item 2"},
							{"id": 3, "name": "Item 3"},
						}

					default:
						statusCode = 404
						message = "Unknown action"
					}

					// 构造响应
					resp := APIResponse{
						RequestID: ctx.GetID(),
						Status:    map[int]string{200: "ok", 201: "created", 404: "error", 500: "error"}[statusCode],
						Code:      statusCode,
						Message:   message,
						Data:      respData,
						Timestamp: time.Now().Format("2006-01-02T15:04:05Z07:00"),
					}

					respBytes, err := encoder.Encode(resp)
					if err != nil {
						fmt.Printf("[APIServer] Encode error: %v\n", err)
						return
					}

					ctx.Write(respBytes)
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[APIServer] Client disconnected: %s\n", ctx.GetID())
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("API Server started on " + address)
	fmt.Println("Actions: query_user, create_order, update_profile, list_items")
	select {}
}
