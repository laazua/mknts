package main

import (
	"fmt"
	"msbn/global"
	api "msbn/routers"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	/* 启动守护进程 */
	// utils.StartApp()
	r := api.GetRouter()
	/* 启动程序 */
	r.Run(fmt.Sprintf("%s:%s", global.AppCon.GetString("app.addr"),
		global.AppCon.GetString("app.port")))
}
