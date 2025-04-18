// 线程
package main

import (
	"fmt"
	"sync"
)

var (
	wg sync.WaitGroup
)

func test(i int) {
	defer wg.Done() // goroutine结束就登记-1
	fmt.Println("goroutine ", i)
}

func main() {
	for i := 0; i < 5; i++ {
		wg.Add(1) // 启动一个goroutine登记+1
		go test(i)
	}
	wg.Wait() // 等待所有登记的goroutine都结束
}
