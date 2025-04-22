package api

import (
	"gin-vue-admin/utils"

	"github.com/gin-gonic/gin"
)

func NewRoute() *gin.Engine {

	route := gin.Default()

	gin.SetMode(utils.GetEnv("MODE"))

	userApi := new(UserApi)

	route.POST("/login", userApi.Login)
	user := route.Group("/user")
	{
		user.GET("/info", userApi.GetInfo)
	}

	return route
}
