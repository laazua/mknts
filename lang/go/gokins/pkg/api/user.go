package api

import (
	"fmt"
	"log/slog"
	"net/http"

	"gokins/pkg/core"
	"gokins/pkg/model"
	"gokins/pkg/service"
)

// 用户登陆
func signUser(w http.ResponseWriter, r *http.Request) {
	slog.Info("## 用户登陆")
	// 获取客户端认证
	var login model.UserLoginForm
	ctx := &core.Context{Writer: w, Request: r}

	if err := ctx.BindJSON(&login); err != nil {
		slog.Error(fmt.Sprintf("## 获取客户端请求数据失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "获取客户端请求数据失败"})
		return
	}
	// 获取数据库认证
	db, err := core.NewDb()
	if err != nil {
		slog.Error(fmt.Sprintf("## 实例化数据库失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "实例化数据库失败"})
		return
	}
	defer db.Pool.Close()
	dbUser := service.NewDbUser(db)
	if !dbUser.Auth(login) {
		slog.Info("## 用户名或者密码错误")
		ctx.JSON(400, core.H{"msg": "用户名或者密码错误"})
		return
	}

	ctx.JSON(200, core.H{"msg": "登陆成功"})

}

func infoUser(w http.ResponseWriter, r *http.Request) {

}

// 新增用户
func addUser(w http.ResponseWriter, r *http.Request) {
	slog.Info("## 添加用户")
	var user model.UserForm
	ctx := &core.Context{Writer: w, Request: r}
	if err := ctx.BindJSON(&user); err != nil {
		slog.Error(fmt.Sprintf("## 获取客户端请求参数失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "获取客户端请求参数失败"})
		return
	}
	// TODO: 信息入库
	db, err := core.NewDb()
	if err != nil {
		slog.Error("## 实例化数据库失败")
		ctx.JSON(400, core.H{"msg": "实例化数据库失败"})
		return
	}
	defer db.Pool.Close()
	dbUser := service.NewDbUser(db)
	if !dbUser.Add(user) {
		ctx.JSON(400, core.H{"msg": "用户信息入库失败"})
		return
	}
	ctx.JSON(200, core.H{"msg": "用户信息入库成功"})
}

// 删除用户
func delUser(w http.ResponseWriter, r *http.Request) {
	slog.Info("## 删除用户")
	var user model.UserForm
	ctx := &core.Context{Writer: w, Request: r}
	if err := ctx.BindJSON(&user); err != nil {
		slog.Error(fmt.Sprintf("## 获取客户端请求参数失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "获取客户端请求参数失败"})
		return
	}
	db, err := core.NewDb()
	if err != nil {
		slog.Error(fmt.Sprintf("## 实例化数据库失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "实例化数据库失败"})
		return
	}
	defer db.Pool.Close()
	dbUser := service.NewDbUser(db)
	if !dbUser.Delete(user) {
		ctx.JSON(400, core.H{"msg": "删除用户失败"})
		return
	}
	ctx.JSON(200, core.H{"msg": "删除用户成功"})
}

// 获取用户列表
func getUser(w http.ResponseWriter, r *http.Request) {
	slog.Info("## 获取用户")
	ctx := &core.Context{Writer: w, Request: r}
	db, err := core.NewDb()
	if err != nil {
		slog.Error(fmt.Sprintf("## 实例化数据库失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "实例化十几块失败"})
		return
	}
	defer db.Pool.Close()
	dbUser := service.NewDbUser(db)
	users, err := dbUser.Query()
	if err != nil {
		slog.Error(fmt.Sprintf("## 获取用户列表失败: %v\n", err))
		ctx.JSON(400, core.H{"msg": "获取用户列表失败"})
		return
	}
	ctx.JSON(200, core.H{"msg": "获取用户列表成功", "users": users})
}

// 更新用户
func updateUser(w http.ResponseWriter, r *http.Request) {

}
