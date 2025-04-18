package api

import (
	"github.com/gin-gonic/gin"
)

func NewMaster() *gin.Engine {
	router := gin.New()

	user := newApiUser()
	router.POST("/login", user.login)
	userGroup := router.Group("/user")
	{
		userGroup.POST("/add", user.add)
		userGroup.DELETE("/delete", user.delete)
		userGroup.PUT("/modify", user.modify)
		userGroup.GET("/query", user.query)
		userGroup.PUT("/logout", user.logout)
	}

	role := newApiRole()
	roleGroup := router.Group("/role")
	{
		roleGroup.POST("/add", role.add)
		roleGroup.DELETE("/delete", role.delete)
		roleGroup.PUT("/modify", role.modify)
		roleGroup.GET("/query", role.query)
	}

	perm := newApiPerm()
	permGroup := router.Group("/perm")
	{
		permGroup.POST("/add", perm.add)
		permGroup.DELETE("/delete", perm.delete)
		permGroup.PUT("/modify", perm.modify)
		permGroup.GET("/query", perm.query)
	}

	work := newApiWork()
	workGroup := router.Group("/work")
	{
		workGroup.POST("/test", work.test)
	}

	return router
}
