package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 防粘包服务器示例
// 启动：go run examples/server/frame_server.go
// 使用长度前缀协议防止粘包
func frameMain(address string) {
	server := bootstrap.NewFrameServerBootstrap()

	// 设置长度字段帧解码器
	server.SetFrameDecoder(codec.NewLengthFieldFrameDecoder(4, 1024*1024))

	// 创建编码器用于回复
	encoder := codec.NewLengthFieldEncoder(4)

	server.SetHandler(func(ch *channel.FrameChannel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[FrameServer] Client connected: %s\n", ctx.GetID())
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				fmt.Printf("[FrameServer] Client disconnected: %s\n", ctx.GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					fmt.Printf("[FrameServer] Received (size=%d): %s\n", len(data), string(data))

					// 回复
					response := fmt.Sprintf("Echo: %s", string(data))
					encoded, _ := encoder.Encode(response)
					ctx.Write(encoded)
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Frame Server started on " + address)
	fmt.Println("Uses Length-Field protocol to prevent packet sticking")
	select {}
}
