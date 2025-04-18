package router

import (
	"sunflower/controller"
	"sunflower/middleware"

	"github.com/gin-gonic/gin"
)

func SetupRouter() *gin.Engine {
	
	r := gin.Default()
	r.Use(middleware.CORSMiddleware(), middleware.RecoverMiddleware())

	api := r.Group("v1")
	{
		api.POST("/user/register", controller.Register)
		api.POST("/user/login", controller.Login)
		api.GET("/user/info", middleware.AuthMiddleware(), controller.Info)
	}

	return r
}