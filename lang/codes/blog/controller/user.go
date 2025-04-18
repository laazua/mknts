package controller

import (
	"env"
	"schema"

	"github.com/gin-gonic/gin"
)

func (u *User) ApiName() string {
	return "user"
}

func (u *User) ApiInit(group *gin.RouterGroup) {
	group.POST("/user/create", u.create)
	group.DELETE("/user/delete", u.delete)
	group.PUT("/user/update", u.update)
	group.GET("/user/query", u.query)
	group.GET("/user/query/:id", u.queryId)
}

func (u *User) create(ctx *gin.Context) {
	var user schema.User
	if err := ctx.ShouldBind(&user); err != nil {
		u.Logger.Fatalf("user create api bind schema error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user create api bind schema error"})
		return
	}
	if err := u.StorageUser.Create(user); err != nil {
		u.Logger.Fatalf("user create api create user error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user create api create user error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "create user success"})
}

func (u *User) delete(ctx *gin.Context) {
	id := ctx.Param("id")
	if err := u.StorageUser.Delete(env.Atoint(id)); err != nil {
		u.Logger.Fatalf("user delete api delete user error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user delete api delete user error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "delete user success"})
}

func (u *User) update(ctx *gin.Context) {
	var user schema.User
	if err := ctx.ShouldBind(&user); err != nil {
		u.Logger.Fatalf("user update api bind schema error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user update api bind schema error"})
		return
	}
	if err := u.StorageUser.Update(user); err != nil {
		u.Logger.Fatalf("user update api update user error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user update api update user error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "update user success"})
}

// query user list
func (u *User) query(ctx *gin.Context) {
	users := u.StorageUser.Select()
	if users == nil {
		u.Logger.Fatalf("user query api query user list empty")
		ctx.JSON(400, gin.H{"code": 400, "message": "user query api query user list is empty"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "query user list success", "users": users})
}

func (u *User) queryId(ctx *gin.Context) {
	id := ctx.Param("id")
	user, err := u.StorageUser.SelectId(env.Atoint(id))
	if err != nil {
		u.Logger.Fatalf("user queryId api query user error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "user queryId api query user error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "query user success", "user": user})
}
