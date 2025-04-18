package router

import (
	"v2man/pkg/api"
	"v2man/pkg/config"
	"v2man/pkg/utils"
	"v2man/storage"
	"v2man/storage/service"

	"github.com/gin-gonic/gin"
)

func NewRouter(cfg *config.Config, db *storage.DbHandler) *gin.Engine {

	helper := utils.NewHelpers(cfg)
	userService := service.NewUserService(db, helper)
	userApi := api.NewUserApi(userService)

	router := gin.New()
	gin.SetMode(cfg.RunMode)
	router.Use(gin.Recovery())

	// user api handler
	router.POST("/user/login", userApi.Login)
	userGroup := router.Group("/user")
	{
		userGroup.PUT("/add", userApi.Add)
		userGroup.DELETE("/delete", userApi.Delete)
		userGroup.POST("/update/:name", userApi.Update)
		userGroup.GET("/query", userApi.Query)
	}

	return router
}
