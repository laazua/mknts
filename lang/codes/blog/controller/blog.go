package controller

import (
	"env"
	"schema"

	"github.com/gin-gonic/gin"
)

func (b *Blog) ApiName() string {
	return "Blog"
}

func (b *Blog) ApiInit(group *gin.RouterGroup) {
	group.POST("/create", b.create)
	group.DELETE("/delete", b.delete)
	group.PUT("/update", b.update)
	group.GET("/query", b.query)
	group.GET("/query/:id", b.queryId)
}

func (b *Blog) create(ctx *gin.Context) {
	var blog schema.Blog
	if err := ctx.ShouldBind(&blog); err != nil {
		b.Logger.Fatalf("blog create api bind schema error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "blog create api bind schema error"})
		return
	}
	if err := b.StorageBlog.Create(blog); err != nil {
		b.Logger.Fatalf("blog create api create blog error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "blog create api create blog error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "create blog success"})
}

func (b *Blog) delete(ctx *gin.Context) {
	id := ctx.Param("id")
	if err := b.StorageBlog.Delete(env.Atoint(id)); err != nil {
		b.Logger.Fatalf("blog delete api delete blog error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "blog delete api delete blog error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "delete blog success"})
}

func (b *Blog) update(ctx *gin.Context) {
	var blog schema.Blog
	if err := b.StorageBlog.Update(blog); err != nil {
		b.Logger.Fatalf("blog update api update blog error: %v", err)
		ctx.JSON(400, gin.H{"code": 400, "message": "blog update api update blog error"})
		return
	}
	ctx.JSON(200, gin.H{"code": 200, "message": "update blog success"})
}

func (b *Blog) query(ctx *gin.Context) {}

func (b *Blog) queryId(ctx *gin.Context) {}
