package rgpc

import (
	"bnzt/global"
	"context"
	"time"

	"github.com/shirou/gopsutil/net"
	"github.com/smallnest/rpcx/client"
	"github.com/smallnest/rpcx/protocol"
	"github.com/smallnest/rpcx/share"
)

// rpc client api
type RpcxClient interface {
	RZone(sevName, ip, channame, zone, target string, RepMsg chan interface{})
	RHost(sevName, ip string, RepMsg chan interface{})
}

func NewRpcxClient() RpcxClient {
	return &RClient{}
}

///////////////////////////////////////区服管理////////////////////////////////////////
type ZReq struct {
	ChanName string
	Zone     string
	Target   string
}

type ZReply struct {
	ZReq
	Msg string
}

type RClient struct{}

func (r *RClient) RZone(sevName, ip, channame, zone, target string, RepMsg chan interface{}) {
	d, err := client.NewPeer2PeerDiscovery("tcp@"+ip+global.AppCon.GetString("rpc.port"), "")
	if err != nil {
		RepMsg <- err
		return
	}
	opt := client.DefaultOption
	opt.SerializeType = protocol.JSON
	xclient := client.NewXClient(sevName, client.Failtry, client.RandomSelect, d, opt)
	xclient.Auth(global.AppCon.GetString("rpc.token"))
	defer xclient.Close()

	args := ZReq{
		ChanName: channame,
		Zone:     zone,
		Target:   target,
	}

	rep := &ZReply{}
	ctx := context.WithValue(context.Background(), share.ReqMetaDataKey, make(map[string]string))
	call, err := xclient.Go(ctx, sevName, args, rep, nil)
	if err != nil {
		RepMsg <- err
		return
	}
	repc := <-call.Done
	if repc.Error != nil {
		RepMsg <- repc.Error
		return
	}

	RepMsg <- rep
}

///////////////////////////////////主机资源/////////////////////////////////////////////
type HRelpy struct {
	C   Cpu
	M   Mem
	D   Disk
	L   Load
	N   Nett
	Num uint
	Ip  string
}

type Cpu struct {
	PhysicalCnt  int
	LogicalCnt   int
	TotalPercent []float64
	PerPercent   []float64
}

type Mem struct {
	Total   uint64
	Used    uint64
	Free    uint64
	Percent float64
}

type Disk struct {
	Total   uint64
	Free    uint64
	Used    uint64
	Percent float64
}

type Load struct {
	L1  float64
	L5  float64
	L15 float64
}

type Nett struct {
	IoConn  []net.ConnectionStat
	IoCount []net.IOCountersStat
}

type HReq struct {
	Ip string
}

func (r *RClient) RHost(sevName, ip string, RepMsg chan interface{}) {
	d, err := client.NewPeer2PeerDiscovery("tcp@"+ip+global.AppCon.GetString("rpc.port"), "")
	if err != nil {
		RepMsg <- err
		return
	}
	option := client.DefaultOption
	option.SerializeType = protocol.JSON
	option.IdleTimeout = time.Second * 240

	xclient := client.NewXClient(sevName, client.Failtry, client.RandomSelect, d, option)
	xclient.Auth(global.AppCon.GetString("rpc.token"))
	defer xclient.Close()

	args := HReq{
		Ip: ip,
	}
	rep := &HRelpy{}
	ctx := context.WithValue(context.Background(), share.ReqMetaDataKey, make(map[string]string))
	call, err := xclient.Go(ctx, sevName, args, rep, nil)
	if err != nil {
		RepMsg <- err
		return
	}
	replyCall := <-call.Done
	if replyCall.Error != nil {
		RepMsg <- replyCall.Error
	}
	RepMsg <- rep
}
