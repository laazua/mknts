package utils

import (
	"cmsmanager/model"
	"github.com/jinzhu/gorm"
	"github.com/spf13/viper"
	"os"
)

func QueryName(db *gorm.DB, name string) bool {
	var user model.User
	db.Where("username = ?", name).First(&user)
	if user.ID != 0 {
		return true
	}
	return false
}

func InitConfig() {
	workDir, _ := os.Getwd()
	viper.SetConfigName("cmsmg")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(workDir + "/config")

	if err := viper.ReadInConfig(); err !=nil {
		panic("read config error")
		return
	}
}
