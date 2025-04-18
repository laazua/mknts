// 协程通信 channel
package main

import "fmt"

func recv(c chan int) {
	ret := <-c
	fmt.Println("recive: ", ret)
	close(c)
}

func main() {
	ch := make(chan int)
	go recv(ch)
	ch <- 10
	fmt.Println("send.")
}
