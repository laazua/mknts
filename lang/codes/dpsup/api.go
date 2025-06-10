package main

import (
	"encoding/json"
	"errors"
	"log/slog"
	"net/http"
)

/*---------------- 请求头序列化 ----------------*/
func bind(r *http.Request, v any) error {
	if r.Body == nil {
		return errors.New("request body is empty")
	}
	defer r.Body.Close()

	// 解码 JSON 数据
	decoder := json.NewDecoder(r.Body)
	err := decoder.Decode(v)
	if err != nil {
		return errors.New("failed to decode JSON")
	}
	return nil
}

/*----------------- 响应结构化 -----------------*/
type Map map[string]any

func success(w http.ResponseWriter, m Map) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	// 将 map 序列化为 JSON 并写入响应
	json.NewEncoder(w).Encode(m)
}

func failure(w http.ResponseWriter, m Map) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusBadRequest)

	// 将 map 序列化为 JSON 并写入响应
	json.NewEncoder(w).Encode(m)
}

// 请求体
type Process struct {
	Name    string `json:"name"`
	Command string `json:"command"`
	Number  int    `json:"number"`
}

type Pn struct {
	Name string `json:"name"`
}

/*--------------- 接口操作 ------------------*/
type Api struct {
	dp *Dp
}

func (api *Api) Create(w http.ResponseWriter, r *http.Request) {
	if !IpWhiteList(r) {
		logger.Info("你的IP地址不允许访问该服务")
		failure(w, Map{"code": http.StatusUnauthorized, "message": "你无权访问该服务"})
		return
	}
	var process Process
	if err := bind(r, &process); err != nil {
		logger.Error("创建队列失败,请求体参数绑定出错", slog.String("name", process.Name), slog.String("error", err.Error()))
		failure(w, Map{"code": http.StatusBadRequest, "message": "请求体参数绑定失败"})
		return
	}
	if !IsOsResourceOk() {
		logger.Info("系统资源不足, 不允许创建新的队列")
		failure(w, Map{"code": http.StatusServiceUnavailable, "message": "系统资源不足,不允许创建新的队列"})
		return
	}
	_, err := api.dp.Create(process)
	if err != nil {
		logger.Error("创建守护进程失败", slog.String("name", process.Name), slog.String("error", err.Error()))
		failure(w, Map{"code": http.StatusInternalServerError, "message": "创建守护进程失败"})
		return
	}
	logger.Info("创建守护进程成功", slog.String("name", process.Name))
	success(w, Map{"code": http.StatusOK, "message": "创建守护进程成功"})
}

func (api *Api) Delete(w http.ResponseWriter, r *http.Request) {
	if !IpWhiteList(r) {
		logger.Info("你的IP地址不允许访问该服务")
		failure(w, Map{"code": http.StatusUnauthorized, "message": "你无权访问该服务"})
		return
	}
	var pn Pn
	if err := bind(r, &pn); err != nil {
		logger.Error("移除守护进程失败,请求体参数绑定出错", slog.String("name", pn.Name), slog.String("error", err.Error()))
		failure(w, Map{"code": http.StatusBadRequest, "message": "请全体参数绑定失败"})
		return
	}
	if err := api.dp.Delete(pn.Name); err != nil {
		logger.Error("移除队列配置失败", slog.String("name", pn.Name), slog.String("error", err.Error()))
		failure(w, Map{"code": http.StatusInternalServerError, "message": "删除队列失败"})
		return
	}
	logger.Info("删除队列成功", slog.String("name", pn.Name))
	success(w, Map{"code": http.StatusOK, "message": "删除队列成功"})
}
