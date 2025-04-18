package controller

import (
	"schema"

	"github.com/gin-gonic/gin"
)

func (a *Auth) ApiName() string {
	return "Auth"
}

func (a *Auth) ApiInit(group *gin.RouterGroup) {
	group.POST("/auth/login", a.login)
}

func (a *Auth) login(ctx *gin.Context) {
	var auth schema.Auth
	if err := ctx.ShouldBind(&auth); err != nil {
		a.Logger.Fatalf("auth login api bind schema error: %v .", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "auth login api bind schema error"})
		return
	}
	if !a.StorageAuth.Auth(auth) {
		a.Logger.Fatal("auth login api auth failure !")
		ctx.JSON(400, gin.H{"code": 400, "message": "login api auth failure"})
		return
	}
	// 生成token
	token, err := a.Heper.CreateToken(auth.Email)
	if err != nil {
		a.Logger.Fatalf("auth login api create token error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "auth login api create token error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "login success .", "token": token})
}
