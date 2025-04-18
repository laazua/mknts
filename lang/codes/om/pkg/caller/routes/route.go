package routes

import (
	"vanGogh/pkg/caller/routes/api"
	"vanGogh/pkg/caller/utils"

	"github.com/spf13/viper"

	"github.com/gin-gonic/gin"
)

func GetRoute() *gin.Engine {
	route := gin.New()

	// set app run mode
	if viper.GetBool("app_debug") {
		gin.SetMode(gin.DebugMode)
	} else {
		gin.SetMode(gin.ReleaseMode)
	}

	// add global middleware
	route.Use(utils.GlobleMiddleware()...)

	// mount user api
	user := route.Group("/api", utils.WhiteIps())
	{
		user.POST("/sign", api.CUserSign, utils.JwtAuth())
		user.GET("/chek", api.CUserInfo)
		user.POST("/user", api.CAddUser)
		user.PUT("/user", api.CPutUser)
		user.GET("/user", api.CGetUser)
	}

	// mount zone api
	zone := route.Group("/api")
	{
		zone.GET("/zone", api.CGetZone)
		zone.PUT("/zone", api.CPutZone)
	}

	// mount host api
	host := route.Group("/api")
	{
		host.GET("/host", api.CGetHostInfo)
	}

	return route
}
