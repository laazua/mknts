package controller

import (
	"ginweb/common"
	"ginweb/db"

	"github.com/gin-gonic/gin"
)

// GET        uri传参
// POST       form body或者uri中传参
// DELETE     uri body中传参
// PUT        form body或者uri中传参

// uri对应路径参数
// form对应表单参数
// body对应json参数

func Login(c *gin.Context) {
	var user db.Users
	username := c.PostForm("username") // multipart/form-data
	password := c.PostForm("password") // multipart/form-data

	token, _ := common.EnCodeToken(user)
	// query database
	if db.QueryUser(username, common.HashPassword(password)) {
		c.JSON(200, gin.H{
			"message": "login successful.",
			"token":   token,
		})
		return
	} else {
		c.JSON(401, gin.H{
			"message": "username or password error.",
		})
	}

}

func Register(c *gin.Context) {
	username := c.PostForm("username")
	password := c.PostForm("password")
	role := c.PostForm("role")

	hashPassword := common.HashPassword(password)

	// query database
	if db.QueryUser(username, hashPassword) {
		c.JSON(401, gin.H{
			"message": "User already exist.",
		})
		return
	}

	if db.AddUser(username, hashPassword, role) {
		c.JSON(200, gin.H{
			"message": "Register successful.",
		})
	} else {
		c.JSON(401, gin.H{
			"message": "Register failed.",
		})
		return
	}
}

func DeleteUser(c *gin.Context) {
	username := c.PostForm("username")
	password := c.PostForm("password")

	// delete user
	if db.DelUser(username, common.HashPassword(password)) {
		c.JSON(200, gin.H{
			"message": "delete user successful.",
		})
	} else {
		c.JSON(401, gin.H{
			"message": "delete user failed.",
		})
	}
}

func ChangePassword(c *gin.Context) {
	username := c.PostForm("username")
	password := c.PostForm("password")
	newPassword := c.PostForm("newPassword")

	if db.ChangePwd(username, common.HashPassword(password), common.HashPassword(newPassword)) {
		c.JSON(200, gin.H{
			"message": "Change password successful.",
		})
	} else {
		c.JSON(401, gin.H{
			"message": "Change password failed.",
		})
	}
}

// 用户信息
func UserInfo(c *gin.Context) {
	// 通过token获取用户的详细信息，返回给浏览器并分配相应的权限.
}
