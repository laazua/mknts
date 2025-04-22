package main

import (
	"gin-vue-admin/api"
	"gin-vue-admin/utils"
)

func main() {

	route := api.NewRoute()

	route.Run(utils.GetEnv("ADDRESS"))
}
