package main

import (
	"encoding/json"
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

// API 客户端示例
// 启动：go run examples/client/api_client.go
func apiMain(address string) {
	client := bootstrap.NewClientBootstrap()

	encoder := codec.NewStructEncoder(4)
	decoder := codec.NewStructDecoder(4)

	client.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[APIClient] Connected to server")

				// 发送一系列请求
				requests := []Request{
					{
						Action: "query_user",
						Params: map[string]interface{}{
							"user_id": 123,
						},
					},
					{
						Action: "create_order",
						Params: map[string]interface{}{
							"items": []string{"item1", "item2"},
							"total": 99.99,
						},
					},
					{
						Action: "list_items",
						Params: map[string]interface{}{
							"page":     1,
							"per_page": 10,
						},
					},
					{
						Action: "update_profile",
						Params: map[string]interface{}{
							"name":  "Bob",
							"email": "bob@example.com",
						},
					},
				}

				// 发送所有请求
				for _, req := range requests {
					data, err := encoder.Encode(req)
					if err != nil {
						fmt.Printf("Encode error: %v\n", err)
						continue
					}

					fmt.Printf("[APIClient] Sending action: %s\n", req.Action)
					ctx.Channel().Write(data)
					time.Sleep(500 * time.Millisecond)
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[APIClient] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码响应
					var resp APIResponse
					err := decoder.DecodeToStruct(data, &resp)
					if err != nil {
						fmt.Printf("[APIClient] Decode error: %v\n", err)
						return
					}

					fmt.Printf("[APIClient] Response: Status=%s, Code=%d, Message=%s\n",
						resp.Status, resp.Code, resp.Message)

					if resp.Data != nil {
						dataJSON, _ := json.MarshalIndent(resp.Data, "", "  ")
						fmt.Printf("[APIClient] Response Data:\n%s\n", string(dataJSON))
					}
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	// 保持连接
	select {}
}
