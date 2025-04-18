package api

import (
	"vanGogh/pkg/caller/utils"

	"github.com/gin-gonic/gin"
)

func SGetHostInfo(ctx *gin.Context) {

	utils.Success(ctx, "get host info success", nil)
}
