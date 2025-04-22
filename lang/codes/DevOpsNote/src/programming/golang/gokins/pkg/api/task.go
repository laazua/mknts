package api

import (
	"fmt"
	"log/slog"
	"net/http"

	"gokins/pkg/core"
	"gokins/pkg/service"
)

const WebHookPasswd = "xadfadfad"

func addTask(w http.ResponseWriter, r *http.Request) {
	slog.Info("## 添加打包任务")
	ctx := &core.Context{Writer: w, Request: r}
	// println(r.RemoteAddr)

	ctx.JSON(200, core.H{"msg": "添加任务成功"})
}

func runTask(w http.ResponseWriter, r *http.Request) {
	name := r.Context().Value("name").(string)
	slog.Info(fmt.Sprintf("运行打包任务: %v", name))
	// 加上gitee的头部认证
	ctx := &core.Context{Writer: w, Request: r}
	providePasswd := ctx.Request.Header.Get("X-Gitee-Token")
	if providePasswd != WebHookPasswd {
		ctx.JSON(http.StatusUnauthorized, core.H{"message": "Unauthorized"})
		return
	}

	if err := service.ParseTask(fmt.Sprintf("%v/%v.yaml", core.Setting.TaskPath, name)); err != nil {
		ctx.JSON(400, core.H{"msg": "运行任务失败"})
		return
	}

	ctx.JSON(200, core.H{"msg": "运行任务成功"})
}
