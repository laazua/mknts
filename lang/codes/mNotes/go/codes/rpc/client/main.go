package main

import (
	"fmt"
	"log"
	"net/rpc"
)

func main() {
	client, err := rpc.Dial("tcp", ":8888")
	if err != nil {
		log.Fatal("dial error: ", err)
	}

	var rep string
	err = client.Call("HelloService.Hello", "hello", &rep)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(rep)
}
