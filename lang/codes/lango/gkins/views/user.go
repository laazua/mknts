package views

import (
	"log/slog"
	"net/http"

	"gkins/form"
	"gkins/store"
	"gkins/utils"
)

// Login 用户登陆
func Login(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet {
		renderTemplate(w, "login.html", nil)
		return
	}
	if r.Method == http.MethodPost {
		email := r.FormValue("email")
		password := r.FormValue("password")
		if store.AuthUser(email, password) {
			token, _ := utils.CreateToken(email)
			http.SetCookie(w, &http.Cookie{
				Name:  "token",
				Value: token,
			})
			http.Redirect(w, r, "/dashboard", http.StatusSeeOther)
			return
		}
		loginData := loginResp{ErrMsg: "Validate Failure"}
		renderTemplate(w, "login.html", loginData)
	}
}

// CreateUser 新增用户
func CreateUser(w http.ResponseWriter, r *http.Request) {
	var userForm form.User
	if err := bind(r, userForm); err != nil {
		slog.Error("Create User Failure", slog.String("error", err.Error()))
		return
	}
	if err := store.CreateUser(userForm); err != nil {
		slog.Error("Create User To Db Failure", slog.String("error", err.Error()))
		return
	}
	renderTemplate(w, "user.html", nil)
}

// DeleteUser 删除用户
func DeleteUser(w http.ResponseWriter, r *http.Request) {
	var userForm form.User
	if err := bind(r, userForm); err != nil {
		slog.Error("Delete User Failure", slog.String("error", err.Error()))
		return
	}
	if err := store.DeleteUser(userForm); err != nil {
		slog.Error("Delete User From Db Failure", slog.String("error", err.Error()))
		return
	}
	renderTemplate(w, "user.html", nil)
}

// UpdateUser 更新用户
func UpdateUser(w http.ResponseWriter, r *http.Request) {}

// QueryUser 查询用户
func QueryUser(w http.ResponseWriter, r *http.Request) {}

// UserList 用户列表
func UserList(w http.ResponseWriter, r *http.Request) {
	users := store.UserList()
	renderTemplate(w, "user", users)
}
