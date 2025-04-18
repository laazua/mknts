package middleware

import (
	"fmt"
	"msbn/global"
	"msbn/utils"
	"strings"
	"time"

	"github.com/chenhg5/collection"
	"github.com/gin-gonic/gin"
)

// ip白名单放行
func IpWhite() gin.HandlerFunc {
	return func(c *gin.Context) {
		index := strings.Index(c.Request.RemoteAddr, ":")
		clientIp := c.Request.RemoteAddr[:index]
		if !collection.Collect(global.AppCon.GetStringSlice("app.whiteip")).Contains(clientIp) {
			c.JSON(200, gin.H{
				"message": "您的ip禁止访问该应用!",
				"data":    nil,
			})
			c.Abort()
			return
		}
		c.Next()
	}
}

// jwt解析
func JwtAuth() gin.HandlerFunc {
	return func(c *gin.Context) {
		token := c.Request.Header.Get("token")
		if token == "" {
			c.JSON(200, gin.H{
				"message": "token为空!",
				"token":   nil,
			})
			c.Abort()
			return
		}

		if claims, err := utils.ParseToken(token); err != nil {
			c.JSON(200, gin.H{
				"message": "登录失效,请重新登录!",
				"token":   nil,
			})
			c.Abort()
			return
		} else {
			c.Set("username", claims.UserName)
			c.Next()
		}
	}
}

var T int64 = 0

// 接口重复请求拦截
func ReSubmit() gin.HandlerFunc {
	return func(c *gin.Context) {
		if T == 0 {
			T = time.Now().Unix()
			c.Next()
		} else {
			if time.Now().Unix()-T < 5 {
				T = time.Now().Unix()
				fmt.Println("5s后再请求该接口")
				c.JSON(200, gin.H{
					"message": "5s后再请求该接口",
					"code":    400,
				})
				return
			} else {
				T = time.Now().Unix()
				c.Next()
			}
		}
	}
}
