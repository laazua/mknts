package controller

import (
	"fmt"
	"log/slog"
	"net/http"

	"msite/pkg/env"
	"msite/pkg/router"
	"msite/pkg/schema"
	"msite/pkg/storage"
)

type User struct {
	Logger  *slog.Logger
	Storage *storage.User
}

// 实现Controller接口
func (u *User) Name() string {
	return "user"
}

func (u *User) InitRoute(router *router.Router) {
	user := router.Group("/user")
	user.Handle(http.MethodPost, "/create", http.HandlerFunc(u.create))
	user.Handle(http.MethodDelete, "/delete", http.HandlerFunc(u.delete))
	user.Handle(http.MethodPut, "/update", http.HandlerFunc(u.update))
	user.Handle(http.MethodGet, "/query", http.HandlerFunc(u.query))
	user.Handle(http.MethodGet, "/query/{id}", http.HandlerFunc(u.queryId))
}

func (u *User) create(w http.ResponseWriter, r *http.Request) {
	var user schema.User
	if err := bind(r, &user); err != nil {
		u.Logger.Error(fmt.Sprintf("user create api bind schema error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user create api bind schema error"})
		return
	}
	if err := u.Storage.Create(user); err != nil {
		u.Logger.Error(fmt.Sprintf("user create api storage user error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user create api storage user error"})
		return
	}
	success(w, object{"code": http.StatusOK, "message": "add user success"})
}
func (u *User) delete(w http.ResponseWriter, r *http.Request) {
	var user schema.User
	if err := bind(r, &user); err != nil {
		u.Logger.Error(fmt.Sprintf("user delete api bind schema error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user delete api bind schema error"})
		return
	}
	if err := u.Storage.Delete(user.Id); err != nil {
		u.Logger.Error(fmt.Sprintf("user delete api Storage user error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user delete api storage user error"})
		return
	}
	success(w, object{"code": http.StatusOK, "message": "delete user success"})
}
func (u *User) update(w http.ResponseWriter, r *http.Request) {
	var user schema.User
	if err := bind(r, &user); err != nil {
		u.Logger.Error(fmt.Sprintf("user update api bind schema error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user update api bind schema error"})
		return
	}
	if err := u.Storage.Update(user); err != nil {
		u.Logger.Error(fmt.Sprintf("user update api storage user error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user update api storage user error"})
		return
	}
	success(w, object{"code": http.StatusOK, "message": "update user success"})
}
func (u *User) query(w http.ResponseWriter, r *http.Request) {
	users, err := u.Storage.Query()
	if err != nil {
		u.Logger.Error(fmt.Sprintf("user query api storage user error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user query api storage user error"})
		return
	}
	success(w, object{"code": http.StatusOK, "message": "query users success", "users": users})
}
func (u *User) queryId(w http.ResponseWriter, r *http.Request) {
	id := router.Param(r, "id")
	user, err := u.Storage.QueryId(env.StoInt(id))
	if err != nil {
		u.Logger.Error(fmt.Sprintf("user queryId api storage user error: %v", err.Error()))
		failure(w, object{"code": http.StatusInternalServerError, "message": "user queryId api storage user error"})
		return
	}
	success(w, object{"code": http.StatusOK, "message": "query user success", "user": user})
}
