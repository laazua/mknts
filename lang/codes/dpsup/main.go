package main

import (
	"flag"
	"log/slog"
	"net/http"
)

var config string
var logfile string

func main() {
	flag.StringVar(&config, "config", "./.env", "服务启动配置: /path/.env")
	flag.StringVar(&logfile, "logfile", "/var/log/dpsup.log", "服务日志文件: /path/dpsup.log")
	flag.Parse()

	NewLogger()
	LoadEnv(config)

	api := &Api{dp: new(Dp)}
	mux := http.NewServeMux()
	mux.HandleFunc("POST /api/create", api.Create)
	mux.HandleFunc("DELETE /api/delete", api.Delete)

	address := GetOsEnv("address")
	server := http.Server{
		Handler: mux,
		Addr:    address,
	}
	logger.Info("Server start", slog.String("address", address))
	if err := server.ListenAndServe(); err != nil {
		panic(err)
	}
}
