//该实例展示在go中如何创建日志中间件
//中间件只接受http.HanderFunc作为其参数之一,对其进行包装并返回新对http.用于服务器调用对HanderFunc
package main

import (
	"fmt"
	"log"
	"net/http"
)

func logging(f http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		log.Println(r.URL.Path)
		f(w, r)
	}
}

func foo(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "foo")
}

func bar(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "bar")
}

func main() {
	http.HandleFunc("/foo", logging(foo))
	http.HandleFunc("/bar", logging(bar))

	http.ListenAndServe("0.0.0.0:8888", nil)
}

//go run middleware.go
//curl -s http://localhost:8888/bar
//curl -s http://localhost:8888/foo