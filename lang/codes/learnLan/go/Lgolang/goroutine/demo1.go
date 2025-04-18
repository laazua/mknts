// Goroutine 是与其他函数或方法同时运行的函数或方法。
// Goroutines 可以被认为是轻量级的线程。 与线程相比，创建 Goroutine 的开销很小。
// Go应用程序同时运行数千个 Goroutine 是非常常见的做法
package goroutine

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup
var ch = make(chan int, 5) // 创建大小为5的缓冲channel

// 协程不需要通信的函数
func routineNotCommunicate(url string) {
	fmt.Println("down load: ", url)
	time.Sleep(time.Second)
	wg.Done()
}

func routineCommunicate(url string) {
	fmt.Println("down load: ", url)
	time.Sleep(time.Second * 5)
	ch <- 1
}

func main() {
	// 协程不需要通信
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go routineNotCommunicate("start/" + fmt.Sprintf("%v", i))
	}
	wg.Wait()
	fmt.Println("routine not communicate done!")

	// 协程之间要通行
	for i := 0; i < 5; i++ {
		go routineCommunicate("start/" + fmt.Sprintf("%v", i))
	}
	for i := 0; i < 5; i++ {
		msg := <-ch
		fmt.Println(msg)
	}
	fmt.Println("routine communicate done!")
}
