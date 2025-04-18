package api

import (
	"fmt"
	"log/slog"
	"net/http"
	"strconv"

	"gookins/core"
	"gookins/model"
	"gookins/service"

	"github.com/gin-gonic/gin"
)

// @Summary 创建任务
// @Description 任务创建接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param task body model.TaskForm true "创建任务请求参数"
// @Success 200 {object} model.ApiRespone "创建任务成功"
// @Failure 500 {object} model.ApiRespone "创建任务失败"
// @Router /task/add [post]
func CreateTask(ctx *gin.Context) {
	var taskForm model.TaskForm
	if err := ctx.ShouldBindJSON(&taskForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	if err := service.CreateTask(taskForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "创建任务成功"})
}

// @Summary 删除任务
// @Description 任务删除接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param id path string true "id"
// @Success 200 {object} model.ApiRespone "删除任务成功"
// @Failure 500 {object} model.ApiRespone "删除任务失败"
// @Router /task/del/{id} [delete]
func DeleteTask(ctx *gin.Context) {
	idStr := ctx.Param("id")
	id, err := strconv.ParseUint(idStr, 10, 0) // 将字符串转换为 uint64
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	if err := service.DeleteTask(id); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "删除任务成功"})
}

// @Summary 更新任务
// @Description 任务更新接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param task body model.TaskForm true "更新任务请求参数"
// @Success 200 {object} model.ApiRespone "更新任务成功"
// @Failure 500 {object} model.ApiRespone "更新任务失败"
// @Router /task/upt/{id} [put]
func UpdateTask(ctx *gin.Context) {
	var taskForm model.TaskForm
	if err := ctx.ShouldBindJSON(&taskForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
	}
	if err := service.UpdateTask(taskForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "更新任务成功"})
}

// @Summary 任务列表
// @Description 任务列表接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Success 200 {object} model.ApiRespone "获取任务成功"
// @Failure 500 {object} model.ApiRespone "获取任务失败"
// @Router /task/list [get]
func TaskLists(ctx *gin.Context) {
	tasks, err := service.TaskLists()
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "获取任务列表成功", Data: tasks})
}

// @Summary 运行任务
// @Description 运行任务接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param task body model.TaskForm true "添加务请求参数"
// @Success 200 {object} model.ApiRespone "添加任务到任务池成功"
// @Failure 500 {object} model.ApiRespone "添加任务到任务池失败"
// @Router /task/run [post]
func RunTask(ctx *gin.Context) {
	var taskForm model.TaskForm
	if err := ctx.ShouldBindJSON(&taskForm); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	job := &core.TaskJob{
		Id:       taskForm.Id,
		Name:     taskForm.Name,
		PipeLine: taskForm.PipeLine,
	}
	if err := core.Tp.AddTask(job); err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "任务加入任务池成功"})
}

// @Summary hook运行任务
// @Description hook运行任务接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param task body model.TaskForm true "hook添加任务请求参数"
// @Success 200 {object} model.ApiRespone "hook添加任务到任务池成功"
// @Failure 401 {object} model.ApiRespone "hook添加任务到任务池失败"
// @Router /task/hook [post]
func TaskHook(ctx *gin.Context) {
	// 代码仓库回调接口
}

// @Summary 取消任务
// @Description 任务取消接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param name path string true "name"
// @Success 200 {object} model.ApiRespone "取消任务成功"
// @Failure 500 {object} model.ApiRespone "取消任务失败"
// @Router /task/cancel/{name} [post]
func CancelTask(ctx *gin.Context) {
	name := ctx.Param("name")
	if !core.Tp.CancelTask(name) {
		slog.Error("取消任务失败")
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: "取消任务失败"})
		return
	}
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "取消任务成功"})
}

// @Summary 任务状态
// @Description 任务状态接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param name path string true "name"
// @Success 200 {object} model.ApiRespone "获取任务状态成功"
// @Failure 401 {object} model.ApiRespone "获取任务状态失败"
// @Router /task/state/{name} [get]
func TaskStatus(ctx *gin.Context) {
	name := ctx.Param("name")
	status, exists := core.Tp.GetTaskStatus(name)
	if !exists {
		slog.Error("任务不存在")
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: "任务不存在"})
		return
	}
	fmt.Println("status: ", status)
	ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "获取任务状态成功", Data: status})
}

// @Summary 禁用任务
// @Description 任务禁用接口
// @Security ApiKeyAuth
// @Tags 任务
// @Accept json
// @Produce json
// @Param name path string true "name"
// @Success 200 {object} model.ApiRespone "取消任务成功"
// @Failure 500 {object} model.ApiRespone "取消任务失败"
// @Router /task/cancel/{name} [post]
func TaskDisabled(ctx *gin.Context) {
	name := ctx.Param("name")
	tasks, err := service.TaskLists()
	if err != nil {
		slog.Error(err.Error())
		ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 500, Message: err.Error()})
		return
	}
	for _, task := range tasks {
		if task.Name == name {
			service.TaskDisable(name, !task.Disabled)
			ctx.JSON(http.StatusOK, model.ApiRespone{Code: 200, Message: "任务禁用成功"})
			return
		}
	}
	ctx.JSON(http.StatusInternalServerError, model.ApiRespone{Code: 400, Message: "未找到任务"})
}
