package utils

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type RespData struct {
	Code int         `json:"code"`
	Data interface{} `json:"data"`
}

func ret(w http.ResponseWriter, code int, data any) {
	wData := fmt.Sprintf(`{"code": %d, "data": %v}`, code, data)
	w.Header().Set("content-type", "application/json")
	jsonData, _ := json.Marshal(RespData{Code: code, Data: wData})
	w.Write(jsonData)

}

// func Success(w http.ResponseWriter, data any) {
// 	ret(w, 200, data, msg)
// }

// func Failed(w http.ResponseWriter, data any) {
// 	ret(w, 400, data, msg)
// }

func HttpRespse(w http.ResponseWriter, data any) {
	ret(w, http.StatusOK, data)
}
