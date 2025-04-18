package main

import (
	"context"
	"fmt"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"gookins/core"
	"gookins/docs"

	"github.com/gin-contrib/static"
	"github.com/gin-gonic/gin"
	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// //go:embed statics
// var staticFiles embed.FS

// @title gookins web api
// @version 1.0
// @description gookins server web api.
// @termsOfService http://192.168.165.88:8084/terms/

// @contact.name API Support
// @contact.url http://192.168.165.88:8084/support
// @contact.email 1323212038@qq.com

// @license.name Apache 2.0
// @license.url http://www.apache.org/licenses/LICENSE-2.0.html

// @host 192.168.165.88:8084
// @BasePath /
// @securityDefinitions.apikey ApiKeyAuth
// @in header
// @name Authorization
func main() {
	router := newRouter()
	router.Use(static.Serve("/", static.LocalFile("statics", true)))
	docs.SwaggerInfo.BasePath = "/"
	router.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	server := http.Server{
		Addr:    core.Config.Address,
		Handler: router,
	}
	router.NoRoute(func(ctx *gin.Context) {
		fmt.Printf("%s doesn't exists, redirect on /\n", ctx.Request.URL.Path)
		// c.Redirect(http.StatusMovedPermanently, "/")
		ctx.File("./statics/index.html")
	})
	go func() {
		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			slog.Error(err.Error())
		}
	}()

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt, syscall.SIGTERM)
	<-quit
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if err := server.Shutdown(ctx); err != nil {
		slog.Error(err.Error())
	} else {
		slog.Info("服务关闭成功")
	}

}
