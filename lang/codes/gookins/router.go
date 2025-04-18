package main

import (
	"gookins/api"
	"gookins/core"

	"github.com/gin-gonic/gin"
)

func newRouter() *gin.Engine {
	router := gin.New()

	router.Use(gin.Logger(), gin.Recovery(), core.CorMiddleware())

	router.POST("/login", api.UserSign)
	userGroup := router.Group("/user", core.AuthMiddleware())
	{
		userGroup.POST("/add", api.CreateUser)
		userGroup.DELETE("/del/:id", api.DeleteUser)
		userGroup.PUT("/upt", api.UpdateUser)
		userGroup.GET("/list", api.UserLists)
	}
	taskGroup := router.Group("/task", core.AuthMiddleware())
	{
		taskGroup.POST("/add", api.CreateTask)
		taskGroup.DELETE("/del/:id", api.DeleteTask)
		taskGroup.PUT("/upt", api.UpdateTask)
		taskGroup.GET("/list", api.TaskLists)
		taskGroup.POST("/run", api.RunTask)
		taskGroup.POST("/cancel/:name", api.CancelTask)
		taskGroup.GET("/state/:name", api.TaskStatus)
		taskGroup.POST("/disable/:name", api.TaskDisabled)
	}

	return router
}
