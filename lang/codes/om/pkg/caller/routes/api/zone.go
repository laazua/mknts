// zone api
package api

import (
	"vanGogh/pkg/caller/utils"

	"github.com/gin-gonic/gin"
)

// add zone
func CAddZone(ctx *gin.Context) {

	utils.Success(ctx, "add zone success", nil)
}

// operate zone
func CPutZone(ctx *gin.Context) {

	utils.Success(ctx, "opt zone success", nil)
}

// get zone list
func CGetZone(ctx *gin.Context) {

	utils.Success(ctx, "get zone success", nil)
}
