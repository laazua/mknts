package main

import(
	"io"
	"log"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	//io包输出字符串比fmt包更节省资源
	io.WriteString(w, "hello, world!")
}

func main() {
	http.HandleFunc("/hello", helloHandler)
	err := http.ListenAndServe("0.0.0.0:8080", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err.Error())
	}
}
