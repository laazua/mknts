package main

import "net/http"

func main() {
	// 注册函数响应请求
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hello world"))
	})

	/* http */
	// 方式一启动服务
	serve := http.Server{
		Addr:    "0.0.0.0:8888",
		Handler: nil, // DefaultServeMux
	}
	serve.ListenAndServe()

	// 方式二启动服务
	// http.ListenAndServe(":8888", nil)

	/* https */
	// 方式一
	//http.ListenAndServer()
	// 方式二
	// serve.ListenAndServeTLS()
}
