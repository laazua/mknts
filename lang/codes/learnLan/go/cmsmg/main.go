package main

import (
	"cmsmanager/common"
	"cmsmanager/routers"
	"cmsmanager/utils"
	"github.com/spf13/viper"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	utils.InitConfig()
	db := common.GetDB()
	defer db.Close()

	r := routers.GetRouters()

	if port := viper.GetString("server.port"); port != "" {
		panic(r.Run(":" + port))
	}
}


