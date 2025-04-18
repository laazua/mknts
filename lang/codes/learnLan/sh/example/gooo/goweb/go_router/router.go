//gorilla/mux
//go get github.com/gorilla/mux
package main

/*
import (
	"net/http"
	"github.com/gorilla/mux"
)
//crete a new router
r := mux.NewRouter()

//一旦有了r路由器可以使用r.HandleFunc(...),不需要使用http.HandleFunc(...)

//gorilla/mux路由最大的优势在于能够从请求URL中提取分段,如应用程序中的URL: /books/go-programming-blueprint/page/10
//上面的URL有两个动态的段book title slug (go-programming-blueprint)和page(10)
//要使处理请求程序与上述RUL匹配,则可以使用URL模式中的占位符替换动态分段,如下
r.HandeFunc("/books/{title}/page/{page}", func(w http.ResponseWriter, r *http.Request){
	//get the book
	//navigate to the page
})

//从片段中获取数据,mux.Vars(r), 该函数将http.Request作为参数并返回片段的映射
func (w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	vars["title"]  //the book title slug
	vars["page"]   //the page
}

//设置http server路由
//http.ListenAndServer(":80", nil), nil是net/http默认路由参数,要使用自己的路由参数,则将nil替换成自己的路由器r
http.ListenAndServe(":80", r)
 */

import (
	"fmt"
	"net/http"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/books/{title}/page/{page}", func (w http.ResponseWriter, r*http.Request){
		vars := mux.Vars(r)
		title := vars["title"]
		page := vars["page"]

		fmt.Fprintf(w, "you have requested the book: %s on page %s\n", title, page)
	})

	http.ListenAndServe("0.0.0.0:8888", r)
}

/*
将请求处理程序限定为特定的http方法:
r.HandleFunc("/books/{title}", CreateBook).Method("POST")
r.HandleFunc("/books/{title]", ReadBook).Method("GET")
r.HandleFunc("books/{title}", UpdateBook).Method("PUT")
r.HandleFunc("books/{title}", DeleteBook).Method("DELETE")

将请求处理程序限定为特定的主机域名
r.HandleFunc("/books/{title}", BookHandler).Host("www.hello.com")

将请求处理限定为http或者https
r.HandleFunc("/secure", SecureHandler).Schemes("https")
r.HandleFunc("/insecure", InsecureHandler).Schemes("http")

将请求处理程序限定为特定路径前缀
bookrouter := r.PathPrefix("/books").Subrouter()
bookrouter.HandleFunc("/", AllBooks)
bookrouter.HandleFunc("/{title}", GetBook)
*/