package main

import (
	"stdhttp/pkg/app"
	"stdhttp/pkg/env"
)

func main() {
	// 加载配置
	env.LoadEnvFile(".env")

	app := app.NewApp()
	if err := app.Run(); err != nil {
		panic(err)
	}
}
