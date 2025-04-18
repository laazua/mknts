package servant

import (
	"fmt"
	"manage/internal/network"
	"net"
)

type Servant struct {
	Conn net.Conn
}

func NewServant() *Servant {
	return &Servant{}
}

func (s Servant) Run(addr string) error {
	// 监听端口
	listener, err := net.Listen("tcp", addr)
	if err != nil {
		fmt.Println("Error listening:", err)
		return err
	}
	defer listener.Close()

	fmt.Println("Server listening on ", addr)

	for {
		// 等待客户端连接
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			panic(err)
		}

		// 处理客户端连接
		go handleClient(conn)
	}
}

func handleClient(conn net.Conn) {
	defer conn.Close()
	tcpConn := network.NewMConn(conn)
	data := tcpConn.DataDecode()
	fmt.Println(data.Aa, data.Bb)
	m := network.Message{Aa: "1", Bb: "2"}
	tcpConn.DataEncode(m)
}
