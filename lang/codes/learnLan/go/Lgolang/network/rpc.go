/*
远程过程调用(server/client):
通过网络从远程计算机程序上请求服务
rpc.Dial()
rpc.DialHTTP()
*/

//server
package network

import(
	"net/rpc"
	"net"
	"log"
	"errors"
	"net/http"
)

type Args struct {
	A, B int
}

type Quotient struct {
	Quo, Rem int
}

type Arith int

func (t *Arith) Multiply(args *Args, reply *int) error {
	*reply = args.A * args.B
	return  nil
}

func (t *Arith) Divide(args * Args, quo *Quotient) error {
	if args.B == 0 {
		return errors.New("divide by zero")
	}
	quo.Quo = args.A / args.B
	quo.Rem = args.A % args.B
	return  nil
}

func main() {
	arith := new(Arith)
	rpc.Register(arith)
	rpc.HandleHTTP()
	l, e := net.Listen("tcp", ":8888")
    if e != nil {
    	log.Fatal("listen error: ", e)
	}
	go http.Serve(l, nil)
}
