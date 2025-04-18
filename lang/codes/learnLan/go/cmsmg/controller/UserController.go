package controller

import (
	"cmsmanager/common"
	"cmsmanager/dto"
	"cmsmanager/model"
	"cmsmanager/response"
	"cmsmanager/utils"
	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
	"log"
	"net/http"
)

func Register(c *gin.Context) {
	// 获取参数
	DB := common.GetDB()
	username := c.PostForm("username")
	password := c.PostForm("password")
    log.Println(username, password)
	// 验证数据
	if len(username) == 0 || len(password) == 0 {
		response.Response(c, http.StatusUnprocessableEntity, 422, nil, "name or password can not be empty!")
		return
	}

	if len(password) < 6 {
		response.Response(c, http.StatusUnprocessableEntity, 422, nil, "password must be more than 6!")
		return
	}
	// 判断用户是否存在
	if utils.QueryName(DB, username){
		response.Response(c, http.StatusUnprocessableEntity, 422, nil, "name is used!")
		return
	}
	// 创建用户
	if hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost); err != nil {
		response.Response(c, http.StatusInternalServerError, 500, nil, "Password hashed error!")
		return
	} else {
		newUser := model.User{
			Username:     username,
			Password: string(hashedPassword),
		}
		DB.Create(&newUser)
	}

	// 返回结果
	log.Println(username, password)
	response.Success(c, nil, "register successful!")
}

func Login(c *gin.Context) {
	// 获取参数
	DB := common.GetDB()
	username := c.PostForm("username")
	password := c.PostForm("password")

	log.Println(username, password)
	// 验证数据
	if len(username) == 0 || len(password) == 0 {
		response.Response(c, http.StatusUnprocessableEntity, 422, nil, "username or password can not be empty!")
		return
	}
	var user model.User
	DB.Where("username = ?", username).First(&user)
	if user.ID == 0 {
		response.Response(c, http.StatusUnprocessableEntity, 422, nil,  "user is not in!")
		return
	}

	if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(password)); err != nil {
		response.Response(c, http.StatusUnauthorized, 400, nil, "Password error!")
		return
	}

	// 发放token
	token, err := common.ReleaseToken(user)
	if err != nil {
		response.Response(c, http.StatusInternalServerError, 500, nil, "token error")
		log.Printf("token generate error: %v", err)
		return
	}
    log.Println(token)
	response.Success(c, gin.H{"token": token}, "login successful!")
}

func Info(c *gin.Context) {
	user, _ := c.Get("user")
    response.Success(c, gin.H{"user":dto.ToUserDto(user.(model.User))},"user info successful!")

	// c.JSON(http.StatusOK, gin.H{
	//	"code": 200,
	//	"data": gin.H{
	//		"user": dto.ToUserDto(user.(model.User)),
	//	},
	//})
}