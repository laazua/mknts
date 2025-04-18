package common

import (
	"cmsmanager/model"
	"github.com/gin-gonic/gin"
	"net/http"
	"strings"
)

func AuthMiddleWare() gin.HandlerFunc{
	return func(c *gin.Context){
		// 获取authorization header
		tokenString := c.GetHeader("Authorization")

		// validate token format
		if tokenString == "" || !strings.HasPrefix(tokenString, "Bearer") {
			c.JSON(http.StatusUnauthorized, gin.H{
				"code": 401,
				"message": "权限不足！",
			})
			c.Abort()
			return
		}
		tokenString = tokenString[7:]

		token, claims, err := ParseToken(tokenString)
		if err != nil || !token.Valid {
			c.JSON(http.StatusUnauthorized, gin.H{
				"code": 401,
				"message": "权限不足!",
			})
			return
		}

		// 验证通过获取claims中的userId
		userId := claims.UserID
		DB := GetDB()
		var user model.User
		DB.First(&user, userId)

		// user not in
		if user.ID == 0 {
			c.JSON(http.StatusUnauthorized, gin.H{
				"code": 401,
				"message": "权限不足",
			})
			c.Abort()
			return
		}

		// user in, write user info into context
		c.Set("user", user)
		c.Next()
	}
}
