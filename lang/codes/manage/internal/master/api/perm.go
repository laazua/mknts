package api

import "github.com/gin-gonic/gin"

type apiPerm struct{}

func newApiPerm() *apiPerm {
	return &apiPerm{}
}

func (ap *apiPerm) add(ctx *gin.Context) {}

func (ap *apiPerm) delete(ctx *gin.Context) {}

func (ap *apiPerm) modify(ctx *gin.Context) {}

func (ap *apiPerm) query(ctx *gin.Context) {}
