package api

import (
	"log"
	"v2man/storage/model"
	"v2man/storage/service"

	"github.com/gin-gonic/gin"
)

type UserApi struct {
	UserService *service.UserService
}

func NewUserApi(userService *service.UserService) *UserApi {
	return &UserApi{UserService: userService}
}

func (u *UserApi) Login(ctx *gin.Context) {
	var user model.LoginRequest
	if err := ctx.ShouldBindJSON(&user); err != nil {
		log.Fatalf("Bind LoginRequest Model Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Bind LoginRequest Model Error"})
		return
	}
	if err := u.UserService.Auth(user); err != nil {
		log.Fatalf("User Auth Error: %v\n", err)
		ctx.JSON(400, gin.H{"code": 400, "msg": "User Auth Error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "Login Success"})
}

func (u *UserApi) Add(ctx *gin.Context) {
	var user model.User
	if err := ctx.ShouldBindJSON(&user); err != nil {
		log.Fatalf("Bind User Model Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Bind User Model Error"})
		return
	}
	if err := u.UserService.Add(user); err != nil {
		log.Fatalf("User Add To Db Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "User Add To Db Error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "Add User Success"})
}

func (u *UserApi) Delete(ctx *gin.Context) {
	name := ctx.Param("name")
	if err := u.UserService.Delete(name); err != nil {
		log.Fatalf("Delete User From Db Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Delete User From Db Error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "Delete User Success"})
}

func (u *UserApi) Update(ctx *gin.Context) {
	var user model.User
	if err := ctx.ShouldBindJSON(&user); err != nil {
		log.Fatalf("Bin User Model Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Bin User Model Error"})
		return
	}
	if err := u.UserService.Update(user); err != nil {
		log.Fatalf("Update User To Db Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Update User To Db Error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "Update User Success"})
}

// ok
func (u *UserApi) Query(ctx *gin.Context) {
	users, err := u.UserService.Query()
	if err != nil {
		log.Fatalf("Query Users From Db Error: %v\n", err)
		ctx.JSON(500, gin.H{"code": 500, "msg": "Query Users From Db Error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "msg": "Query Users Success", "data": users})
}
