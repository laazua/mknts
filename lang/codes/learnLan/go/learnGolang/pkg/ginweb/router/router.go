package router

import (
	"github.com/gin-gonic/gin"

	"ginweb/controller"
)

func SetupRouter() *gin.Engine {
	router := gin.Default()

	user := router.Group("/user")
	{
		user.POST("/login", controller.Login)
		user.POST("/register", controller.Register)
		user.POST("/deleteUser", controller.DeleteUser)
		user.POST("/changePassword", controller.ChangePassword)
		user.GET("/userInfo", controller.UserInfo)
	}

	return router
}
