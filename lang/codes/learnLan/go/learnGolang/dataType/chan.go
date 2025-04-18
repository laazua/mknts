// chan
package main

import "fmt"

func main() {
	// 不带缓冲的chan
	// ch1 := make(chan int)

	// 声明带5个缓冲的chan
	ch2 := make(chan int, 5)
	ch2 <- 1
	ch2 <- 2
	ch2 <- 3
	ch2 <- 4
	ch2 <- 5
	if val1, ok := <-ch2; ok {
		fmt.Println(val1, ok)
	}
	if val2, ok := <-ch2; ok {
		fmt.Println(val2, ok)
	}

	// 声明只读chan
	// ch3: make(<-chan int)

	// 声明只写chan
	// ch4: make(chan<- int)

	// close(chan)
	// close后不能再写入，写入会panic
	// 重复close或出现panic
	// close后还能读取数据

	stop := make(chan bool)
	stop <- false
	testChan(stop)
	time.Sleep(10 * time.Second)
	stop <- true
	testChan(stop)
}

func testChan(isStop chan bool) {
	go func() {
		for {
			select {
			case <-isStop:
				fmt.Println("stopped, exit.")
			default:
				fmt.Println("running...")
			}
		}
	}()
}
