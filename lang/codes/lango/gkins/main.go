package main

import (
	"context"
	"embed"
	"io/fs"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"gkins/env"
	"gkins/store"
	"gkins/utils"
	"gkins/views"
)

//go:embed views/static/*
var staticFS embed.FS

func main() {
	// 实例化ServeMux
	mux := http.NewServeMux()
	address := os.Getenv("app.address")
	server := http.Server{
		Addr:    address,
		Handler: utils.CorsMiddleware(mux),
	}
	// 加载静态文件[开发模式]
	//mux.Handle("/static/", http.StripPrefix("/static", http.FileServer(http.Dir("./views/static"))))
	// 加载静态资源[打包成一个文件]
	//mux.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.FS(staticFS))))
	staticSubFS, err := fs.Sub(staticFS, "views/static")
	if err != nil {
		slog.Error(err.Error())
		return
	}
	mux.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.FS(staticSubFS))))

	// 用户相关路由处理
	mux.HandleFunc("/", views.Login)
	mux.HandleFunc("/api/user/create", utils.AuthMiddleware(views.CreateUser))
	mux.HandleFunc("/api/user/delete", utils.AuthMiddleware(views.DeleteUser))
	mux.HandleFunc("/api/user/update", utils.AuthMiddleware(views.UpdateUser))
	mux.HandleFunc("/api/user/query", utils.AuthMiddleware(views.QueryUser))
	mux.HandleFunc("/api/user/list", utils.AuthMiddleware(views.UserList))
	// 任务相关路由处理
	mux.HandleFunc("/dashboard", utils.AuthMiddleware(views.Dashboard))
	mux.HandleFunc("/api/task/create", utils.AuthMiddleware(views.CreateTask))
	mux.HandleFunc("/api/task/delete", utils.AuthMiddleware(views.DeleteTask))
	mux.HandleFunc("/api/task/update", utils.AuthMiddleware(views.UpdateTask))
	mux.HandleFunc("/api/task/query", utils.AuthMiddleware(views.QueryTask))
	mux.HandleFunc("/api/task/list", utils.AuthMiddleware(views.TaskList))
	mux.HandleFunc("/api/task/manual", utils.AuthMiddleware(views.ManualRunTask))
	mux.HandleFunc("/api/task/webhook", utils.AuthMiddleware(views.WebhookRunTask))
	// 启动ServeMux实例
	slog.Info("Server Run At", slog.String("address", address))
	go func() {
		if err := server.ListenAndServe(); err != nil {
			_ = store.DB.Close()
			slog.Error(err.Error())
		}
	}()
	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(env.ParseTDuration(os.Getenv("app.shutsmooth"))))
	defer cancel()
	<-sig
	slog.Info("Receive shutdown signal")
	_ = store.DB.Close()
	_ = server.Shutdown(ctx)
}
