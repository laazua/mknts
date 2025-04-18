package api

import (
	"bnzt/models"

	"github.com/gin-gonic/gin"
)

// elastic接口
type EsOa interface {
	RechaRank(c *gin.Context)
	GradeDist(c *gin.Context)
	CountData(c *gin.Context)
	RollsData(c *gin.Context)
	RetenData(c *gin.Context)
	VipsData(c *gin.Context)
	LtvsData(c *gin.Context)
}

func NewEsOa() EsOa {
	return &esOa{}
}

// 实现EsOaApi接口的实例
type esOa struct {
	Rrs models.Rrs
	Gds models.Gds
	Dgs models.Dgs
	Rds models.Rds
	Kds models.Kds
}

//
// @Description  充值排行
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Rrs false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "成功获取数据"}"
// @Router /oa/api/recharank [post]
func (e *esOa) RechaRank(c *gin.Context) {
	if err := c.BindJSON(&e.Rrs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetRechaRank(e.Rrs)
	if err != nil {
		resp.Failed(c, nil, "充值排行查询失败")
		return
	}
	resp.Success(c, result, "成功获取数据")
}

//
// @Description  等级分布
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "等级分布查询成功"}"
// @Router /oa/api/gradedist [post]
func (e *esOa) GradeDist(c *gin.Context) {
	if err := c.BindJSON(&e.Gds); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetGradeDist(e.Gds)
	if err != nil {
		resp.Failed(c, nil, "等级分布查询失败")
		return
	}
	resp.Success(c, result, "等级分布查询成功")
}

//
// @Description  数据查询
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "数据查询成功"}"
// @Router /oa/api/countdata [post]
func (e *esOa) CountData(c *gin.Context) {
	if err := c.BindJSON(&e.Dgs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetCountData(e.Dgs)
	if err != nil {
		resp.Failed(c, nil, "数据查询失败")
		return
	}
	resp.Success(c, result, "数据查询成功")
}

//
// @Description  滚服数据
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询滚服数据成功"}"
// @Router /oa/api/rollsdata [post]
func (e *esOa) RollsData(c *gin.Context) {
	if err := c.BindJSON(&e.Rds); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetCountData(e.Dgs)
	if err != nil {
		resp.Failed(c, nil, "查询滚服数据失败")
		return
	}
	resp.Success(c, result, "查询滚服数据成功")
}

//
// @Description  留存数据
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询留存数据成功"}"
// @Router /oa/api/retendata [post]
func (e *esOa) RetenData(c *gin.Context) {
	if err := c.BindJSON(&e.Kds); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetCountData(e.Dgs)
	if err != nil {
		resp.Failed(c, nil, "查询留存数据失败")
		return
	}
	resp.Success(c, result, "查询留存数据成功")
}

//
// @Description  VIP等级
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询VIP等级成功"}"
// @Router /oa/api/vipsdata [post]
func (e *esOa) VipsData(c *gin.Context) {
	if err := c.Bind(&e.Dgs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetCountData(e.Dgs)
	if err != nil {
		resp.Failed(c, nil, "查询VIP等级失败")
		return
	}
	resp.Success(c, result, "查询VIP等级成功")
}

//
// @Description  LTV数据
// @Tags 业务运营相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Gds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询LTV数据成功"}"
// @Router /oa/api/ltvsdata [post]
func (e *esOa) LtvsData(c *gin.Context) {
	if err := c.BindJSON(e.Dgs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	result, err := oa.GetCountData(e.Dgs)
	if err != nil {
		resp.Failed(c, nil, "查询LTV数据失败")
		return
	}
	resp.Success(c, result, "查询LTV数据成功")
}
