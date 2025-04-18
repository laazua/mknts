package api

import (
	"bnzt/dao"
	"bnzt/rgpc"
	"bnzt/utils"

	"github.com/gin-gonic/gin"
)

// 全局变量
var (
	// 错误信息
	ErrForm  = "表单参数错误!"
	ErrPass  = "密码错误!"
	ErrToken = "创建token错误!"

	// 前端响应接口对象
	resp = utils.NewResp()
	// 数据库接口对象
	userDao = dao.NewDbUser()
	roleDao = dao.NewDbRole()
	permDao = dao.NewDbPerm()
	zoneDao = dao.NewDbZone()
	// token接口对象
	tk = utils.NewToken()
	// elastic接口对象
	oa = dao.NewOperation()
	// rpc接口对象
	grpc = rgpc.NewRpcxClient()
)

// http请求基础接口
type BaseApi interface {
	Get(c *gin.Context)
	Add(c *gin.Context)
	Del(c *gin.Context)
	Upd(c *gin.Context)
	GetList(c *gin.Context)
}

// 创建对应的接口实例对象
func NewApi(name string) interface{} {
	switch name {
	case "user":
		return &user{}
	case "role":
		return &role{}
	case "perm":
		return &perm{}
	default:
		return nil
	}
}
