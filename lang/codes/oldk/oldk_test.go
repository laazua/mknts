package oldk

import "testing"

// import (
// 	"fmt"
// 	"net/http"
// )

// func helloHandler(w http.ResponseWriter, r *http.Request) {
// 	// for k, v := range r.Header {
// 	// 	fmt.Println(k, v)
// 	// }
// 	fmt.Println(r.Header["Origin"])
// }

// func main() {
// 	http.HandleFunc("/", helloHandler)

// 	// 第二个参数是http请求的入口,这里使用http包默认的实例处理
// 	// 该实例实现了http.handler接口
// 	// http.ListenAndServe(":8080", nil)

// 	engine := new(Engine)
// 	http.ListenAndServe(":8080", engine)
// }

func TestOldk(t *testing.T) {
	o := oldk.New()
	o.Get("/", func(c *Context) {
		c.Data(200, []byte("aaaa"))
	})
	if err := o.Run(":8080"); err != nil {
		panic(err)
	}
}
