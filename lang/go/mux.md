### mux

- 标准库路由分组
```go
package main

import "net/http"

func main() {
	mux := http.NewServeMux()

	mux1 := http.NewServeMux()
	mux1.HandleFunc("GET /test", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("mux1 test\n"))
	})
	mux1.HandleFunc("POST /hello", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("mux1 hello\n"))
	})

	mux2 := http.NewServeMux()
	mux2.HandleFunc("GET /test", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("mux2 test\n"))
	})
	mux2.HandleFunc("POST /hello", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("mux2 hello\n"))
	})

	mux.Handle("/mux1/", http.StripPrefix("/mux1", mux1))
	mux.Handle("/mux2/", http.StripPrefix("/mux2", mux2))
	http.ListenAndServe(":8010", mux)
}
```