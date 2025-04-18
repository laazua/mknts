package utils

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Resp struct {
	Ctx *gin.Context
}

func NewResp(c *gin.Context) *Resp {
	return &Resp{
		Ctx: c,
	}
}

func (r *Resp) ret(status, code int, msg string, data interface{}) {
	r.Ctx.JSON(status, gin.H{"code": code, "data": data, "message": msg})
}

func (r *Resp) Success(msg string, data interface{}) {
	r.ret(http.StatusOK, 200, msg, data)
}

func (r *Resp) Failed(msg string, data interface{}) {
	r.ret(http.StatusBadRequest, 400, msg, data)
}
