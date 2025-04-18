package app

import (
	"context"
	"fmt"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"stdhttp/pkg/controller"
	"stdhttp/pkg/middleware"
	"stdhttp/pkg/router"
)

type App struct {
	router      *router.Router
	logger      *slog.Logger
	controllers []controller.Controller
}

func NewApp() *App {
	var opsLog *slog.HandlerOptions
	switch os.Getenv("app.log.level") {
	case "debug":
		opsLog = &slog.HandlerOptions{Level: slog.LevelDebug}
	case "warn":
		opsLog = &slog.HandlerOptions{Level: slog.LevelWarn}
	case "error":
		opsLog = &slog.HandlerOptions{Level: slog.LevelError}
	default:
		opsLog = &slog.HandlerOptions{Level: slog.LevelInfo}
	}
	logger := slog.New(slog.NewTextHandler(os.Stdout, opsLog))
	return &App{
		router: router.NewRouter(),
		logger: logger,
		controllers: []controller.Controller{
			&controller.Auth{Logger: logger},
			&controller.Blog{Logger: logger},
		},
	}
}

func (a *App) Run() error {
	// 使用中间件
	//a.router.Use()

	a.initController()

	address := os.Getenv("app.address")
	a.logger.Info(fmt.Sprintf("app run [%v]", address))
	server := http.Server{
		Addr:    address,
		Handler: a.router.Mux,
	}

	go func() {
		if err := server.ListenAndServe(); err != http.ErrServerClosed {
			a.logger.Error("start server error")
		}
	}()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)

	ctx, cancel := context.WithTimeout(
		context.Background(),
		time.Duration(10)*time.Second)

	defer cancel()

	<-sig
	a.logger.Info("Receive shutdown signal")

	return server.Shutdown(ctx)
}

func (a *App) initController() {
	root := a.router.Group("/api/")
	// 全局middleware
        root.Use(middleware.CorsMw)
	for _, controller := range a.controllers {
		a.logger.Info(fmt.Sprintf("Init Controller: %v", controller.Name()))
		api := a.router.Group(root.Prefix + controller.Name())
		controller.InitRoute(api)
	}
}
