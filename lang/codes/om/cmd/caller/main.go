package main

import (
	"context"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
	"vanGogh/pkg/caller/routes"
	"vanGogh/pkg/caller/utils"

	"github.com/spf13/viper"
)

func init() {
	utils.InitConfig("caller")
	utils.InitMongodb()
}

func main() {
	appServe := http.Server{
		Addr:         viper.GetString("app_url"),
		Handler:      routes.GetRoute(),
		ReadTimeout:  viper.GetDuration("app_read_timeout") * time.Second,
		WriteTimeout: viper.GetDuration("app_write_timeout") * time.Second,
	}
	quit := make(chan os.Signal, 1)
	go func() {
		if err := appServe.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			panic(err)
		}
	}()
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	ctx, channel := context.WithTimeout(context.Background(), time.Second*10)
	defer channel()
	if err := appServe.Shutdown(ctx); err != nil {
		panic(err)
	}
}
