package code

import (
	"fmt"
	"time"
)

func ChanTest() {
	// 无缓冲chan
	c := make(chan int)

	// 开启一个协程
	go func() {
		time.Sleep(time.Second * 60)
		c <- 1
	}()
	fmt.Println("do something...")

	// 等待协程完成
	<-c
	fmt.Println("协程已完成")
}
