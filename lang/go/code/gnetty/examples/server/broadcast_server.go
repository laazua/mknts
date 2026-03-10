package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"gnetty/bootstrap"
	"gnetty/channel"
	"gnetty/handler"
)

// 广播服务器示例（聊天室）
// 启动：go run examples/server/broadcast_server.go
// 测试：开多个客户端连接到 localhost:9001
func broadcastMain(address string) {
	server := bootstrap.NewServerBootstrap()

	server.SetHandler(func(ch *channel.Channel) {
		h := handler.NewSimpleInboundHandler().
			OnActive(func(ctx channel.ChannelContext) {
				id := ctx.Channel().GetID()
				fmt.Printf("[Broadcast] User joined: %s\n", id)

				// 获取用户名
				ctx.Channel().SetAttr("username", "User-"+id)

				// 通知其他用户
				msg := fmt.Sprintf("[System] %s joined\n", id)
				server.BroadCast([]byte(msg))
			}).
			OnRead(func(ctx channel.ChannelContext, msg interface{}) {
				if data, ok := msg.([]byte); ok {
					text := strings.TrimSpace(string(data))
					if text == "" {
						return
					}

					username := ctx.Channel().GetAttr("username").(string)
					message := fmt.Sprintf("[%s] %s\n", username, text)

					fmt.Printf("[Broadcast] %s", message)
					server.BroadCast([]byte(message))
				}
			}).
			OnInactive(func(ctx channel.ChannelContext) {
				id := ctx.Channel().GetID()
				fmt.Printf("[Broadcast] User left: %s\n", id)

				msg := fmt.Sprintf("[System] %s left\n", id)
				server.BroadCast([]byte(msg))
			})

		ch.GetPipeline().AddLast(h)
	})

	err := server.Bind(address)
	if err != nil {
		log.Fatalf("Failed to bind: %v\n", err)
	}

	fmt.Println("Broadcast Server (Chat Room) started on " + address)
	fmt.Println("Multiple clients can connect. Type messages to broadcast.")

	// 启动命令行输入线程
	go func() {
		scanner := bufio.NewScanner(os.Stdin)
		for scanner.Scan() {
			cmd := scanner.Text()
			if cmd == "users" {
				conns := server.GetConnections()
				fmt.Printf("Connected users: %d\n", len(conns))
				for id := range conns {
					fmt.Printf("  - %s\n", id)
				}
			} else if cmd == "quit" {
				server.Close()
				os.Exit(0)
			}
		}
	}()

	select {}
}
