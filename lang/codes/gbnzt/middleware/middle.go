package middleware

import (
	"bnzt/global"
	"bnzt/utils"
	"net/http"
	"strings"

	"github.com/chenhg5/collection"
	"github.com/gin-gonic/gin"
)

type Middleware interface {
	JwtAuth() gin.HandlerFunc
	IpWhite() gin.HandlerFunc
	Cors() gin.HandlerFunc
}

func NewMiddleware() Middleware {
	return &middle{}
}

type middle struct{}

// jwt
func (m *middle) JwtAuth() gin.HandlerFunc {
	return func(c *gin.Context) {
		token := c.Request.Header.Get("token")
		if token == "" {
			c.JSON(http.StatusOK, gin.H{
				"message": "token为空",
			})
			c.Abort()
			return
		}
		t := utils.NewToken()
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

// ip白名单放行
func (m *middle) IpWhite() gin.HandlerFunc {
	return func(c *gin.Context) {
		index := strings.Index(c.Request.RemoteAddr, ":")
		ip := c.Request.RemoteAddr[:index]
		if isIn := collection.Collect(global.AppCon.GetStringSlice("app.whiteip")).Contains(ip); !isIn {
			c.JSON(http.StatusOK, gin.H{
				"message": "您的ip禁止访问该应用!",
			})
			c.Abort()
			return
		}
		c.Next()
	}
}

// 跨域
func (m *middle) Cors() gin.HandlerFunc {
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
