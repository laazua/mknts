//channel是类型相关的,不同的channel有不同的类型
package main

import (
	"fmt"
	"time"
)

func Count(ch chan int) {
	ch <- 1
	fmt.Println("Counting")
}

func main() {
	chs := make([]chan int, 10)
	for i := 0; i < 10; i++ {
		chs[i] = make(chan  int)
		go Count(chs[i])
	}

	for _, ch := range (chs) {
		<-ch
	}
}

/*
var ch1 chan int
var ch2 chan map[string] chan bool
ch3 := make(chan int, 5)  带缓存channel  可以使用range关键字
ch4 := make(chan int)    不带缓存的channel  不可以使用关键字range

ch <- value    往ch中写数据
value := <-  ch   从ch中读取数据
往channel中写如的数据数量超过了channel的大小时,会阻塞channel,
从空channel中读取数据时,也会阻塞channel

单向channel: 只读或者只写channel
var ch5 chan<- int   只用于写int型数据
var ch6 <-chan int   只用于读int型数据

单向channel初始化(类型转换)
ch7 := make(chan int)
ch8 := <-chan int(ch7)
ch9 := chan<- int(ch7)

channel关闭
close(ch)
判断channel是否被关闭
x, ok := <-ch
if !ok {
   fmt.Println(x)
}
*/

//select,随机向ch中写入0或者1
func TestSelect1(ch chan int) chan int{
	for {
		select {
		    case ch <- 0:
			case ch <- 1:
		}
		i := <- ch
		fmt.Println("i = ", i)
		return  ch
	}
}

//利用select机制解决channel读写超时
//select特点是只要其中一个case已经完成,程序就继续往下执行,而不会考虑其他case的情况
func TestSelect2(ch chan  int) {
	//实现并执行一个匿名超时等待函数
	timeout := make(chan bool, 1)
	go func() {
		//设置ch阻塞时间
		time.Sleep(time.Second * 1)
		timeout <- true
	}()

	select {
	    //从ch中读取数据
	    case <- ch:
	    //没有从ch中读取到数据,就从timeout中读取数据,继续向下执行使ch阻塞了1s
	    case <- timeout:
	}
}

//channel传递[在管道中传递的数据是一个整数(value)];定义一系列PipeData的数据结构并传递给handle()
//实际应用中value可能是个数据块
type PipeData struct {
	value    int
	handler  func(int) int
	next     chan int
}

func handle(queue chan *PipeData) {
	for data := range queue {
		data.next <- data.handler(data.value)
	}
}