package main

import (
	"log/slog"
	"net/http"
)

func main() {
	http.HandleFunc("/test", test)
	println("App Start On: [0.0.0.0:9999]")
	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		panic(err)
	}
}

func test(w http.ResponseWriter, r *http.Request) {
	slog.Info("hanle request")
	w.Write([]byte("this is a test"))
}
