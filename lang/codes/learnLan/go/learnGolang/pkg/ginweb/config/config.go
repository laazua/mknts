package config

import (
	"fmt"
	"os"

	"github.com/spf13/viper"
)

func InitConfig() {
	dir, err := os.Getwd()
	if err != nil {
		panic("Get config dir error!")
	}

	viper.SetConfigName("app")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(dir)
	fmt.Println(dir)
	if err := viper.ReadInConfig(); err != nil {
		panic("Read config file error!")
	}
}
