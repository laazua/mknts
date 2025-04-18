// channel

package main

import (
    "fmt"
    "time"
)

func main() {
	// 创建一个存放任意类型的channel
	ch := make(chan interface{})

	go func() {
		fmt.Println("start goroutine...")
		ch <- 100
		fmt.Println("exit goroutine...")
	}()
	fmt.Println("wait goroutine...")
	<-ch
	fmt.Println("all goroutine done...")

	// 单向channel
	// 只能发送 chan<-, 例子: ch := make(<-chan, int)
	// 只能接受 <-chan, 例子: ch := make(chan<-, int)

	// 带缓冲的channel
	// ch := make(chan int, 5)

	// data, ok := ch
	// if ok { fmt.Println(data) }

	// select
        // 协程通信
        ich := make(chan int, 10)
        for i:=0; i<10; i++ {
            go SendData(ich, i)
        }
        
        go GetsData(ich)
        time.Sleep(2*time.Second)
}

func SendData(ch chan int, num int) {
    ch <- num
}

func GetsData(ch chan int) {
    for {
        m := <- ch
        fmt.Println(m)
    }
}
