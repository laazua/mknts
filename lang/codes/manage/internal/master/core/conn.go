package core

import (
	"fmt"
	"manage/internal/network"
	"net"
)

func SendData(addr string, data any) {
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		panic(err)
	}
	tcpConn := network.NewMConn(conn)
	tcpConn.DataEncode(data)
	d := tcpConn.DataDecode()
	fmt.Println(d.Aa, d.Bb)
}
