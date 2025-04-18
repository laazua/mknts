package api

import (
	"fmt"
	"gweb/pkg/api/route"
	"gweb/pkg/utils"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"
)

func RunService() {
	// 加载css,js相关静态文件
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	// 系统相关的接口
	http.HandleFunc("/system/index", route.Index)
	http.HandleFunc("/system/dashboard", route.DashBoard)
	// 用户相关的接口
	http.HandleFunc("/user/login", route.Login)
	http.HandleFunc("/user/add", route.AddUser)
	// 运维相关的接口
	http.HandleFunc("/ops/man", route.ManZone)

	// http参数设置
	fmt.Printf("http server start on: %s:%d\n", utils.AppCon.App.Ip, utils.AppCon.App.Port)
	address := fmt.Sprintf("%s:%d", utils.AppCon.App.Ip, utils.AppCon.App.Port)
	server := &http.Server{
		Addr:         address,
		ReadTimeout:  time.Second * 1,
		WriteTimeout: time.Second * 1,
		Handler:      nil,
	}
	// 注册关闭信号
	quit := make(chan os.Signal)
	signal.Notify(quit, os.Interrupt)
	// 监听信号
	go func() {
		<-quit
		if err := server.Close(); err != nil {
			log.Println("close server: ", err)
		}
	}()
	// 启动服务
	server.ListenAndServe()
}
