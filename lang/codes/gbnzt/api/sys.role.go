package api

import (
	"bnzt/models"

	"github.com/gin-gonic/gin"
)

// 角色接口
type Role interface {
	BaseApi
}

// 实现角色接口实例
type role struct {
	Ars models.Ars
	Grs models.Grs
	Urs models.Urs
}

//
// @Description  查询角色
// @Tags 系统角色相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Grs false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "查询角色成功"}"
// @Router /role/api/roles [get]
func (r *role) Get(c *gin.Context) {
	if err := c.BindJSON(&r.Grs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	role, err := roleDao.GetRole(r.Grs.Name)
	if err != nil {
		resp.Failed(c, nil, "查询角色失败")
		return
	}
	resp.Success(c, role, "查询角色成功")
}

// @Description  添加角色
// @Tags 系统角色相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Ars false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "添加角色成功"}"
// @Router /role/api/roles [post]
func (r *role) Add(c *gin.Context) {
	if err := c.BindJSON(&r.Ars); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !roleDao.AddRole(r.Ars.Name, r.Ars.Desc, r.Ars.Menu) {
		resp.Failed(c, nil, "添加角色失败")
		return
	}
	resp.Success(c, nil, "添加角色成功")
}

//
// @Description  删除角色
// @Tags 系统角色相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Drs false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "删除角色成功"}"
// @Router /role/api/roles [delete]
func (r *role) Del(c *gin.Context) {
	if err := c.BindJSON(&r.Grs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !roleDao.DelRole(r.Grs.Name) {
		resp.Failed(c, nil, "删除角色失败")
		return
	}
	resp.Success(c, nil, "删除角色成功")
}

//
// @Description  更新角色
// @Tags 系统角色相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Urs false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "更新角色成功"}"
// @Router /role/api/roles [put]
func (r *role) Upd(c *gin.Context) {
	if err := c.BindJSON(&r.Urs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !roleDao.UpdRole(r.Urs.Name, r.Urs.Column, r.Urs.Value) {
		resp.Failed(c, nil, "更新角色失败")
		return
	}
	resp.Success(c, nil, "更新角色成功")
}

//
// @Description  角色列表
// @Tags 系统角色相关
// @Accept application/json
// @Produce application/json
// @Success 200 {string} json "{"data": object, "code":200, "message": "获取角色列表成功"}"
// @Router /role/api/rolelist [put]
func (r *role) GetList(c *gin.Context) {
	roles := roleDao.RoleList()
	resp.Success(c, roles, "获取角色列表成功")
}
