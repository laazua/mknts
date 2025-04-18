package routers

import (
	"cmsmanager/common"
	"cmsmanager/controller"
	"github.com/gin-gonic/gin"
)

func GetRouters() *gin.Engine {
	r := gin.Default()
	r.POST("/api/auth/register", controller.Register)
	r.POST("/api/auth/login", controller.Login)
	r.GET("/api/auth/info", common.AuthMiddleWare(), controller.Info)

	return r
}