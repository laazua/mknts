package controller

import (
	"fmt"
	"log/slog"
	"stdhttp/pkg/router"
	"net/http"
)

type Auth struct {
	Logger *slog.Logger
}

func (a *Auth) Name() string {
	return "auth"
}

func (a *Auth) InitRoute(router *router.Router) {
	a.Logger.Info(fmt.Sprintf("URI: %v", router.Prefix))
	router.Handle(http.MethodPost, router.Prefix+"/login", http.HandlerFunc(a.login))
}

func (a *Auth) login(w http.ResponseWriter, r *http.Request) {
	success(w, object{"code": 200, "message": "login success"})
}
