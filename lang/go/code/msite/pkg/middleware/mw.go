package middleware

import (
	"context"
	"fmt"
	"log/slog"
	"msite/pkg/utils"
	"net/http"
)

// 认证中间件
func Auth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// 获取token
		token := r.Header.Get("Authorization")
		if token == "" {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}
		_, err := utils.ParseToken(token)
		if err != nil {
			http.Error(w, "TokenParseErr", http.StatusUnauthorized)
			return
		}
		// 调用下一个中间件或处理程序
		next.ServeHTTP(w, r)
	})
}

// 跨域中间件
func Cors(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		r.Header.Set("Access-Control-Allow-Origin", "*")
		r.Header.Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
		r.Header.Set("Access-Control-Allow-Headers", "Content-Type")
		// 如果是OPTIONS请求，直接返回200响应
		if r.Method == http.MethodOptions {
			return
		}
		next.ServeHTTP(w, r)
	})
}

// 记录挨批接口访问日志
func Logger(next http.Handler) http.Handler {
	ctx := context.Background()
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		slog.Log(ctx, slog.LevelInfo, fmt.Sprintf("[%v] %v", r.Method, r.URL))
		next.ServeHTTP(w, r)
	})
}
