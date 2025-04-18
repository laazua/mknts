//web工作方式:
//            url                        发送请求到ip地址
// 浏览器  ---------> dns服务器(查询ip) -------------------> 建立tcp连接
//            request
// client <------------> server
//            response
//net/http包含所有处理客户端请求的组件
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
		fmt.Fprintf(w, "Welcome to my website!")
	})

	fs := http.FileServer(http.Dir("static/"))
	http.Handle("/static", http.StripPrefix("/static", fs))

	http.ListenAndServe("0.0.0.0:8888", nil)
}

