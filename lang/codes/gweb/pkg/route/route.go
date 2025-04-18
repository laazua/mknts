package route

import (
	"gweb/pkg/route/api"
	"gweb/pkg/utils"

	"github.com/gin-gonic/gin"
)

func GetRoute() *gin.Engine {
	r := gin.Default()
	gin.SetMode(utils.Setting.App.RunMode)

	// 使用全局中间件
	r.Use(utils.Cors())

	// 用户接口路由
	userApi := api.NewUserApi()
	user := r.Group("/user/api")
	{
		user.POST("/login", userApi.Login)
		user.Use(utils.JwtAuth())
		user.POST("/user", userApi.Add)
		user.DELETE("/user", userApi.Del)
		user.GET("/user", userApi.Get)
	}

	// 运维接口
	devops := r.Group("/devops/api")
	{
		devops.POST("/host")
	}

	return r
}
