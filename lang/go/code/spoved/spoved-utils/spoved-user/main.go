package main

import (
	"flag"
	"os"
	"spoved-user/internal/app"
	"spoved-utils/config"
)

var configPath string

func init() {
	if err := argFlag(); err != nil {
		println("配置文件不存在")
		os.Exit(-1)
	}
	// 加载配置
	if err := config.InitConfig(configPath); err != nil {
		// return nil, errors.New("加载配置文件失败: " + err.Error())
		panic(err)
	}
}

func main() {
	// 启动应用
	app, err := app.New()
	if err != nil {
		panic(err)
	}
	if err := app.Run(); err != nil {
		panic(err)
	}
}

func argFlag() error {
	// 解析命令行参数
	flag.StringVar(&configPath, "config", "config.yaml", "配置文件")
	flag.Parse()

	// 检测配置文件是否存在
	if _, err := os.Stat(configPath); os.IsNotExist(err) {
		return err
	}
	return nil
}
