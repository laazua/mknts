package common

import (
	// "github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

func LoadConfig(file string) *viper.Viper {
	v := viper.New()
	v.SetConfigFile(file)
	// 读取配置文件
	err := v.ReadInConfig()
	if err != nil {
		return nil
	}
	// 热加载配置
	// viper.WatchConfig()
	// viper.OnConfigChange(func(e fsnotify.Event) {
	// 	fmt.Println("Config file changed:", e.Name)
	// 	// 执行相应的操作

	// })

	return v
}
