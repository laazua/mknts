package main

import (
	"fmt"
	"net/http"
	"time"
)

// 方式一
type HandlerFunc func(w http.ResponseWriter, r *http.Request)

func Logger(f HandlerFunc) HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		now := time.Now()
		f(w, r)
		fmt.Println("Time:", time.Since(now))
	}
}

func Greet(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World! %s", time.Now())
}

func main() {

	mux := http.NewServeMux()

	mux.HandleFunc("/greet", Logger(Greet))
	server := &http.Server{
		Addr:    ":8080",
		Handler: Logging(mux),
	}
	server.ListenAndServe()
}

// 方式二
func Logging(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		now := time.Now()
		next.ServeHTTP(w, r)
		fmt.Println("Time:", time.Since(now))
	})
}
