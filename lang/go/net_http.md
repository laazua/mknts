### net/http

- 示例
```go
package main

import (
	"fmt"
	"log/slog"
	"net/http"
)

func main() {
	r := http.NewServeMux()
	handler := func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Println(id)
		w.Write(fmt.Appendf(nil, "hello ID: %v\n", id))
	}

	handler = applyMw(handler, mwAuth, mwLogger)

	r.HandleFunc("GET /api/{id}", handler)

	slog.Info("start ...")
	http.ListenAndServe(":7788", r)
}

// mwAuth 中间件
func mwAuth(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Auth Request ...")
		next.ServeHTTP(w, r)
		fmt.Println("Auth Response ...")
	}
}

func mwLogger(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Logger Request ...")
		next.ServeHTTP(w, r)
		fmt.Println("Logger Response ...")
	}
}

type middleWare func(next http.HandlerFunc) http.HandlerFunc

// applyMw 应用中间件
func applyMw(handler http.HandlerFunc, mws ...middleWare) http.HandlerFunc {
	// 从最内层的处理器开始
	hd := handler
	// 从最后一个中间件开始向前应用（保持执行顺序）
	for i := len(mws) - 1; i >= 0; i-- {
		hd = mws[i](hd)
	}

	return hd
}

```
