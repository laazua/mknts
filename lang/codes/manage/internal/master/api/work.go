package api

import (
	"manage/internal/master/core"
	"manage/internal/network"

	"github.com/gin-gonic/gin"
)

type apiWork struct {
	core.TestModel
}

func newApiWork() *apiWork {
	return &apiWork{}
}

func (aw *apiWork) test(ctx *gin.Context) {
	if err := ctx.ShouldBindJSON(&aw.TestModel); err != nil {
		panic(err)
	}
	data := network.Message{Aa: aw.Aa, Bb: aw.Bb}
	core.SendData("192.168.165.88:8898", data)
	ctx.JSON(200, "success")
}
