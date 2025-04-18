package router

import (
	"bnzt/api"
	"bnzt/global"
	"bnzt/middleware"

	_ "bnzt/docs"

	"github.com/gin-gonic/gin"
	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// @bnzt API
// @version 1.0
// @description  bnzt web server.

// @contact.name API Support
// @contact.url http://172.16.9.127:8880/support

// @license.name Apache 2.0
// @license.url http://www.apache.org/licenses/LICENSE-2.0.html

// @host http://172.16.9.127:8880
// @BasePath /
func GetRoute() *gin.Engine {
	route := gin.Default()
	// 模式设置(release|debug)
	gin.SetMode(global.AppCon.GetString("app.mode"))
	// 禁止控制台输出
	// gin.DefaultWriter = ioutil.Discard
	// 获取自定义中间件
	m := middleware.NewMiddleware()
	m.Cors()
	// url := ginSwagger.URL("http://172.16.9.127:8880/swagger/doc.json")
	route.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	// 用户接口路由
	userApi, ok := api.NewApi("user").(api.User)
	if !ok {
		panic("获取用户接口错误")
	}
	user := route.Group("/user/api")
	{
		user.Use(m.IpWhite()) // 绑定中间件
		user.POST("/login", userApi.Login)
		user.Use(m.JwtAuth())                  // 绑定中间件
		user.GET("/users", userApi.Get)        // 用户信息
		user.POST("/users", userApi.Add)       // 添加用户记录
		user.PUT("/users", userApi.Upd)        // 更新用户
		user.DELETE("/users", userApi.Del)     // 删除用户
		user.GET("/userlist", userApi.GetList) // 用户列表
	}
	// 角色接口路由
	roleApi, ok := api.NewApi("role").(api.Role)
	if !ok {
		panic("获取角色接口错误")
	}
	role := route.Group("/role/api", m.IpWhite(), m.JwtAuth())
	{
		// role.Use(m.IpWhite(), m.JwtAuth())     // 绑定中间件
		role.GET("/roles", roleApi.Get)        // 角色信息
		role.POST("/roles", roleApi.Add)       // 添加角色记录
		role.PUT("/roles", roleApi.Upd)        // 更新角色
		role.DELETE("/roles", roleApi.Del)     // 删除角色
		role.GET("/rolelist", roleApi.GetList) // 角色列表
	}
	// 权限接口路由
	permApi, ok := api.NewApi("perm").(api.Perm)
	if !ok {
		panic("获取权限口错误")
	}
	perm := route.Group("/perm/api", m.IpWhite(), m.JwtAuth())
	{
		// perm.Use(m.IpWhite())               // 绑定中间件
		perm.GET("/perms", permApi.Get)        // 权限信息
		perm.POST("/perms", permApi.Add)       // 添加权限记录
		perm.PUT("/perms", permApi.Upd)        // 更新权限
		perm.DELETE("/perms", permApi.Del)     // 删除权限
		perm.GET("/permlist", permApi.GetList) // 权限列表
	}
	// 运营接口路由
	oaApi := api.NewEsOa()
	oa := route.Group("/oa/api", m.IpWhite(), m.JwtAuth())
	{
		oa.POST("/recharank", oaApi.RechaRank) // 充值排行
		oa.POST("/gradedist", oaApi.GradeDist) // 等级分布
		oa.POST("/countdata", oaApi.CountData) // 数据查询
		oa.POST("/rollsdata", oaApi.RollsData) // 滚服数据
		oa.POST("/retendata", oaApi.RetenData) // 留存数据
		oa.POST("/vipsdata", oaApi.VipsData)   // VIP等级
		oa.POST("/ltvsdata", oaApi.LtvsData)   // LTV数据
	}
	// 玩家接口路由
	playerApi := api.NewPlayer()
	player := route.Group("/player/api", m.IpWhite(), m.JwtAuth())
	{
		player.POST("/orderdata", playerApi.OrderData) // 订单查询
		player.POST("/roledata", playerApi.RoleData)   // 角色查询
		player.POST("/currdata", playerApi.CurrData)   // 货币查询
	}
	// 运维接口路由
	devopsApi := api.NewYwMg()
	devops := route.Group("/zone/api/", m.IpWhite(), m.JwtAuth())
	{
		devops.POST("/zones", devopsApi.Add)    // 添加区服
		devops.POST("/man", devopsApi.Manage)   // 区服管理
		devops.GET("/zones", devopsApi.GetList) // 区服列表
		devops.POST("/host", devopsApi.Host)    // 主机资源
	}

	return route
}
