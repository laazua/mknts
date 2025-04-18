package routers

import (
	api "msbn/controllers"
	"msbn/middleware"

	"github.com/gin-gonic/gin"
)

func GetRouter() *gin.Engine {
	r := gin.Default()
	gin.SetMode(gin.ReleaseMode)
	/* user api */
	user := r.Group("/user/api")
	{
		user.POST("/login", api.Login)
		user.Use(middleware.JwtAuth(), middleware.IpWhite())
		/*用户管理*/
		user.GET("/info", api.GetUserInfo)
		user.GET("/users", api.GetUserList)     // 获取用户列表
		user.POST("/users", api.AddUser)        // 创建用户
		user.PUT("/users", api.UpdateUser)      // 更新用户
		user.DELETE("/users", api.DeleteUser)   // 删除用户
		user.GET("/users/:id", api.GetUserById) // 根据id获取单个用户
		user.PATCH("/users", api.DistributeRoleForUser)
	}

	/* role api */
	role := r.Group("/role/api")
	{
		role.Use(middleware.JwtAuth(), middleware.IpWhite())
		role.GET("/roles", api.GetRoleList)       // 获取角色列表
		role.POST("/roles", api.AddRole)          // 创建角色
		role.PUT("/roles/:id", api.UpdateRole)    // 更新角色
		role.DELETE("/roles/:id", api.DeleteRole) // 删除角色
		// role.GET("/roles/:id", api.GetRoleById)                    // 根据id获取单个角色
		role.PATCH("/roles", api.DistributeMenusForRole) // 给角色分配权限
	}

	/* menu api */
	perm := r.Group("/perm/api")
	{
		perm.Use(middleware.JwtAuth(), middleware.IpWhite())
		perm.GET("/perms", api.GetMenusList)       // 获取菜单列表
		perm.POST("/perms", api.AddMenus)          // 创建菜单
		perm.PUT("/perms/:id", api.UpdateMenus)    // 更新菜单
		perm.DELETE("/perms/:id", api.DeleteMenus) // 删除菜单
		perm.GET("/perms/:id", api.GetMenusById)   // 根据id获取单个菜单
	}

	/* gm工具api */
	gm := r.Group("/gm/api")
	{
		gm.Use(middleware.JwtAuth(), middleware.IpWhite())
		gm.POST("/zoneaddaward", api.ZoneAddAward)                   // 区服添加奖励
		gm.POST("/announcementquery", api.AnnouncementQuery)         // 公告查询
		gm.POST("/playeraddaward", api.PlayerAddAward)               // 玩家添加奖励
		gm.POST("/firstpageannouncement", api.FirstPageAnnouncement) // 首页公告
		gm.POST("/awardoprecord", api.AwardOpRecord)                 // 发奖操作记录
		gm.POST("/zoneaddannouncement", api.ZoneAddAnnouncement)     // 区服添加公告
	}

	/* oa api */
	oa := r.Group("/oa/api")
	{
		oa.Use(middleware.JwtAuth(), middleware.IpWhite())
		oa.POST("/dataquery", api.DataQuery)                             // 数据查询
		oa.POST("/gradedistibution", api.GradeDistibution)               // 等级分布
		oa.POST("/retainedata", api.RetaineData)                         // 留存数据
		oa.POST("/vipdistbution", api.VipDistibution)                    // VIP分布
		oa.POST("/firstrechargegradedist", api.FirstRechargeGradeDist)   // 首次充值等级分布
		oa.POST("/equipemtstatistics", api.EquipemtStatistics)           // 装备统计汇总
		oa.POST("/ontimestatistics", api.OnTimeStatistics)               // 实时在线统计
		oa.POST("/rechargerankquery", api.RechargeRankQuery)             // 充值排行查询
		oa.POST("/livdata", api.LivData)                                 // LIV数据
		oa.POST("/loginonlinedistribution", api.LoginOnlineDistribution) // 登录在线分布
		oa.POST("/rollzonedata", api.RollZoneData)                       // 滚服数据
	}

	/* player api */
	pa := r.Group("/pa/api")
	{
		pa.Use(middleware.JwtAuth(), middleware.IpWhite())
		pa.POST("/getroleinfo", api.GetRoleInfo)   // 角色信息
		pa.POST("/getorderinfo", api.GetOrderInfo) // 订单查询
		pa.POST("/getcurrencon", api.GetCurrenCon) // 货币消耗
	}

	/* gifts api */
	gt := r.Group("/gt/api")
	{
		gt.Use(middleware.JwtAuth(), middleware.IpWhite())
		gt.POST("/configgifts", api.ConfigGifts)     // 配置礼包
		gt.POST("/getactivecode", api.GetActiveCode) // 激活码列表
	}

	return r
}
