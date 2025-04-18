package routers

import (
	"msbn/models"
	"msbn/utils"

	"github.com/gin-gonic/gin"
)

// 角色信息
func GetRoleInfo(c *gin.Context) {
	var roleq models.RoleSchema
	if err := c.BindJSON(&roleq); err != nil {
		c.JSON(200, gin.H{
			"message": "表单绑定错误",
			"data":    err,
			"code":    400,
		})
		return
	}
	res, err := utils.GetRole(roleq.Zone, roleq.Uid)
	if err != nil {
		c.JSON(200, gin.H{
			"message": "获取数据错误",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "获取数据成功!",
		"data":    res,
		"code":    200,
	})
}

// 订单查询
func GetOrderInfo(c *gin.Context) {
	var orderq models.OrderSchema
	if err := c.BindJSON(&orderq); err != nil {
		c.JSON(200, gin.H{
			"message": "表单绑定错误",
			"data":    err,
			"code":    400,
		})
		return
	}
	res, err := utils.GetOrder(orderq.Zone, orderq.Uid, orderq.Order)
	if err != nil {
		c.JSON(200, gin.H{
			"message": "获取数据错误",
			"data":    nil,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "获取数据成功!",
		"data":    res,
		"code":    200,
	})
}

// 货币消耗
func GetCurrenCon(c *gin.Context) {

}
