package routes

import (
	"vanGogh/pkg/caller/utils"
	"vanGogh/pkg/slaver/routes/api"

	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"
)

func GetRoute() *gin.Engine {
	route := gin.New()

	if viper.GetBool("app_debug") {
		gin.SetMode(gin.DebugMode)
	} else {
		gin.SetMode(gin.ReleaseMode)
	}

	route.Use(utils.GlobleMiddleware()...)

	zone := route.Group("/api/zone", utils.WhiteIps())
	{
		zone.POST("/zone", api.SAddZone)
		zone.PUT("/zone", api.SOptZone)
	}

	host := route.Group("/api", utils.WhiteIps())
	{
		host.GET("/host", api.SGetHostInfo)
	}

	return route
}
