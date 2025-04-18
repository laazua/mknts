package utils

import (
	"log/slog"

	"github.com/spf13/viper"
)

func LoadConfig(name string) {
	// 设置Viper配置文件名称和路径
	// viper.SetConfigName("server")
	// viper.SetConfigType("yaml")
	// viper.AddConfigPath("config")
	viper.SetConfigFile(name)

	// 读取配置文件
	if err := viper.ReadInConfig(); err != nil {
		panic(err)
	}
	slog.Info("加载配置文件成功!")
}
