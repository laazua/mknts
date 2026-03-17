package middleware

import (
	"time"

	"spoved-utils/xlog"

	"github.com/gin-gonic/gin"
)

func Logger() gin.HandlerFunc {

	return func(c *gin.Context) {

		start := time.Now()

		path := c.Request.URL.Path
		method := c.Request.Method
		clientIP := c.ClientIP()

		c.Next()

		latency := time.Since(start)

		status := c.Writer.Status()

		xlog.Info(
			"method=%s path=%s status=%d latency=%s ip=%s",
			method,
			path,
			status,
			latency,
			clientIP,
		)

		if len(c.Errors) > 0 {
			for _, e := range c.Errors {
				xlog.Error(
					"error path=%s err=%s",
					path,
					e.Error(),
				)
			}
		}
	}
}
