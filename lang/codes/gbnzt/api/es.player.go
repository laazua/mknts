package api

import "github.com/gin-gonic/gin"

// 玩家接口
type EsPlayer interface {
	OrderData(c *gin.Context)
	RoleData(c *gin.Context)
	CurrData(c *gin.Context)
}

func NewPlayer() EsPlayer {
	return &player{}
}

type player struct{}

//
// @Description  订单查询
// @Tags 业务玩家相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Rgs false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询订单成功"}"
// @Router /player/api/orderdata [post]
func (p *player) OrderData(c *gin.Context) {

}

//
// @Description  角色查询
// @Tags 业务玩家相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Ods false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询角色成功"}"
// @Router /player/api/roledata [post]
func (p *player) RoleData(c *gin.Context) {

}

//
// @Description  货币消耗
// @Tags 业务玩家相关
// @Accept application/json
// @Produce application/json
// @Param object body models.Cds false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询货币成功"}"
// @Router /player/api/currdata [post]
func (p *player) CurrData(c *gin.Context) {

}
