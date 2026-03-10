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

// 防粘包客户端示例
// 启动：go run examples/client/frame_client.go
func frameMain(address string) {
	client := bootstrap.NewClientBootstrap()

	encoder := codec.NewLengthFieldEncoder(4)

	client.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Println("[FrameClient] Connected to server")

				// 发送多个消息，测试粘包处理
				messages := []string{
					"Message 1",
					"Message 2",
					"Message 3",
					"Message 4",
					"Message 5",
				}

				for _, msg := range messages {
					encoded, _ := encoder.Encode(msg)
					fmt.Printf("[FrameClient] Sending: %s (size=%d)\n", msg, len(encoded))
					ctx.Channel().Write(encoded)
					time.Sleep(200 * time.Millisecond)
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Println("[FrameClient] Disconnected")
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[FrameClient] Received: %s\n", string(data))
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := client.Connect(address)
	if err != nil {
		log.Fatalf("Failed to connect: %v\n", err)
	}

	time.Sleep(10 * time.Second)
	client.Close()
}
