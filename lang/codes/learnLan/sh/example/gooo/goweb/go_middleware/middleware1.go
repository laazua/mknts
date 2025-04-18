//该示例将展示如何在go中创建更高级的中间件
//在这里定义一种新型的中间件,它使得多个中间件连接在一起变得更加容易
package main

import(
	"fmt"
	"log"
	"net/http"
	"time"
)

type Middleware func(handlerFunc http.HandlerFunc) http.HandlerFunc

//logging logs all request with its path and the time it took to process
func Logging() Middleware {
	//create a new middleware
	return func(f http.HandlerFunc) http.HandlerFunc {
		//define the http.HandlerFunc
		return func(w http.ResponseWriter, r *http.Request) {
			//do middleware thing
			start := time.Now()
			defer func() {log.Println(r.URL.Path, time.Since(start))}()
			//call the next middleware/hander in chain
			f(w, r)
		}
	}
}

//method ensures that url can only be requested with a specific method, else returns a 400 bad request
func Method(m string) Middleware {
	//create a new middleware
	return func(f http.HandlerFunc) http.HandlerFunc {
		//define the http.HandlerFunc
		return func(w http.ResponseWriter, r *http.Request) {
			//do middleware thing
			if r.Method != m {
				http.Error(w, http.StatusText(http.StatusBadRequest), http.StatusBadRequest)
				return
			}
			//call the next middleware/handler in chain
			f(w, r)
		}
	}
}

//Chain applies middlewares to a http.HandlerFunc
func Chain(f http.HandlerFunc, middlewares ...Middleware) http.HandlerFunc {
	for _, m := range middlewares {
		f = m(f)
	}
	return f
}

func Hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "hello world")
}

func main() {
	http.HandleFunc("/", Chain(Hello, Method("GET"), Logging()))
	http.ListenAndServe("0.0.0.0:8888", nil)
}