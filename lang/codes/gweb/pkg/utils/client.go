package utils

import (
	"encoding/json"
	"fmt"
	"log"
	"net"
)

type Client struct {
	Addr      string
	IpVersion string
	Conn      net.Conn
	ConData   ZoneParam
	DataCryt  DataCryt
}

func NewClient(conData ZoneParam) *Client {
	return &Client{
		Addr:      fmt.Sprintf("%s:%d", conData.ZoneIp, Setting.App.RemotePort),
		IpVersion: "tcp4",
		ConData:   conData,
		DataCryt:  NewDataHandle(),
	}
}

func (c Client) StartClient(ch chan interface{}) {
	addr, err := net.ResolveTCPAddr(c.IpVersion, c.Addr)
	if err != nil {
		panic(err)
	}
	c.Conn, err = net.DialTCP(c.IpVersion, nil, addr)
	if err != nil {
		panic(err)
	}
	go c.handleData(c.ConData, ch)
}

func (c Client) handleData(data ZoneParam, MsgCh chan interface{}) {
	mdata, err := json.Marshal(data)
	if err != nil {
		panic(err)
	}
	defer c.Conn.Close()
	c.DataCryt.WriteConnData(c.Conn, mdata)
	cdata := c.DataCryt.ReadConnData(c.Conn)
	log.Println(cdata)
	MsgCh <- cdata
}
