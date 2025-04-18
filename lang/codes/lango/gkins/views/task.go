package views

import (
	"net/http"
)

// Dashboard 渲染主页
func Dashboard(w http.ResponseWriter, r *http.Request) {
	renderTemplate(w, "dashboard", nil)
}

// CreateTask 新增任务
func CreateTask(w http.ResponseWriter, r *http.Request) {}

// DeleteTask 删除任务
func DeleteTask(w http.ResponseWriter, r *http.Request) {}

// UpdateTask 更新任务
func UpdateTask(w http.ResponseWriter, r *http.Request) {}

// QueryTask 查询任务
func QueryTask(w http.ResponseWriter, r *http.Request) {}

// TaskList 任务列表
func TaskList(w http.ResponseWriter, r *http.Request) {
	renderTemplate(w, "task", nil)
}

// ManualRunTask 手动运行任务
func ManualRunTask(w http.ResponseWriter, r *http.Request) {}

// WebhookRunTask webhook触发运行任务
func WebhookRunTask(w http.ResponseWriter, r *http.Request) {}
