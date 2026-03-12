package middleware

import (
	"spoved-utils/xlog"

	"github.com/gin-gonic/gin"
)

func Recover() gin.HandlerFunc {
	return func(c *gin.Context) {
		defer func() {
			if err := recover(); err != nil {
				xlog.Errorf(
					"panic path=%s err=%v",
					c.Request.URL.Path,
					err,
				)
				c.AbortWithStatus(500)
			}
		}()
		c.Next()
	}
}
