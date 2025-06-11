package main

import (
	"fmt"

	"sksrv/pkg/codec"
	"sksrv/pkg/handler"
	"sksrv/pkg/middleware"
	"sksrv/pkg/server"
)

func main() {
	// 创建服务器
	server := server.NewServer(":8886", &codec.JsonCodec{})

	// 添加中间件
	server.Use(middleware.HeartbeatMiddleware())
	server.Use(middleware.AuthMiddleware([]string{"xxxaaa", "aaaxxx"}))
	server.Use(middleware.LoggingMiddleware())

	// 设置处理器
	server.SetHandler(handler.NewEchoHandler())

	// 启动服务器
	if err := server.Start(); err != nil {
		fmt.Printf("Failed to start server: %v\n", err)
		return
	}

	// 等待退出信号
	fmt.Println("Press Enter to stop the server...")
	fmt.Scanln()

	// 停止服务器
	server.Stop()
}
