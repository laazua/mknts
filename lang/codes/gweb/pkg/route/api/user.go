package api

import (
	"fmt"
	"gweb/pkg/dto"
	"gweb/pkg/utils"

	"github.com/gin-gonic/gin"
)

type UserApi struct {
	UserLoginParam UserSignIn
}

func NewUserApi() *UserApi { return &UserApi{} }

func (u *UserApi) Login(c *gin.Context) {
	// 实例化http响应对象
	resp := utils.NewResp(c)
	if err := c.BindJSON(&u.UserLoginParam); err != nil {
		resp.Failed("get login user param error", err)
		return
	}
	if !dto.NewUserDto(u.UserLoginParam.Username, u.UserLoginParam.Password).CheckUser() {
		resp.Failed("username or password error", nil)
		return
	}
	if token, err := utils.NewToken().Create(u.UserLoginParam.Username); err != nil {
		resp.Failed("create token error", err)
		return
	} else {
		resp.Success("sign in success", token)
	}
}

func (u *UserApi) Add(c *gin.Context) {
	resp := utils.NewResp(c)
	if err := c.BindJSON(&u.UserLoginParam); err != nil {
		resp.Failed("get add user param error", err)
		return
	}
	if !dto.NewUserDto(u.UserLoginParam.Username, u.UserLoginParam.Password).AddUser() {
		resp.Failed("insert user to database error", nil)
		return
	}
	resp.Success("insert user to database success", nil)
}

func (u *UserApi) Del(c *gin.Context) {
	resp := utils.NewResp(c)
	name := c.Query("username")
	fmt.Println("xxx", name)
	if !dto.NewUserDto(name, "").DeleteUser() {
		resp.Failed("delete user from database error", nil)
		return
	}
	resp.Success("delete user from database success", name)
}

func (u *UserApi) Get(c *gin.Context) {
	resp := utils.NewResp(c)
	if result, err := dto.NewUserDto("", "").GetUser(); err != nil {
		resp.Failed("get user from database error", err)
	} else {
		resp.Success("get user from database success", result)
	}
}
