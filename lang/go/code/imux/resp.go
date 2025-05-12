package imux

import (
	"encoding/json"
	"net/http"
)

type Map map[string]any

func Success(w http.ResponseWriter, m Map) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	// 将 map 序列化为 JSON 并写入响应
	if err := json.NewEncoder(w).Encode(m); err != nil {
		panic(err)
	}
}

func Failure(w http.ResponseWriter, m Map) {
	// 设置响应头为 JSON 格式
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusInternalServerError)

	// 将 map 序列化为 JSON 并写入响应
	if err := json.NewEncoder(w).Encode(m); err != nil {
		panic(err)
	}
}

func NotFound(w http.ResponseWriter, m Map) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNotFound)

	if err := json.NewEncoder(w).Encode(m); err != nil {
		panic(err)
	}
}

func BadRequest(w http.ResponseWriter, m Map) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusBadRequest)

	if err := json.NewEncoder(w).Encode(m); err != nil {
		panic(err)
	}
}
