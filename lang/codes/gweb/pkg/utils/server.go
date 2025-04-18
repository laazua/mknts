package utils

import (
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"os/exec"
)

type Serve struct {
	Addr      string
	IpVersion string
	DataCryt  DataCryt
}

func NewServe() *Serve {
	return &Serve{
		Addr:      fmt.Sprintf("%s:%d", Setting.App.Ip, Setting.App.Port),
		IpVersion: "tcp4",
		DataCryt:  NewDataHandle(),
	}
}

func (s Serve) Start() {
	addr, err := net.ResolveTCPAddr(s.IpVersion, s.Addr)
	if err != nil {
		panic(err)
	}
	listen, err := net.ListenTCP(s.IpVersion, addr)
	if err != nil {
		panic(err)
	}
	defer listen.Close()
	log.Printf("runing on: %v, Waiting for clients...\n", s.Addr)
	for {
		conn, err := listen.Accept()
		if err != nil {
			continue
		}
		log.Println(conn.RemoteAddr().String(), "connect success")
		go s.handConn(conn)
	}
}

func (s Serve) handConn(conn net.Conn) {
	condata := s.DataCryt.ReadConnData(conn)
	jdata := s.handleJob(condata)
	if jdata == nil {
		log.Println("cmd handle errpr")
		return
	}
	jsondata, err := json.Marshal(jdata)
	if err != nil {
		return
	}
	s.DataCryt.WriteConnData(conn, jsondata)
}

func (s Serve) handleJob(data string) *ConnData {
	var (
		z   *ZoneParam
		cmd string
	)
	err := json.Unmarshal([]byte(data), &z)
	if err != nil {
		return nil
	}
	zonePath := fmt.Sprintf("%s%s_%d", Setting.App.ZonePath, z.ZoneName, z.ZoneId)
	switch z.Target {
	case "open":
		if err := os.MkdirAll(zonePath, os.ModePerm); err != nil {
			return nil
		}
		cmd = ""
		fmt.Println("open")
	case "start":
		cmd = ""
	case "check":
		cmd = ""
	case "stop":
		cmd = ""
	case "reload":
		cmd = ""
	case "updatecon":
		cmd = ""
		fmt.Println("updatecon")
	case "updatebin":
		cmd = ""
	default:
		cmd = ""
		return &ConnData{Msg: "cmd error"}
	}
	if out, err := s.runCmd(cmd); err != nil {
		return &ConnData{Zone: z, Msg: err.Error()}
	} else {
		return &ConnData{Zone: z, Msg: out}
	}
}

func (s Serve) runCmd(cmd string) (string, error) {
	command := exec.Command("/bin/bash", "-c", cmd)
	if out, err := command.Output(); err != nil {
		return "", err
	} else {
		return string(out), nil
	}
}
