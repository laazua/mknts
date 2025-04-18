package main

import (
	"context"
	"fmt"
	"gweb/pkg/route"
	"gweb/pkg/utils"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func main() {
	// 加载配置
	utils.LoadCon("app1")
	// 加载mysql
	utils.LoadSql()

	quit := make(chan os.Signal, 1)
	appServe := http.Server{
		Addr:         fmt.Sprintf("%s:%d", utils.Setting.App.Ip, utils.Setting.App.Port),
		ReadTimeout:  time.Second * utils.Setting.App.ReadTimeout,
		WriteTimeout: time.Second * utils.Setting.App.WriteTimeout,
		Handler:      route.GetRoute(),
	}
	go func() {
		if err := appServe.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			panic(err)
		}
	}()
	// 注册信号
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit

	ctx, channel := context.WithTimeout(context.Background(), time.Microsecond*10)
	defer channel()
	if err := appServe.Shutdown(ctx); err != nil {
		panic(err)
	}
}
