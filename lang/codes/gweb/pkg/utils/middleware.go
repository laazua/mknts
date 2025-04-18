package utils

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func JwtAuth() gin.HandlerFunc {
	return func(c *gin.Context) {
		token := c.Request.Header.Get("token")
		if token == "" {
			c.JSON(http.StatusOK, gin.H{
				"message": "token为空",
			})
			c.Abort()
			return
		}
		t := NewToken()
		if claims, err := t.Parse(token); err != nil {
			c.JSON(http.StatusOK, gin.H{
				"message": "TOKEN已经过期",
			})
			c.Abort()
			return
		} else {
			c.Set("name", claims.Username)
			c.Next()
		}
	}
}

func Cors() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Header("Access-Control-Allow-Origin", c.Request.Header.Get("Origin"))
		c.Header("Access-Control-Allow-Credentials", "true")
		c.Header("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
		c.Header("Access-Control-Allow-Methods", "GET,POST,PUT,PATCH,DELETE,OPTIONS")

		// 过滤OPTIONS和HEAD请求
		if c.Request.Method == "OPTIONS" || c.Request.Method == "HEAD" {
			c.AbortWithStatus(204)
			return
		}
		c.Next()
	}
}
