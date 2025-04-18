// 中间件
package common

import (
	"github.com/gin-gonic/gin"
)

func AllowIp() gin.HandlerFunc {
	ALLOW_IP := []string{"127.0.0.1", "192.168.30.123"} // 写在配置文件中
	return func(c *gin.Context) {
		for _, ip := range ALLOW_IP {
			if ip != c.ClientIP() {
				c.JSON(200, gin.H{
					"message": "ip not allow visit.",
				})
				c.Abort()
			}
			c.Next()
		}
	}
}
