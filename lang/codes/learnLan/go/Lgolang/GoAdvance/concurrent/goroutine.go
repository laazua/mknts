// 并发实现: 协成
// 多个协成之间通行
// 多个协成间的同步
package concurrent

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

// 协成并发
func Loop() {
	for i := 1; i < 11; i++ {
		fmt.Println(i)
		time.Sleep(time.Microsecond * 20)
	}
}

func testGoroutine() {
	fmt.Printf("cpu num = %d", runtime.NumCPU()) // 设置cpu核心数(一般写在程序入口处), 注意不能影响其他程序的正常运行.
	runtime.GOMAXPROCS(runtime.NumCPU() - 1)
	//启动两个协成
	go Loop()
	go Loop()
}

// 协成通讯
var (
	chanInt chan int  = make(chan int, 5)
	timeout chan bool = make(chan bool)
)

func Send() {
	chanInt <- 1
	chanInt <- 2
	chanInt <- 3
	chanInt <- 4
	timeout <- true
}

func Receive() {
	for {
		select {
		case num := <-chanInt:
			fmt.Println(num)
		case <-timeout:
			fmt.Println("time out ...")
		}
	}
}

// 协成同步
var WG sync.WaitGroup

func Read() {
	for i := 0; i < 3; i++ {
		WG.Add(1)
	}
}

func Write() {
	for i := 1; i < 3; i++ {
		time.Sleep(time.Second * 2)
		WG.Done()
	}
}
