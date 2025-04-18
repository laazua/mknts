package network

import (
	"encoding/gob"
	"net"
)

type tcpConn struct {
	Id   int
	Conn net.Conn
}

func NewMConn(conn net.Conn) *tcpConn {
	return &tcpConn{
		Id:   1,
		Conn: conn,
	}
}

func (tc *tcpConn) DataEncode(data any) {
	encoder := gob.NewEncoder(tc.Conn)
	encoder.Encode(data)
}

func (tc *tcpConn) DataDecode() Message {
	decoder := gob.NewDecoder(tc.Conn)
	var data Message
	decoder.Decode(&data)
	return data
}
