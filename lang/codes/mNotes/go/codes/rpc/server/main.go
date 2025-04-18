package main

import (
	"log"
	"net"
	"net/rpc"
)

type HelloService struct{}

func (h *HelloService) Hello(req string, rep *string) error {
	*rep = "hello:" + req
	return nil
}

func main() {
	rpc.RegisterName("HelloService", new(HelloService))

	listener, err := net.Listen("tcp", ":8888")
	if err != nil {
		log.Fatal("listen tcp error: ", err)
	}

	conn, err := listener.Accept()
	if err != nil {
		log.Fatal("accept error: ", err)
	}
	rpc.ServeConn(conn)
}
