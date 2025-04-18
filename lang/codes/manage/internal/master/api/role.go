package api

import "github.com/gin-gonic/gin"

type apiRole struct{}

func newApiRole() *apiRole {
	return &apiRole{}
}

func (ao *apiRole) add(ctx *gin.Context) {}

func (ao *apiRole) delete(ctx *gin.Context) {}

func (ao *apiRole) modify(ctx *gin.Context) {}

func (ao *apiRole) query(ctx *gin.Context) {}
