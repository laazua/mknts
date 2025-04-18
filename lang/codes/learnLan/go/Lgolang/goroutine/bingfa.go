//并发说明
/*
	每个程序在运行时,都有自己的调用栈和堆,有一个完整的上下文,操作系统在调度进程的时候,会保存被调度进程的上下文环境,等待该进程获得时间片
	后,再恢复该进程的上下文到系统中。
	并发意味着程序在运行时有多个执行上下文,对应着多个调用栈。

	多进程: 是在操作系统层面进行并发的基本模式(由内核管理进程,开销较大)
	多线程: cpu调度的最小单元,是程序内的一个可执行单元(进程层面)
	协程: 一种用户态线程,不需要操作系统来进行抢占式调度,需要语言层面的支持,如果语言不支持,需要在程序中自行实现调度器.

	不同线程(协程)对共享数据处理是有两种方式:共享内存 和 消息机制
	Go采用:消息机制(channel)   "不要通过共享内存来通信,而是应该通过通信来共享内存."
	Goroutine采用半抢占式的写作调度,只有当前Goroutine发生阻塞时才会导致调度;同时发生在用户态,调度器会根据具体函数只保存必要的寄存器,切换的代价比体痛线程低得多

	常见并发模型:
		channel
		生产者&&消费者
		发布订阅模型

	控制并发数量,给主机上的其他应用/任务预留一定的CPU资源
*/
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

var total struct {
	sync.Mutex
	value  int
}

var Total uint64

func main() {
	//原子操作是指并发编程中"最小且不可并行化"的操作,例如多个并发体需要对同一共享资源进行操作的话.
	//同一时刻只允许唯一一个并发体对其进行操作,即通过互斥来保证原子操作
	//用互斥锁来保护数值型的共享资源,麻烦且效率低下,sync/atomic包对原子操作提供了丰富的支持

	//互斥锁实现共享资源的访问
	var wg sync.WaitGroup
	wg.Add(2)    //2启动的协程数量
	//go worker(&wg)
	//go worker(&wg)

	//sync/atomic包实现共享资源的访问
	go doWorker(&wg)
	go doWorker(&wg)

	wg.Wait()
	fmt.Println(total.value)
	fmt.Println(Total)



}

func doWorker(wg *sync.WaitGroup) {
	defer wg.Done()

	var i uint64
	for i = 0; i <= 100; i++ {
		atomic.AddUint64(&Total, i)
	}
}

func worker(wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i <= 100; i++ {
		total.Lock()
		total.value += 1
		total.Unlock()
	}
}