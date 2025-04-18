package api

import (
	"bnzt/models"
	"sync"

	"github.com/gin-gonic/gin"
)

var (
	wg sync.WaitGroup
)

// 区服管理接口
type YwMg interface {
	Add(c *gin.Context)
	Manage(c *gin.Context)
	GetList(c *gin.Context)
	Host(c *gin.Context)
}

func NewYwMg() YwMg {
	return &ywMg{}
}

type ywMg struct {
	Ozs models.Ozs
	Zos models.Zos
	Hrs models.Hrs
}

func (z *ywMg) GetList(c *gin.Context) {
	zones := zoneDao.ZoneList()
	resp.Success(c, zones, "获取区服列表成功")
}

// 添加区服
func (z *ywMg) Add(c *gin.Context) {
	if err := c.BindJSON(&z.Ozs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 区服信息写入数据库
	if !zoneDao.AddZone(z.Ozs) {
		resp.Failed(c, nil, "添加区服失败")
		return
	}
	// 调用对应ip上的区服管理服务进行区服初始化
	rpChan := make(chan interface{}, 1)
	defer close(rpChan)

	wg.Add(1)
	go grpc.RZone("Open", z.Ozs.Ip,
		z.Ozs.ChanName, z.Ozs.Zone, z.Ozs.Target, rpChan)
	wg.Done()
	wg.Wait()
	// 返回信息
	resp.Success(c, <-rpChan, "添加区服成功")
}

// 区服操作
func (z *ywMg) Manage(c *gin.Context) {
	if err := c.BindJSON(&z.Zos); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 调用远程服务(协程处理该功能)
	// runtime.GOMAXPROCS(runtime.NumCPU())
	rpChan := make(chan interface{}, len(z.Zos.Zones))
	wg.Add(len(z.Zos.Zones))
	for _, zz := range z.Zos.Zones {
		go grpc.RZone("ManagZone", zz.Ip,
			zz.ChanName, zz.Zone, zz.Target, rpChan)
	}

	data := make([]interface{}, 0, 6)
	go func(chanMsg chan interface{}) {
		for {
			data = append(data, <-chanMsg)
			wg.Done()
		}
	}(rpChan)
	wg.Wait()
	// defer close(rpChan)
	// 返回成功信息
	resp.Success(c, data, "区服操作成功")
}

func (z *ywMg) Host(c *gin.Context) {
	if err := c.BindJSON(&z.Hrs); err != nil {
		resp.Failed(c, nil, ErrForm)
		return
	}
	// 调用远程服务(多协程处理)
	rpChan := make(chan interface{}, len(z.Hrs.Ips))
	for _, ip := range z.Hrs.Ips {
		go grpc.RHost("Collector", ip, rpChan)
	}
	data := make([]interface{}, 0, 6)
	wg.Add(len(z.Hrs.Ips))
	go func(chanMsg chan interface{}) {
		for {
			data = append(data, <-chanMsg)
			wg.Done()
		}
	}(rpChan)
	wg.Wait()
	resp.Success(c, data, "主机资源获取成功")
}
