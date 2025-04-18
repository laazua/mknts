package api

import (
	"bnzt/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

// 用户接口
type User interface {
	BaseApi
	Login(c *gin.Context)
}

// 实现用户接口的实例
type user struct {
	Uls models.Uls
	Aus models.Aus
	Dus models.Dus
	Uus models.Uus
}

//
// @Description  用户查询
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Success 200 {string} json "{"data": object, "code":200, "message": "用户查询成功"}"
// @Router /user/api/users [get]
func (u *user) Get(c *gin.Context) {
	name, _ := c.Get("name")
	user, err := userDao.GetUser(name.(string))
	if err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 根据用户名获取用户信息
	resp.Success(c, user, "用户查询成功")
}

//
// @Description  添加用户
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Aus false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "添加用户成功"}"
// @Router /user/api/users [post]
func (u *user) Add(c *gin.Context) {
	if err := c.BindJSON(&u.Aus); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 验证密码
	if u.Aus.PassOne != u.Aus.PassTow {
		resp.Failed(c, nil, ErrPass)
		return
	}
	if !userDao.AddUser(u.Aus.Name, u.Aus.PassOne) {
		resp.Failed(c, nil, "添加用户失败")
		return
	}
	resp.Success(c, nil, "添加用户成功")
}

//
// @Description  删除用户
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Dus false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "删除用户成功"}"
// @Router /user/api/users [delete]
func (u *user) Del(c *gin.Context) {
	if err := c.BindJSON(&u.Dus); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !userDao.DelUser(u.Dus.Name) {
		resp.Failed(c, nil, "删除用户失败")
		return
	}
	resp.Success(c, nil, "删除用户成功")
}

//
// @Description  更新用户
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Aus false "查询参数"
// @Success 200 {string} json "{"data": nil, "code":200, "message": "更新用户成功"}"
// @Router /user/api/users [put]
func (u *user) Upd(c *gin.Context) {
	if err := c.BindJSON(&u.Uus); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	if !userDao.UpdUser(u.Uus.Name, u.Uus.Column, u.Uus.Value) {
		resp.Failed(c, nil, "更新用户失败")
		return
	}
	resp.Success(c, nil, "更新用户成功")
}

//
// @Description  用户列表
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Aus false "查询参数"
// @Success 200 {string} json "{"data": object, "code":200, "message": "获取用户列表成功"}"
// @Router /user/api/userlist [get]
func (u *user) GetList(c *gin.Context) {
	users := userDao.UserList()
	resp.Success(c, users, "获取用户列表成功")
}

//
// @Description  用户登录
// @Tags 系统用户相关
// @Accept application/json
// @Produce application/json
// @Param object query models.Aus false "查询参数"
// @Success 200 {string} json "{"token": "", "code":200}"
// @Router /user/api/login [post]
func (u *user) Login(c *gin.Context) {
	if err := c.BindJSON(&u.Uls); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 验证用户跟密码
	if !userDao.ChkUser(u.Uls.Username, u.Uls.Password) {
		resp.Failed(c, nil, ErrPass)
		return
	}
	// 创建token
	token, err := tk.Create(u.Uls.Username)
	if err != nil {
		resp.Failed(c, nil, ErrToken)
		return
	}
	// 返回token
	c.JSON(http.StatusOK, gin.H{
		"token": token,
		"code":  200})
}
