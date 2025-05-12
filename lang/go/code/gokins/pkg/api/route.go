package api

import (
	"net/http"

	"gokins/pkg/core"
)

func NewMuxServe() *core.MuxServer {

	muxServe := core.NewMuxServer()

	// 绑定user路由
	muxServe.HandleFunc("GET /user/login", signUser)
	muxServe.HandleFunc("GET /user/get", authMiddleware(getUser))
	muxServe.HandleFunc("GET /user/info", authMiddleware(infoUser))
	muxServe.HandleFunc("PUT /user/add", authMiddleware(addUser))
	muxServe.HandleFunc("DELETE /user/del", authMiddleware(delUser))
	muxServe.HandleFunc("POST /user/upt", authMiddleware(updateUser))

	// 绑定task路由
	muxServe.HandleFunc("GET /task/add", authMiddleware(runTask))
	muxServe.HandleFunc("POST /task/:name", authMiddleware(addTask))

	return muxServe
}

func authMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Header.Get("Authorization") != "Bearer tokenstr" {
			http.Error(w, "Forbidden", http.StatusForbidden)
			return
		}
		next.ServeHTTP(w, r)
	}
}
