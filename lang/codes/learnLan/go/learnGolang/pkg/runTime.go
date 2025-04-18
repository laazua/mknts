// runtime package
package main

import (
	"fmt"
	"runtime"
	"time"
)

func testGosched(s string) {
	for i := 0; i < 2; i++ {
		fmt.Println(s)
	}
}

func testGoexit() {
	defer fmt.Println("A")
	func() {
		defer fmt.Println("B")
		// 结束协成
		runtime.Goexit()
		defer fmt.Println("C")
		fmt.Println("B")
	}()
	fmt.Println("A")
}

func testGOMAXPROCSa() {
	for i := 1; i < 10; i++ {
		fmt.Println("a: ", i)
	}
}

func testGOMAXPROCSb() {
	for i := 1; i < 10; i++ {
		fmt.Println("b: ", i)
	}
}

func main() {
	// test Gosched
	go testGosched("haha")
	for i := 0; i < 2; i++ {
		// 让出cpu时间片, 再次分配任务
		runtime.Gosched()
		fmt.Println("hehe")
	}

	// test Goexit
	// go testGoexit()
	// for {}

	// test GOMAXPROCS
	runtime.GOMAXPROCS(2) // 设置当前程序并发时占用cpu逻辑核心数
	go testGOMAXPROCSa()
	go testGOMAXPROCSb()
	time.Sleep(time.Second)
}
