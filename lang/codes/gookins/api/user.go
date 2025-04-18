package api

import (
	"log/slog"
	"net/http"
	"strconv"

	"gookins/core"
	"gookins/model"
	"gookins/service"

	"github.com/gin-gonic/gin"
)

// @Summary 用户登录
// @Description 用户登录接口
// @Tags 用户
// @Accept json
// @Produce json
// @Param login body model.LoginForm true "登录请求参数"
// @Success 200 {object} model.LoginRespon "成功返回Token"
// @Failure 500 {object} model.ApiRespone "无效的凭据"
// @Router /login [post]
func UserSign(ctx *gin.Context) {
	var userForm model.LoginForm
	if err := ctx.ShouldBindJSON(&userForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	if err := service.UserSign(userForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 404, Message: err.Error()})
		return
	}
	token, err := core.CreateToken(userForm.Name)
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.LoginRespon{Code: 200, Message: "登陆成功", Token: token})
}

// @Summary 创建用户
// @Description 用户创建接口
// @Security ApiKeyAuth
// @Tags 用户
// @Accept json
// @Produce json
// @Param user body model.UserForm true "创建用户请求参数"
// @Success 200 {object} model.ApiRespone "创建用户成功"
// @Failure 500 {object} model.ApiRespone "创建用户失败"
// @Router /user/add [post]
func CreateUser(ctx *gin.Context) {
	var userForm model.UserForm
	if err := ctx.ShouldBindJSON(&userForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	if err := service.CreateUser(userForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "创建用户成功"})
}

// @Summary 删除用户
// @Description 用户删除接口
// @Security ApiKeyAuth
// @Tags 用户
// @Accept json
// @Produce json
// @Param id path string true "用户ID"
// @Success 200 {object} model.ApiRespone "删除用户成功"
// @Failure 500 {object} model.ApiRespone "删除用户失败"
// @Router /user/del/{id} [delete]
func DeleteUser(ctx *gin.Context) {
	idStr := ctx.Param("id")
	id, err := strconv.ParseUint(idStr, 10, 0) // 将字符串转换为 uint64
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	if err := service.DeleteUser(id); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "删除用户成功"})
}

// @Summary 更新用户
// @Description 用户更新接口
// @Security ApiKeyAuth
// @Tags 用户
// @Accept json
// @Produce json
// @Param user body model.UserForm true "更新用户请求参数"
// @Success 200 {object} model.ApiRespone "更新用户成功"
// @Failure 500 {object} model.ApiRespone "更新用户失败"
// @Router /user/upt/{id} [put]
func UpdateUser(ctx *gin.Context) {
	var userForm model.UserForm
	if err := service.UpdateUser(userForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "更新用户成功"})
}

// @Summary 用户列表
// @Description 用户列表接口
// @Security ApiKeyAuth
// @Tags 用户
// @Accept json
// @Produce json
// @Success 200 {object} model.ApiRespone "获取用户列表成功"
// @Failure 500 {object} model.ApiRespone "获取用户列表失败"
// @Router /user/list [get]
func UserLists(ctx *gin.Context) {
	users, err := service.UserLists()
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "获取用户列表成功", Data: users})
}
