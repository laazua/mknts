package middleware

import (
	"net/http"
)

func AuthMw(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// 获取token
		token := r.Header.Get("Authorization")
		if token == "" {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}
		// 调用下一个中间件或处理程序
		next.ServeHTTP(w, r)
	})
}

// 跨域中间件
func CorsMw(next http.Handler) http.Handler {
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

