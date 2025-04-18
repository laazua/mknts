package global

import (
	"log"

	"github.com/spf13/viper"
)

var AppCon *viper.Viper

func init() {
	AppCon = loadCon()
}

// 加载配置
func loadCon() *viper.Viper {
	con := viper.New()
	con.SetConfigName("app")
	con.SetConfigType("yaml")
	con.AddConfigPath("config/")
	con.Set("verbose", true)

	if err := con.ReadInConfig(); err != nil {
		panic(err)
	}
	con.WatchConfig()
	log.Println("配置文件加载成功!")
	return con
}
