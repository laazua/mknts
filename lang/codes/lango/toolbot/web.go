package main

import (
	"log/slog"
	"net/http"
)

func RunToolBot(addr string) {
	mux := http.NewServeMux()
	server := http.Server{
		Addr:    addr,
		Handler: mux,
	}
	mux.HandleFunc("/webhook", webhook)
	slog.Info("toolbot web run on", slog.String("address", addr))
	if err := server.ListenAndServe(); err != nil {
		panic(err)
	}
}

func webhook(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		return
	}
}
