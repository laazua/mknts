package main

import (
	"fmt"
	"log"
	"log/slog"
	"net/http"

	"gokins/pkg/api"
	"gokins/pkg/core"
	_ "gokins/statik"

	"github.com/rakyll/statik/fs"
)

func main() {
	muxServe := api.NewMuxServe()
	server := http.Server{
		Addr:    core.Setting.Address,
		Handler: muxServe,
	}

	/////////////statik嵌入静态文件////////////
	// 创建文件系统
	statikFS, err := fs.New()
	if err != nil {
		log.Fatal(err)
	}
	// 设置文件服务器
	muxServe.Handle("GET /", http.FileServer(statikFS))

	slog.Info(
		fmt.Sprintf("## 启动服务并监听: [%v]", core.Setting.Address))

	if err := server.ListenAndServe(); err != nil {
		panic(fmt.Sprintf("## 启动服务失败: %v", err))
	}
}
