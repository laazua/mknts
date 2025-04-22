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

	"msite/pkg/controller"
	"msite/pkg/middleware"
	"msite/pkg/router"
	"msite/pkg/storage"
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
			&controller.User{Logger: logger, Storage: &storage.User{}},
			&controller.Blog{Logger: logger},
		},
	}
}

func (a *App) Run() error {

	// 注册路由
	a.initController()

	address := os.Getenv("app.address")
	a.logger.Info(fmt.Sprintf("App Run [%v]", address))
	server := http.Server{
		Addr:    address,
		Handler: a.router.Mux,
	}

	go func() {
		if err := server.ListenAndServe(); err != http.ErrServerClosed {
			a.logger.Error(fmt.Sprintf("start server error: %v", err.Error()))
		}
	}()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM, syscall.SIGABRT, syscall.SIGINT, syscall.SIGQUIT)

	ctx, cancel := context.WithTimeout(
		context.Background(),
		time.Duration(10)*time.Second)

	defer cancel()

	a.logger.Info(fmt.Sprintf("Receive shutdown signal: %v", <-sig))

	return server.Shutdown(ctx)
}

func (a *App) initController() {
	// 根路由组
	api := a.router.Group("/api")
	// 全局中间件
	api.Use(middleware.Cors)
	api.Use(middleware.Logger)
	for _, controller := range a.controllers {
		a.logger.Info(fmt.Sprintf("Register controller: %v", controller.Name()))
		controller.InitRoute(api)
	}
}
