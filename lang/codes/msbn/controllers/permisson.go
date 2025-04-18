package routers

import (
	"msbn/models"

	"github.com/gin-gonic/gin"
)

// 获取权限列表
func GetMenusList(c *gin.Context) {
	p := models.QuerySysPermisson()
	if p == nil {
		c.JSON(200, gin.H{
			"message": "获取菜单列表失败!",
			"data":    nil,
			"code":    400,
		})
	}
	c.JSON(200, gin.H{
		"message": "获取菜单列表成功!",
		"data":    p,
		"code":    200,
	})
}

// 添加权限
func AddMenus(c *gin.Context) {
	var permissonSchema models.AddPerSchema
	if err := c.BindJSON(&permissonSchema); err != nil {
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    nil,
			"code":    400,
		})
		return
	}

	if !models.AddSysPermisson(permissonSchema.Desc,
		permissonSchema.Namepath, permissonSchema.Mainmenu,
		permissonSchema.Subdesc, permissonSchema.Subpath) {
		c.JSON(200, gin.H{
			"message": "添加权限失败!",
			"data":    permissonSchema,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "添加权限成功!",
		"data":    permissonSchema,
		"code":    200,
	})
}

// 更新权限
func UpdateMenus(c *gin.Context) {}

// 删除权限
func DeleteMenus(c *gin.Context) {}

// 根据id获取单个权限
func GetMenusById(c *gin.Context) {}
