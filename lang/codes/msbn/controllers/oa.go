package routers

import (
	"fmt"
	"msbn/models"
	"msbn/utils"

	"github.com/gin-gonic/gin"
)

// 数据查询
func DataQuery(c *gin.Context) {
	var dataQ models.GradeDistibutionSchema
	if err := c.BindJSON(&dataQ); err != nil {
		fmt.Println(err)
		c.JSON(400, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
	}
	res, err := utils.GetData(dataQ.Stime, dataQ.Etime, dataQ.Zone, dataQ.Page.Size, dataQ.Page.Num)
	if err != nil {
		c.JSON(400, gin.H{
			"message": err,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "数据查询",
		"data":    res,
		"code":    200,
	})
}

// 等级分布
func GradeDistibution(c *gin.Context) {
	var grade models.GradeDistibutionSchema
	if err := c.BindJSON(&grade); err != nil {
		fmt.Println(err)
		c.JSON(400, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    400,
		})
		return
	}
	res, err := utils.GetGradeDistribution(grade.Stime, grade.Etime, grade.Zone, grade.Page.Size, grade.Page.Num)
	if err != nil {
		c.JSON(400, gin.H{
			"message": err,
			"code":    400,
		})
		return
	}
	c.JSON(200, gin.H{
		"message": "等级分布",
		"data":    res,
		"code":    200,
	})
}

// 留存数据
func RetaineData(c *gin.Context) {

}

// VIP分布
func VipDistibution(c *gin.Context) {
	var vgs models.VipGradeSchema
	if err := c.BindJSON(&vgs); err != nil {
		c.JSON(200, gin.H{
			"message": "表单参数错误",
			"code":    400,
		})
		return
	}
	fmt.Println(vgs.Zone)
	c.JSON(200, gin.H{
		"code": 200,
		"data": "VIP等级",
	})
}

// 首次充值等级分布
func FirstRechargeGradeDist(c *gin.Context) {

}

// 装备统计汇总
func EquipemtStatistics(c *gin.Context) {

}

// 实时在线统计
func OnTimeStatistics(c *gin.Context) {

}

// 充值排行查询
func RechargeRankQuery(c *gin.Context) {
	var rechargeSchema models.RechargeRankSchema
	if err := c.BindJSON(&rechargeSchema); err != nil {
		fmt.Println(err.Error())
		c.JSON(200, gin.H{
			"message": "获取表单参数错误!",
			"data":    err,
			"code":    200,
		})
		return
	}
	resp, err := utils.GetRechargeRank(
		rechargeSchema.Stime, rechargeSchema.Etime,
		rechargeSchema.Zone, rechargeSchema.Page.Size,
		rechargeSchema.Page.Num)
	if err != nil {
		c.JSON(400, gin.H{
			"message": "ES数据查询失败!",
			"data":    nil,
			"code":    200,
		})
	}
	c.JSON(200, gin.H{
		"message": "获取充值排行查询成功!",
		"data":    resp,
		"code":    200,
	})
}

// LIV数据
func LivData(c *gin.Context) {

}

// 登录在线分布
func LoginOnlineDistribution(c *gin.Context) {

}

// 滚服数据
func RollZoneData(c *gin.Context) {
	res, err := utils.GetRollData()
	if err != nil {
		c.JSON(200, gin.H{
			"message": err,
			"code":    200,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": res,
		"code": 200,
	})
}
