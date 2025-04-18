package routers

import (
	"msbn/models"

	"github.com/gin-gonic/gin"
)

// 获取角色列表
func GetRoleList(c *gin.Context) {
	r := models.QuerySysRoleList()
	c.JSON(200, gin.H{
		"message": "角色列表",
		"data":    r,
		"code":    200,
	})
}

// 添加角色
func AddRole(c *gin.Context) {
	var roleSchema models.AddRoleSchema
	if err := c.BindJSON(&roleSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if !models.AddSysRole(roleSchema.Rolename, roleSchema.Desc) {
		c.JSON(200, gin.H{
			"message": "创建角色失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "添加角色成功!",
		"data":    roleSchema,
		"code":    200,
	})
}

// 更新角色
func UpdateRole(c *gin.Context) {
	var upRoleSchema models.UpRoleSchema
	if err := c.BindJSON(&upRoleSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "更新角色",
		"data":    nil,
	})
}

// 删除角色
func DeleteRole(c *gin.Context) {
	var delRoleSchema models.DelRoleSchema
	if err := c.BindJSON(&delRoleSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if !models.DeleteSysRole(delRoleSchema.Rolename) {
		c.JSON(200, gin.H{
			"message": "删除角色失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "删除角色成功！",
		"data":    nil,
		"code":    200,
	})
}

// 根据id获取单个角色
// func GetRoleById(c *gin.Context) {
// 	roleid := c.Param("id")
// 	rid, _ := strconv.ParseUint(roleid, 10, 64)
// 	r := models.GetSysRoleById(rid)
// 	c.JSON(200, gin.H{
// 		"message": "根据id获取单个角色",
// 		"data":    r,
// 	})
// }

// 给角色分配权限
func DistributeMenusForRole(c *gin.Context) {
	var rpSchema models.RpSchema
	if err := c.BindJSON(&rpSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	if !models.DistributeMenus(rpSchema.Rolename, rpSchema.MainMenu) {
		c.JSON(200, gin.H{
			"message": "给角色分配权限失败!",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "给角色分配权限成功!",
		"data":    nil,
		"code":    200,
	})
}
