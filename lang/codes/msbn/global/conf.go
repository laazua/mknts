package global

import (
	"github.com/spf13/viper"
)

var AppCon *viper.Viper

func init() {
	AppCon = loadCon()
}

func loadCon() *viper.Viper {
	vp := viper.New()
	vp.SetConfigName("app")
	vp.SetConfigType("yaml")
	vp.AddConfigPath("config/")
	vp.Set("verbose", true)

	if err := vp.ReadInConfig(); err != nil {
		panic(err)
	}
	vp.WatchConfig()

	return vp
}
