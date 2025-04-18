// host api
package api

import (
	"vanGogh/pkg/caller/utils"

	"github.com/gin-gonic/gin"
)

func CGetHostInfo(ctx *gin.Context) {

	utils.Success(ctx, "get info success", nil)
}
