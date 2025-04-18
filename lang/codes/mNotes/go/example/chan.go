package main

import "fmt"

func main() {
	ch := make(chan int, 1)

	// 入管道
	ch <- 1

	// 出管道
	num, ok := <-ch
	if ok {
		fmt.Println(num)
	}

	// 关闭管道
	close(ch)
}
