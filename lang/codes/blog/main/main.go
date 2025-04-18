package main

import (
	"app"
	"env"
)

func main() {
	// 加载配置
	env.Load()

	application := app.New()
	if err := application.Run(); err != nil {
		panic(err)
	}
}
