package mwire

import "show/internal/api"

func provideApis(
	user api.Api,
	// 这里可以继续添加 role, menu 等 controller
) []api.Api {
	return []api.Api{user}
}
