package app

import (
	"context"
	"errors"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"spoved-user/internal/router"
	"spoved-utils/config"
	"spoved-utils/db"
	"spoved-utils/security"
	"spoved-utils/xlog"
)

type App struct {
	Server *http.Server
}

func New() (*App, error) {
	// 初始化日志系统
	xlog.Init()
	// 初始化Redis连接
	if err := db.InitRedis(); err != nil {
		// return nil, errors.New("初始化Redis失败: " + err.Error())
		panic(err)
	}
	xlog.Info("初始化Redis成功 ...")
	// 初始化数据库连接
	if err := db.InitMySQL(); err != nil {
		// return nil, errors.New("初始化数据库失败: " + err.Error())
		panic(err)
	}
	xlog.Info("初始化数据库成功 ...")
	router := router.New()
	// 实例化服务器
	server := &http.Server{
		Handler:      router,
		Addr:         config.Get().SrvAddr(),
		ReadTimeout:  config.Get().Server.ReadTimeout,
		WriteTimeout: config.Get().Server.WriteTimeout,
	}

	return &App{
		Server: server,
	}, nil
}

func (a *App) Run() error {
	quiet := make(chan os.Signal, 1)
	// 监听失败和退出信号
	signal.Notify(quiet, syscall.SIGINT, syscall.SIGTERM, syscall.SIGQUIT)

	// 配置 TLS
	tlsOptions := security.SetupTLS()
	if tlsOptions.UseTLS {
		a.Server.TLSConfig = tlsOptions.TLSConfig
	}
	// 启动服务器
	go func() {
		xlog.Infof("服务器正在监听 addr=%s tls=%t", a.Server.Addr, tlsOptions.UseTLS)
		var err error
		if !tlsOptions.UseTLS {
			err = a.Server.ListenAndServe()
		} else {
			err = a.Server.ListenAndServeTLS("", "")
		}

		if err != nil && !errors.Is(err, http.ErrServerClosed) {
			xlog.Error("启动服务失败", "error", err)
			os.Exit(-2)
		}
	}()
	<-quiet
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	return a.Server.Shutdown(ctx)
}

func (a *App) Shutdown() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if err := a.Server.Shutdown(ctx); err != nil {
		xlog.Error("关闭服务失败", "error", err)
	}
	if err := db.CloseMySQL(); err != nil {
		xlog.Error("关闭数据库连接失败", "error", err)
	}
	if err := db.CloseRedis(); err != nil {
		xlog.Error("关闭Redis连接失败", "error", err)
	}
	xlog.Info("资源清理完成,退出程序")
}
