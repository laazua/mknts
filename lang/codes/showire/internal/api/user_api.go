package api

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"show/internal/model"
	"show/internal/service"
)

type UserController struct {
	svc *service.UserService
}

func NewUserController(svc *service.UserService) *UserController {
	return &UserController{svc: svc}
}

// 实现Api接口
func (ctl *UserController) RegApi(mux *http.ServeMux) {
	mux.HandleFunc("POST /user/create", ctl.createUser)
	mux.HandleFunc("GET /user/get", ctl.getUser)
	mux.HandleFunc("PUT/user/update", ctl.updateUser)
	mux.HandleFunc("DELETE /user/delete", ctl.deleteUser)
}

func (ctl *UserController) createUser(w http.ResponseWriter, r *http.Request) {
	var u model.User
	_ = json.NewDecoder(r.Body).Decode(&u)
	ctl.svc.CreateUser(&u)

	w.Write([]byte(fmt.Sprintf("{id: %v, name: %v, age: %v}\n", u.ID, u.Name, u.Age)))
}

func (ctl *UserController) getUser(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(r.URL.Query().Get("id"))
	user := ctl.svc.GetUser(id)
	json.NewEncoder(w).Encode(user)
}

func (ctl *UserController) updateUser(w http.ResponseWriter, r *http.Request) {
	var u model.User
	_ = json.NewDecoder(r.Body).Decode(&u)
	ctl.svc.UpdateUser(&u)
	w.Write([]byte("user updated"))
}

func (ctl *UserController) deleteUser(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(r.URL.Query().Get("id"))
	ctl.svc.DeleteUser(id)
	w.Write([]byte("user deleted"))
}
