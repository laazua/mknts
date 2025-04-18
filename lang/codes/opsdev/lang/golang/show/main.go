package main

import (
	"fmt"
	"log/slog"
	"net/http"
)

func main() {
	// 分组路由muxV1
	muxV1 := http.NewServeMux()
	muxV1.HandleFunc("GET /hello/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Fprintln(w, "GET Hello v1", id)
	})
	muxV1.HandleFunc("POST /hello/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Fprintln(w, "POST Hello v1", id)
	})
	// 分组路由muxV2
	muxV2 := http.NewServeMux()
	muxV2.HandleFunc("GET /hello/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Fprintln(w, "GET Hello v2", id)
	})
	muxV2.HandleFunc("POST /hello/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := r.PathValue("id")
		fmt.Fprintln(w, "POST Hello v2", id)
	})

	muxV3 := http.NewServeMux()
	muxV3.HandleFunc("GET /?page=1&size=10", func(w http.ResponseWriter, r *http.Request) {
		page := r.URL.Query().Get("page")
		size := r.URL.Query().Get("size")
		fmt.Fprintln(w, "GET Hello v3", page, size)
	})

	// 主路由mux
	mux := http.NewServeMux()
	// 将分组路由挂载到主路由
	mux.Handle("/v1/", http.StripPrefix("/v1", muxV1))
	mux.Handle("/v2/", http.StripPrefix("/v2", muxV2))
	mux.Handle("/v3/", http.StripPrefix("/v3", muxV3))

	slog.Info("start server", slog.String("addr", ":8089"))
	http.ListenAndServe(":8089", mux)
}
