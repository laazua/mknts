package main

import (
	"bnzt/rgpc/server/global"
	"context"
	"errors"
	"fmt"
	"log"
	"os"
	"os/exec"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/load"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/net"
	"github.com/shirou/gopsutil/process"
	"github.com/smallnest/rpcx/protocol"
	"github.com/smallnest/rpcx/server"
)

// 运行命令
func runCommand(command string) (string, error) {
	cmd := exec.Command("/bin/bash", "-c", command)
	out, err := cmd.Output()
	if err != nil {
		log.Println(string(out), err)
		return "", err
	}
	return string(out), nil
}

////////////////////////////////////区服管理////////////////////////////////////
type Zone struct{}

// 请求参数
type ZoneReq struct {
	ChanName string
	Zone     string
	Target   string
}

// 响应消息
type ZoneReply struct {
	ZoneReq
	Msg string
}

// 添加区服
func (z *Zone) Open(ctx context.Context, r *ZoneReq, rep *ZoneReply) error {
	// 创建目录
	programePath := global.AppCon.GetString("zone.path") + r.ChanName + "_" + r.Zone
	if err := os.MkdirAll(programePath, os.ModePerm); err != nil {
		return err
	}
	// 拉取配置文件
	svnCmd := fmt.Sprintf("svn --username %v --password %v checkout %v %v --force 1>/dev/null",
		global.AppCon.GetString("svn.user"), global.AppCon.GetString("svn.pass"),
		global.AppCon.GetString("svn.addr"), programePath)
	out, err := runCommand(svnCmd)
	if err != nil {
		return err
	}
	rep.ChanName = r.ChanName
	rep.Zone = r.Zone
	rep.Target = r.Target
	rep.Msg = fmt.Sprintf("%v", out)
	return nil
}

// 区服操作[start|stop|check|update]
func (z *Zone) ManagZone(ctx context.Context, r *ZoneReq, rep *ZoneReply) error {
	var shCmd string
	programePath := global.AppCon.GetString("zone.path") + r.ChanName + "_" + r.Zone
	switch r.Target {
	case "Start":
		shCmd = fmt.Sprintf("cd %v && sh game_opt.sh start", programePath)
	case "Stop":
		shCmd = fmt.Sprintf("cd %v && sh game_opt.sh stop", programePath)
	case "Check":
		shCmd = fmt.Sprintf("cd %v && sh game_opt.sh check", programePath)
	case "UpdateCon":
		shCmd = fmt.Sprintf("svn up --username %v --password %v %v |grep -w revision",
			global.AppCon.GetString("svn.user"), global.AppCon.GetString("svn.pass"), programePath)
	case "UpdateBin":
		shCmd = fmt.Sprintf("cd %v && %v", programePath, global.AppCon.GetString("zone.bincmd"))
	case "Reload":
		shCmd = fmt.Sprintf("cd %v && sh game_opt.sh reload", programePath)
	default:
		shCmd = ""
	}
	if shCmd == "" {
		return errors.New("shCmd nil")
	}
	rep.Target = r.Target
	rep.ChanName = r.ChanName
	rep.Zone = r.Zone

	out, err := runCommand(shCmd)
	if err != nil {
		rep.Msg = "运行命令出错"
		return err
	}
	rep.Msg = fmt.Sprintf("%v", out)
	return nil
}

/////////////////////////////////////////主机信息//////////////////////////////////////////
type Host struct{}

// 请求参数
type HostReq struct {
	Ip string
}

// 响应
type HostReply struct {
	Ip  string
	C   Cpu
	M   Mem
	D   Disk
	L   Load
	N   Nett
	Num uint
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

func (h *Host) Collector(ctx context.Context, r *HostReq, rep *HostReply) error {
	log.Println("xxxxxxx", r.Ip)
	// cpu相关
	physicalCnt, err := cpu.Counts(false)
	if err != nil {
		return errors.New("获取cpu物理核心数错误")
	}
	logicalCnt, err := cpu.Counts(true)
	if err != nil {
		return errors.New("获取cpu逻辑核心数错误")
	}
	totalPercent, err := cpu.Percent(3*time.Second, false)
	if err != nil {
		return errors.New("获取cpu总的使用率错误")
	}
	perPercent, err := cpu.Percent(3*time.Second, true)
	if err != nil {
		return errors.New("获取cpu每秒使用率错误")
	}
	c := &Cpu{
		PhysicalCnt:  physicalCnt,
		LogicalCnt:   logicalCnt,
		TotalPercent: totalPercent,
		PerPercent:   perPercent,
	}
	// 内存相关
	mem, err := mem.VirtualMemory()
	if err != nil {
		return errors.New("获取内存信息失败")
	}
	m := &Mem{
		Total:   mem.Total,
		Used:    mem.Used,
		Free:    mem.Free,
		Percent: mem.UsedPercent,
	}
	// 磁盘相关
	disk, err := disk.Usage(global.AppCon.GetString("host.disk"))
	if err != nil {
		return errors.New("获取磁盘信息失败")
	}
	d := &Disk{
		Total:   disk.Total,
		Used:    disk.Used,
		Free:    disk.Free,
		Percent: disk.UsedPercent,
	}
	// 负载相关
	load, err := load.Avg()
	if err != nil {
		return errors.New("获取负载信息失败")
	}
	l := &Load{
		L1:  load.Load1,
		L5:  load.Load5,
		L15: load.Load15,
	}
	// 网络相关
	nett, err := net.ConnectionsMax("all", 0)
	if err != nil {
		return errors.New("获取网络连接信息错误")
	}
	// 网络流量
	ioNet, err := net.IOCounters(true)
	if err != nil {
		return errors.New("获取网络流量错误")
	}
	n := &Nett{
		IoConn:  nett,
		IoCount: ioNet,
	}
	// 开服数量(pid)
	pids, err := process.Pids()
	if err != nil {
		return errors.New("获取pid信息失败")
	}

	var num uint = 0
	for _, p := range pids {
		pp, _ := process.NewProcess(p)
		name, _ := pp.Name()
		if name == global.AppCon.GetString("zone.name") {
			num++
		}
	}

	rep.C = *c
	rep.M = *m
	rep.D = *d
	rep.L = *l
	rep.N = *n
	rep.Num = num
	rep.Ip = r.Ip

	return nil
}

// token校验
func auth(ctx context.Context, req *protocol.Message, token string) error {
	if token != global.AppCon.GetString("app.token") {
		return errors.New("invalid token")
	}
	return nil
}

func main() {
	service := server.NewServer()
	// 注册服务方法
	service.RegisterName("Open", new(Zone), "")
	service.RegisterName("ManagZone", new(Zone), "")
	service.RegisterName("Collector", new(Host), "")

	service.AuthFunc = auth

	if err := service.Serve("tcp", global.AppCon.GetString("app.addr")); err != nil {
		panic(err)
	}
}
