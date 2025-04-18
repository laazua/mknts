// some middleware
package utils

import (
	"github.com/gin-gonic/gin"
)

func JwtAuth() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		token := ctx.Request.Header.Get("token")
		if token == "" {
			Success(ctx, "token is nil", nil)
			ctx.Abort()
			return
		}
		ctx.Next()
	}
}

func WhiteIps() gin.HandlerFunc {
	return func(ctx *gin.Context) {

		ctx.Next()
	}
}

func WhitePath() gin.HandlerFunc {
	return func(ctx *gin.Context) {

		ctx.Next()
	}
}

func GlobleMiddleware() []gin.HandlerFunc {
	mwSlice := make([]gin.HandlerFunc, 3)
	mwSlice = append(mwSlice, gin.Logger(), gin.Recovery())
	return mwSlice
}
