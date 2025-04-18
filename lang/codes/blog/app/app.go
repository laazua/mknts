package app

import (
	"context"
	"net/http"
	"os"
	"os/signal"
	"schema"
	"syscall"
	"time"
	"utils"

	"controller"
	"env"
	"storage"

	"github.com/gin-gonic/gin"
	"github.com/sirupsen/logrus"
)

type App struct {
	engine      *gin.Engine
	logger      *logrus.Logger
	controllers []controller.Controller
}

func New() App {
	engine := gin.New()
	logger := logrus.StandardLogger()
	logger.SetFormatter(&logrus.TextFormatter{FullTimestamp: true})

	// 初始化数据库
	s, err := storage.New()
	if err != nil {
		panic(err)
	}

	return App{
		engine: engine,
		logger: logger,
		controllers: []controller.Controller{
			&controller.User{Logger: logger, StorageUser: storage.NewUser(s)},
			&controller.Role{Logger: logger, StorageRole: storage.NewRole(s)},
			&controller.Blog{Logger: logger, StorageBlog: storage.NewBlog(s)},
			&controller.Auth{Logger: logger, StorageAuth: storage.NewAuth(s), Heper: utils.NewHelper()},
		},
	}
}

func (a *App) Run() error {
	a.engine.Use(gin.Recovery())
	gin.SetMode(os.Getenv("app.runmode"))

	// 注册controller
	a.initRoute()

	address := os.Getenv("app.address")

	// - http服务启动方式
	server := http.Server{
		Addr:         address,
		Handler:      a.engine,
		IdleTimeout:  5,
		ReadTimeout:  5,
		WriteTimeout: 5,
	}
	a.logger.Printf("Blog start on [%v]", address)
	go func() {
		if err := server.ListenAndServe(); err != http.ErrServerClosed {
			a.logger.Fatalf("Failed to start server, %v", err)
		}
	}()

	// - https服务启动方式1
	// 加载证书
	// cert, err := tls.LoadX509KeyPair("server.crt", "server.key")
	// if err != nil {
	// 	a.logger.Errorf("Load cert file error: %v", err)
	// 	return err
	// }
	// // 配置 TLS
	// tlsConfig := &tls.Config{
	// 	Certificates: []tls.Certificate{cert},
	// 	MinVersion:   tls.VersionTLS13, // 强制使用 TLS 1.3
	// 	MaxVersion:   tls.VersionTLS13, // 强制使用 TLS 1.3
	// }

	// tlsServ := http.Server{
	// 	Addr:      address,
	// 	Handler:   a.engine,
	// 	TLSConfig: tlsConfig,
	// }
	// go func() {
	// 	if err := tlsServ.ListenAndServe(); err != http.ErrServerClosed {
	// 		a.logger.Fatalf("Faild to start server, %v", err)
	// 	}
	// }()

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)

	ctx, cancel := context.WithTimeout(
		context.Background(),
		time.Duration(env.Atoint(os.Getenv("app.shutsmooth")))*time.Second)

	defer cancel()

	ch := <-sig
	a.logger.Infof("Receive signal: %s", ch)

	return server.Shutdown(ctx)
}

func (a *App) initRoute() {
	root := a.engine
	// 初始化项目
	root.POST("/api/init", func(ctx *gin.Context) {
		// 写入管理员信息
		admin := schema.User{}
		if err := ctx.ShouldBind(admin); err != nil {
			a.logger.Fatalf("init admin user error: %v", err)
			ctx.JSON(400, gin.H{"code": 400, "message": "init admin user error"})
			return
		}
		ctx.JSON(200, gin.H{"code": 200, "message": "init admin user success"})
	})

	api := root.Group("/api")
	for _, controller := range a.controllers {
		a.logger.Infof("init route: %v", controller.ApiName())
		controller.ApiInit(api)
	}
}
