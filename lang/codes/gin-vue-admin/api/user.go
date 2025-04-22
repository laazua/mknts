// 用户接口

package api

import (
	"gin-vue-admin/api/form"

	"github.com/gin-gonic/gin"
)

type UserApi struct {
	LoginForm form.LoginForm
}

func (userApi *UserApi) Login(ctx *gin.Context) {
	ctx.Bind(&userApi.LoginForm)
	// 数据库查询

	// 返回token
	ctx.JSON(200, gin.H{"message": "success"})
}

func (userApi *UserApi) GetInfo(ctx *gin.Context) {
	// 获取用户&&角色信息

	// 获取侧边栏菜单信息
}
