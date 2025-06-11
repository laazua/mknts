package middleware

import (
	"fmt"
	"time"

	"sksrv/pkg/comm"
	"sksrv/pkg/handler"
	"sksrv/pkg/server"
)

// AuthMiddleware 认证中间件
func AuthMiddleware(tokens []string) server.Middleware {
	return func(next server.Handler) server.Handler {
		return handler.NewAuthHandler(tokens, next)
	}
}

// HeartbeatMiddleware 心跳中间件
func HeartbeatMiddleware() server.Middleware {
	return func(next server.Handler) server.Handler {
		return handler.NewHeartbeatHandler(next)
	}
}

// LoggingMiddleware 日志中间件
func LoggingMiddleware() server.Middleware {
	return func(next server.Handler) server.Handler {
		return server.HandlerFunc(func(conn *server.Conn, msg *comm.Message) error {
			start := time.Now()

			// 记录接收到的消息
			fmt.Printf("[%s] Received message - Type: %d, Length: %d\n",
				conn.GetRemoteAddress(), msg.Type, msg.Length)

			// 调用下一个处理器
			err := next.Handle(conn, msg)

			// 记录处理结果和耗时
			duration := time.Since(start)
			if err != nil {
				fmt.Printf("[%s] Message processing failed - Error: %v, Duration: %v\n",
					conn.GetRemoteAddress(), err, duration)
			} else {
				fmt.Printf("[%s] Message processed successfully - Duration: %v\n",
					conn.GetRemoteAddress(), duration)
			}

			return err
		})
	}
}
