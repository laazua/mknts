package main

import (
	"msite/pkg/app"
	"msite/pkg/env"
)

func main() {
	// 加载配置
	env.LoadEnv(".env")
	// 加载数据库
	// storage.LoadSql()

	app := app.NewApp()
	if err := app.Run(); err != nil {
		panic(err)
	}
}
