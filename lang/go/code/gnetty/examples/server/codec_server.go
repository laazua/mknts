package main

import (
	"fmt"
	"log"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/codec"
	"gnetty/handler"
)

// 编码解码器示例
// 启动：go run examples/server/codec_server.go
func codecMain(address string) {
	server := bootstrap.NewServerBootstrap()

	// 创建长度前缀解码器
	decoder := codec.NewLengthFieldDecoder(4)
	encoder := codec.NewLengthFieldEncoder(4)

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				fmt.Printf("[Codec] Connection: %s\n", ctx.Channel().GetID())
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					// 解码
					decoded, err := decoder.Decode(data)
					if err != nil {
						fmt.Printf("[Codec] Decode error: %v\n", err)
						return
					}

					if decodedData, ok := decoded.([]byte); ok {
						fmt.Printf("[Codec] Received: %s\n", string(decodedData))

						// 编码并回复
						response := fmt.Sprintf("Echo: %s", string(decodedData))
						encoded, err := encoder.Encode(response)
						if err != nil {
							fmt.Printf("[Codec] Encode error: %v\n", err)
							return
						}

						ctx.Channel().Write(encoded)
					}
				}
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Codec Example Server started on " + address)
	select {}
}
