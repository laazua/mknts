package api

import (
	"manage/internal/master/core"

	"github.com/gin-gonic/gin"
)

type apiUser struct {
	core.LoginModel
}

func newApiUser() *apiUser {
	return &apiUser{}
}

func (au *apiUser) login(ctx *gin.Context) {}

func (au *apiUser) add(ctx *gin.Context) {}

func (au *apiUser) delete(ctx *gin.Context) {}

func (au *apiUser) modify(ctx *gin.Context) {}

func (au *apiUser) query(ctx *gin.Context) {}

func (au *apiUser) logout(ctx *gin.Context) {}
