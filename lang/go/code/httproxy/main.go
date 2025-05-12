package main

import (
	"net/http"
	"net/http/httputil"
	"net/url"
	"log"
)

func main() {
	// 创建一个新的 HTTP 代理
	proxy := httputil.NewSingleHostReverseProxy(&url.URL{
		Scheme: "http",
		Host:   "bullshit.dyvn6.net", // 你可以将此处替换为任何目标服务器
	})

	// 定义处理请求的函数
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// 将请求转发到目标服务器
		proxy.ServeHTTP(w, r)
	})

	// 启动代理服务器
	log.Println("Starting proxy server on :8081")
	if err := http.ListenAndServe(":8081", nil); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
