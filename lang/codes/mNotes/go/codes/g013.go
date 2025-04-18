// 管道监听
package main

import (
	"fmt"
	"time"
)

func main() {
	// 创建两个被监听的管道
	chan1 := make(chan int)
	chan2 := make(chan int)

	// 往chan1中写入数据
	go func() {
		for i := 0; i < 10; i++ {
			chan1 <- i
			time.Sleep(time.Second * 1)
		}
	}()

        // 往chan2中写入数据
	go func() {
		for i := 0; i < 10; i++ {
			chan2 <- i
			time.Sleep(time.Second * 2)
		}
	}()

	// 监听chan1, chan2管道中的数据变化
	go func() {
		for {
			fmt.Println("监听管道数据变化...")
			select {
			case <-chan1:
				fmt.Println("从chan1中取出了数据")
			case <-chan2:
				fmt.Println("从chan2中取出了数据")
				//default:
				//    fmt.Println("没有default分支,则select会阻塞")
				//    time.Sleep(time.Second*6)
			}
		}
	}()

	for {
		fmt.Println("++++++++++++")
		time.Sleep(time.Second * 5)
	}

}
