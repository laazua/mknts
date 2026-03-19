package router

import (
	"spoved-user/internal/api"
	"spoved-utils/config"
	"spoved-utils/middleware"
	"spoved-utils/xlog"

	"github.com/gin-gonic/gin"
)

func New() *gin.Engine {
	xlog.SetLogger(
		xlog.New(),
	)
	gin.SetMode(config.Get().Server.Mode)
	router := gin.New()
	router.Use(
		middleware.Logger(),
		middleware.Recover(),
	)
	if err := registerRoutes(router); err != nil {
		xlog.Error("注册路由失败", "Error", err.Error())
		return nil
	}
	return router
}

// registerRoutes 定义所有的路由和对应的处理函数
func registerRoutes(r *gin.Engine) error {
	// 实例化接口处理器
	authHandler, err := api.NewAuthHandler()
	if err != nil {
		return err
	}
	userHandler, err := api.NewUserHandler()
	if err != nil {
		return err
	}
	roleHandler := api.NewRoleHandler()
	// 设置Gin模式
	gin.SetMode(config.Get().Server.Mode)
	// 定义认证组用于登录和登出
	authGroup := r.Group("/api/auth")
	{
		authGroup.POST("/pwd", authHandler.PwdLogin)
		authGroup.POST("/sms", authHandler.SmsLogin)
		authGroup.POST("/email", authHandler.EmailLogin)
		authGroup.POST("/sms/code", authHandler.SendSmsCode)
		authGroup.POST("/logout", authHandler.Logout)
	}
	// 定义用户组用于用户操作
	userGroup := r.Group("/api/users").Use(
		middleware.AuthMiddleware([]byte(config.Get().Server.JwtSecret)),
	)
	{
		userGroup.GET("/:id", userHandler.GetUser)
		userGroup.PUT("/:id", userHandler.UpdateUser)
		userGroup.POST("/", userHandler.CreateUser)
		userGroup.DELETE("/:id", userHandler.DeleteUser)
		userGroup.GET("/", userHandler.ListUsers)
	}
	// 定义角色组用于角色操作
	roleGroup := r.Group("/api/roles").Use(
		middleware.AuthMiddleware([]byte(config.Get().Server.JwtSecret)),
	)
	{
		roleGroup.GET("/:id", roleHandler.GetRole)
		roleGroup.PUT("/:id", roleHandler.UpdateRole)
		roleGroup.POST("/", roleHandler.CreateRole)
		roleGroup.DELETE("/:id", roleHandler.DeleteRole)
		roleGroup.GET("/", roleHandler.ListRoles)
	}
	return nil
}
