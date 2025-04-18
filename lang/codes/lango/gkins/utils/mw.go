package utils

import (
	"context"
	"log/slog"
	"net/http"
	"path/filepath"
)

// AuthMiddleware 认证中间件
func AuthMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		cookie, err := r.Cookie("token")
		if err != nil {
			http.Redirect(w, r, "/", http.StatusUnauthorized)
			return
		}
		token := cookie.Value
		email, err := ParseToken(token)
		if err != nil {
			slog.Error(err.Error())
			http.Redirect(w, r, "/", http.StatusUnauthorized)
			return
		}
		// 将用户名加入上下文
		ctx := r.Context()
		ctx = context.WithValue(ctx, "username", email)
		r = r.WithContext(ctx)

		next(w, r)
	}
}

// CorsMiddleware 设置 CORS 和 MIME 类型
func CorsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// 设置 CORS 头
		w.Header().Set("Access-Control-Allow-Origin", "*")
		// 处理静态文件的 MIME 类型
		filePath := r.URL.Path
		// 通过文件扩展名设置正确的 MIME 类型
		switch filepath.Ext(filePath) {
		case ".css":
			w.Header().Set("Content-Type", "text/css")
		case ".js":
			w.Header().Set("Content-Type", "application/javascript")
		case ".html":
			w.Header().Set("Content-Type", "text/html")
		}
		// 调用下一个处理器
		next.ServeHTTP(w, r)
	})
}
