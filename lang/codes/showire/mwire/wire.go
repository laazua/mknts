// wire/wire.go
//go:build wireinject
// +build wireinject

package mwire

import (
	"show/internal/api"
	"show/internal/app"
	"show/internal/dao"
	"show/internal/service"

	"github.com/google/wire"
)

func InitializeServer() *app.HTTPServer {
	wire.Build(
		// 基础层
		dao.NewUserDAO,
		service.NewUserService,

		// controller 层
		api.NewUserController,
		wire.Bind(new(api.Api), new(*api.UserController)),

		// slice 构造
		provideApis, // ✅ 返回 []api.Api

		// 注入到 HTTPServer
		app.NewHTTPServer,
	)
	return &app.HTTPServer{}
}
