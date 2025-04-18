// goroutine与python语言中的协程区别:
// 1. goroutine可能发生并行执行,但coroutine始终顺序执行
// 2. goroutine无法控制自己获取高优先度支持,coroutine程
//    序需要主动交出控制权,宿主才能获得控制权并将控制权交
//    给其他coroutine
// 3. goroutine间使用channel通信;coroutine使用yield操作

package main

import (
	"fmt"
	"sync"
	"time"
)

// 并发
// go funcName(args...)
// 协程中的函数返回值会被忽略
// 获取协程函数中的返回值使用管道

var (
	shareNum = 0
	mutex    sync.Mutex
)

func main() {
	// cpuNum := runtime.NumCPU()
	// // cpuNum < 1: 不修改任何数值
	// // cpuNum = 1: 单核执行协程函数
	// // cpuNum > 1: 多核并行执行协程函数

	// runtime.GOMAXPROCS(cpuNum)
	// for i := 1; i < 9; i++ {
	// 	go mPrint(i)
	// 	time.Sleep(time.Second * 1)
	// }

	// 匿名协程函数
	// go func(args ...interface{}) {
	// 	fmt.Println(args...)
	// }(1, 2, 3)

	// 共享内存加锁(不建议)
	// for i := 1; i < 10; i++ {
	// 	go reduce()
	// 	go increase()
	// 	time.Sleep(time.Second * 4)
	// }
	// fmt.Println(shareNum)

	// 管道(建议)
	ch := make(chan interface{})
	go producer(ch)
	go consumer(ch)
	time.Sleep(time.Millisecond * 1000)
}

// func mPrint() {
// 	fmt.Println("协程函数 ", n)
// 	time.Sleep(time.Second * 1)
// }

// 共享内存
func reduce() {
	for {
		mutex.Lock()
		shareNum--
		mutex.Unlock()
		time.Sleep(time.Second * 1)
		fmt.Println("reduce: ", shareNum)
	}
}

func increase() {
	for {
		mutex.Lock()
		shareNum++
		mutex.Unlock()
		time.Sleep(time.Second * 1)
		fmt.Println("increase: ", shareNum)
	}
}

// channel
func producer(ch chan interface{}) {
	fmt.Println("将数据放入管道...")
	ch <- 100
}

func consumer(ch chan interface{}) {
	fmt.Println("将数据从管道取出...")
	data := <-ch
	fmt.Println("从管道中取出的数据是: ", data)
}
