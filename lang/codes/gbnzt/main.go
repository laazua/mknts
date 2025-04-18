package main

import (
	"bnzt/global"
	"bnzt/router"
	"context"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func main() {
	quit := make(chan os.Signal, 1)
	appServe := http.Server{
		Addr:    global.AppCon.GetString("app.addr"),
		Handler: router.GetRoute(),
	}

	// 协程启动服务
	go func() {
		if err := appServe.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			panic(err)
		}
	}()

	// 注册信号
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	// 监听程序关闭信号(阻塞状态)
	<-quit

	// 创建一个超时时间为10秒的上下文信号
	ctx, channel := context.WithTimeout(context.Background(), time.Second*10)
	defer channel()

	// 关闭服务
	if err := appServe.Shutdown(ctx); err != nil {
		panic(err)
	}
}
