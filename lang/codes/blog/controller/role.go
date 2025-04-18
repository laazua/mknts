package controller

import (
	"env"
	"schema"

	"github.com/gin-gonic/gin"
)

func (r *Role) ApiName() string {
	return "role"
}

func (r *Role) ApiInit(group *gin.RouterGroup) {
	group.POST("/role/create", r.create)
	group.DELETE("/role/delete", r.delete)
	group.PUT("/role/update", r.update)
	group.GET("/role/query", r.query)
	group.GET("/role/query/:id", r.queryId)
}

func (r *Role) create(ctx *gin.Context) {
	var role schema.Role
	if err := ctx.ShouldBind(&role); err != nil {
		r.Logger.Fatalf("create role api bind schema error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "create role api bind schema error"})
		return
	}
	if err := r.StorageRole.Create(role); err != nil {
		r.Logger.Fatalf("create role api create role error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "create role api create role error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "create role success"})
}

func (r *Role) delete(ctx *gin.Context) {
	id := ctx.Param("id")
	if err := r.StorageRole.Delete(env.Atoint(id)); err != nil {
		r.Logger.Fatalf("delete role api delete role error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "delete role api delete role error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "delete role success"})
}

func (r *Role) update(ctx *gin.Context) {
	var role schema.Role
	if err := ctx.ShouldBind(&role); err != nil {
		r.Logger.Fatalf("update role api bind schema erro: %v", err)
		ctx.JSON(400, gin.H{"code": 200, "message": "update role api bind schema error"})
		return
	}
	if err := r.StorageRole.Update(role); err != nil {
		r.Logger.Fatalf("update role api update role error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "update role api update role error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "update role success"})
}

func (r *Role) query(ctx *gin.Context) {
	roles := r.StorageRole.Query()
	if roles == nil {
		r.Logger.Fatalf("role query api query role list empty")
		ctx.JSON(400, gin.H{"code": 400, "message": "role query api query role list empty"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "query role list success", "roles": roles})
}

func (r *Role) queryId(ctx *gin.Context) {
	id := ctx.Param("id")
	role, err := r.StorageRole.QueryId(env.Atoint(id))
	if err != nil {
		r.Logger.Fatalf("role queryId api query role error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "role queryId api query role error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "query role success", "role": role})
}
