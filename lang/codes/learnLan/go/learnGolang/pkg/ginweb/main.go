// go mod init ginweb
package main

import (
	"ginweb/router"
)

func main() {

	// config.InitConfig()

	r := router.SetupRouter()
	r.Run(":8000")
	// if port := viper.GetString("server.port"); port != "" {
	//	panic(r.Run(":" + port))
	//}
}
