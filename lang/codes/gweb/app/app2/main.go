package main

import "gweb/pkg/utils"

func main() {
	// 加载配置
	utils.LoadCon("app2")
	// 启动tcp服务
	utils.NewServe().Start()
}
