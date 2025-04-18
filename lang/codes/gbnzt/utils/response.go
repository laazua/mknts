package utils

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Resp interface {
	Success(c *gin.Context, data interface{}, msg string)
	Failed(c *gin.Context, data interface{}, msg string)
}

func NewResp() Resp {
	return &resp{}
}

type resp struct{}

// 前端返回结果
func (resp) Ret(c *gin.Context, status, code int, data interface{}, msg string) {
	c.JSON(status, gin.H{"code": code, "data": data, "message": msg})
}

// 前端返回成功结果
func (r resp) Success(c *gin.Context, data interface{}, msg string) {
	r.Ret(c, http.StatusOK, 200, data, msg)
}

// 前端返回失败结果
func (r resp) Failed(c *gin.Context, data interface{}, msg string) {
	r.Ret(c, http.StatusBadRequest, 400, data, msg)
}
