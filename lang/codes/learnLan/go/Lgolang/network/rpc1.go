//client
package network

import(
	"net/rpc"
	"log"
	"fmt"
)

func main() {
	serverAddress := "127.0.0.1"
	client, err := rpc.DialHTTP("tcp", serverAddress + ":8888")
	if err != nil {
		log.Fatal("dialing: ", err)
	}

	//同步调用
	args := &server.Args{7,8}
	var reply int
	err = client.Call("Arith.Multiply", args, &reply)
	if err != nil {
		log.Fatal("arith error: ", err)
	}
	fmt.Println("Arith: %d * %d %d", args.A, args.B, reply)

	//异步调用
	quotient := new(Quotient)
	divCall := client.Go("Arith.Divide", args, &quotient, nil)
	replyCall := <- divCall.Done
	fmt.Println(replyCall)
}