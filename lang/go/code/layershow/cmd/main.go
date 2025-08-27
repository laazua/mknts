package main

import (
	"net/http"

	"layershow/internal/api"
	"layershow/internal/dao"
	"layershow/internal/service"
	"layershow/pkg/core"
	"layershow/pkg/db"
)

func main() {
	// 初始化 DB
	db, err := db.Get()
	if err != nil {
		panic(err)
	}
	// 初始化依赖
	userDAO := dao.NewUserDao(db)
	userService := service.NewUserService(userDAO)
	userHandler := api.NewUserHandler(userService)

	route := core.NewRouter()
	userHandler.RegisterRoutes(route)

	server := http.Server{
		Addr:    ":8088",
		Handler: route,
	}
	if err := server.ListenAndServe(); err != nil {
		panic(err)
	}
}
