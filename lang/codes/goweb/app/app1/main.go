package main

import (
	"gweb/pkg/api"
	"gweb/pkg/utils"
)

func main() {
	// 加载配置
	utils.LoadCon("app1")
	// 加载mysql
	utils.LoadMysql()
	// 启动web服务
	api.RunService()
}
