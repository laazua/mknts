// 并发安全
package main

import (
	"fmt"
	"sync"
)

var (
	wg   sync.WaitGroup
	num  int64
	lock sync.Mutex // 互斥锁
)

func add() {
	for i := 0; i < 1000; i++ {
		lock.Lock() // 加锁
		num = num + 1
		lock.Unlock() // 解锁
	}
	wg.Done()
}

func main() {
	wg.Add(2)
	go add()
	go add()
	wg.Wait()
	fmt.Println(num)
}
