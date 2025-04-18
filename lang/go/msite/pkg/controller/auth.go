package controller

import (
	"log/slog"
	"msite/pkg/router"
	"msite/pkg/schema"
	"msite/pkg/utils"
	"net/http"
)

type Auth struct {
	Logger *slog.Logger
}

func (a *Auth) Name() string {
	return "auth"
}

func (a *Auth) InitRoute(router *router.Router) {
	auth := router.Group("/auth")
	auth.Handle(http.MethodPost, "/login", http.HandlerFunc(a.login))
}

func (a *Auth) login(w http.ResponseWriter, r *http.Request) {
	var user schema.User
	if err := bind(r, &user); err != nil {
		failure(w, object{"code": http.StatusInternalServerError, "message": "bind schema error: " + err.Error()})
		return
	}
	// 数据库验证用户和秘密

	// 生成token
	token, err := utils.CreateToken(user.Name)
	if err != nil {
		failure(w, object{"code": http.StatusInternalServerError, "message": "create token error: " + err.Error()})
	}

	success(w, object{"code": http.StatusOK, "message": "login success", "token": token})
}
