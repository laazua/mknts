package api

import (
	"vanGogh/pkg/caller/utils"

	"github.com/gin-gonic/gin"
)

func SAddZone(ctx *gin.Context) {

	utils.Success(ctx, "add zone success", nil)
}

func SOptZone(ctx *gin.Context) {

	utils.Success(ctx, "operate zone success", nil)
}
