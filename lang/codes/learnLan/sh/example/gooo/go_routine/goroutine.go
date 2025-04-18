//goroutine：同一个进程中,多个goroutine共享内存数据;
// 但是设计上要遵循：不要通过共享数据来通信,而是通过通信来共享内存数据
//通信方式：channel
package main

import (
	"fmt"
	"runtime"
)

func say(s string) {
	for i := 0; i < 5; i++{
		runtime.Gosched()     //让cpu把时间片分给别人,下次某个时刻继续恢复执行该goroutine
		fmt.Println(s)
	}
}

//channel使用
func sum(a []int, c chan int){
	sum := 0
	for _, v := range a{
		sum += v
	}
	c <- sum     //send sum to c
}

func main(){
	go say("world")
	say("hello")

	a := []int{1,2,3,4,5,6}
	c := make(chan int)
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	x, y := <-c, <-c   //receive from c
	fmt.Println(x, y, x+y)
}