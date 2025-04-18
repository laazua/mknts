package global

import (
	"github.com/spf13/viper"
)

var AppCon *viper.Viper

func init() {
	con := viper.New()
	con.SetConfigName("app")
	con.SetConfigType("yaml")
	con.AddConfigPath("config/")
	con.Set("verbose", true)
	if err := con.ReadInConfig(); err != nil {
		panic(err)
	}
	con.WatchConfig()
	AppCon = con
	// log.Println("配置文件加载成功!")
}
