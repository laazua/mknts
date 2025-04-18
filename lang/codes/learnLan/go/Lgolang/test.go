package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("tcp", ":8080")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("dial is ok")
	conn.Write("aaa123456")
	fmt.Println("data is sended.")
}