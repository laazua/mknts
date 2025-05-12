package api

import (
	"errors"
	"net/http"
	"strconv"

	"scheduletasks/core"

	"github.com/gin-gonic/gin"
	"github.com/robfig/cron/v3"
)

func AddTask(ctx *gin.Context) {
	var payLoad struct {
		Cron    string `json:"cron"`
		Command string `json:"command"`
	}
	if err := ctx.ShouldBindBodyWithJSON(&payLoad); err != nil {
		ctx.JSON(500, gin.H{"code": 500, "msg": errors.New("绑定参数失败").Error()})
		return
	}
	id, err := core.Cron.AddFunc(payLoad.Cron, func() {
		core.ExecuteTask(payLoad.Command)
	})
	if err != nil {
		ctx.JSON(500, gin.H{"code": 500, "msg": errors.New("添加任务失败").Error()})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "添加任务成功", "taskId": id})
}

func GetTask(ctx *gin.Context) {
	var results []map[string]any
	for _, task := range core.Cron.Entries() {
		results = append(results, map[string]any{
			"id":   task.ID,
			"next": task.Next,
		})
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "获取任务成功", "tasks": results})
}

func DelTask(ctx *gin.Context) {
	id := ctx.Param("id")
	eid, err := strconv.Atoi(id)
	if err != nil {
		ctx.AbortWithStatus(http.StatusBadRequest)
		return
	}
	// remove cron job
	core.Cron.Remove(cron.EntryID(eid))
	ctx.JSON(200, gin.H{"code": 200, "msg": "移除成功"})
}
