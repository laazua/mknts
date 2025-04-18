package controller

import (
	"encoding/json"
	"net/http"
)

type object map[string]any

func success(w http.ResponseWriter, obj object) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	// 将 map 序列化为 JSON 并写入响应
	json.NewEncoder(w).Encode(obj)
}

func failure(w http.ResponseWriter, obj object) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusBadRequest)

	// 将 map 序列化为 JSON 并写入响应
	json.NewEncoder(w).Encode(obj)
}
