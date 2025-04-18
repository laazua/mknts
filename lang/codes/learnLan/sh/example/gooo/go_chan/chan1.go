package main

import(
	"fmt"
	"time"
)

func Process(ch chan  int){
	//Do some work...
	time.Sleep(time.Second * 2)

	ch <- 8
}

func main(){
	channels := make([]chan int, 10)	//创建10个元素的切片，类型为channel

	for i := 0; i < 10; i++ {
		channels[i] = make(chan int)	//切片中放入一个channel
		go Process(channels[i])			//启动协程,传一个管道用于通信
	}

	for i, ch := range channels {		//遍历切片，等待子协程结束
		<- ch
		fmt.Println("Routine", i, "quite!")
	}
}