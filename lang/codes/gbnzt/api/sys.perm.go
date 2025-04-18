package api

import (
	"bnzt/models"
	"log"

	"github.com/gin-gonic/gin"
)

// 权限接口
type Perm interface {
	BaseApi
}

// 实现权限接口的实例
type perm struct {
	Ams models.Ams
	Gms models.Gms
	Dms models.Dms
	Ums models.Ums
}

//
// @Description  查询菜单
// @Tags 系统菜单相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Gms false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询菜单成功"}"
// @Router /perm/api/perms [get]
func (p *perm) Get(c *gin.Context) {
	if err := c.BindJSON(&p.Gms); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	perm, err := permDao.GetPerm(p.Gms.Permdesc)
	if err != nil {
		resp.Failed(c, nil, "查询菜单失败")
		return
	}
	resp.Success(c, perm, "查询菜单成功")
}

//
// @Description  添加菜单
// @Tags 系统菜单相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Ams false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "添加菜单成功"}"
// @Router /perm/api/perms [post]
func (p *perm) Add(c *gin.Context) {
	if err := c.BindJSON(&p.Ams); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	log.Println("xxxx", p.Ams)
	if !permDao.AddPerm(p.Ams.Permdesc,
		p.Ams.Namepath, p.Ams.Subdesc, p.Ams.Subpath) {
		resp.Failed(c, nil, "添加菜单失败")
		return
	}
	resp.Success(c, nil, "添加菜单成功")
}

//
// @Description  删除菜单
// @Tags 系统菜单相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Dms false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "删除菜单成功"}"
// @Router /perm/api/perms [delete]
func (p *perm) Del(c *gin.Context) {
	if err := c.BindJSON(&p.Dms); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !permDao.DelPerm(p.Ams.Permdesc) {
		resp.Failed(c, nil, "删除菜单失败")
		return
	}
	resp.Success(c, nil, "删除菜单成功")
}

//
// @Description  更新菜单
// @Tags 系统菜单相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Ums false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "更新菜单成功"}"
// @Router /perm/api/perms [put]
func (p *perm) Upd(c *gin.Context) {
	if err := c.BindJSON(&p.Ums); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !permDao.UpdPerm(p.Ums.Permdesc, p.Ums.Column, p.Ums.Value) {
		resp.Failed(c, nil, "更新菜单失败")
		return
	}
	resp.Success(c, nil, "更新菜单成功")
}

//
// @Description  菜单列表
// @Tags 系统菜单相关
// @Accept application/json
// @Produce application/json
// @Success 200 {string} json "{"data": object, "code":200, "message": "获取菜单列表成功"}"
// @Router /perm/api/permlist [get]
func (p *perm) GetList(c *gin.Context) {
	perm := permDao.PermList()
	resp.Success(c, perm, "获取菜单列表成功")
}
