/*
服务段:
func ListenAndServe(addr string, handler Handler) error  //监听指定tcp网络地址,然后调用服务店程序(handler)处理请求
func ListenAndServeTLS(addr string,certFile string, keyFile string, handler Handler) error 处理https连接请求
*/
package network

import (
	"net/http"
    "time"
)

func main() {
	//func ListenAndServe(addr string, handler Handler) error
	//控制服务端行为,自定义http.Server
	s := &http.Server{
		Addr: ":8888",
		Handler:  myHandler,
		ReadTimeout:  10 * time.Second,
		WriteTimeout:  10* time.Second,
		MaxHeaderBytes: 1 << 20,
	}
}

func myHandler() {
	//...
}