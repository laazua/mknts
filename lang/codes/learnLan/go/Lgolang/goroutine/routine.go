package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func main() {
	for i := 0; i < 10; i++ {
		go Add(i, i)
	}
	//主线程不会等待其他协程执行完毕才推出(主线程自己的逻辑执行完毕立即退出,通过睡眠看到程序效果)
	time.Sleep(time.Second * 2)
}

func Add(x, y int) {
	z := x + y
	fmt.Println(z)
}

//多核并行计算
//计算N个整数的总和,将N个整数分成M份(M为cpu的个数),让每个cpu计算分给它的那个任务,最后将每个cpu的计算结果做累加
type Vector []float64

func (v Vector) DoSome(i, n int, u Vector, c chan int) {
	for ; i < n; i++ {
		v[i] += u.Op(v[i])
	}
	c <- 1    //发信号告诉任务管理者我已经计算完成了
}

const NCPU = 16    //假设总共有16核

func (v Vector) DoAll(u Vector) {
	//设置环境变量GOMAXPROCS的值
	runtime.GOMAXPROCS(16)

	c := make(chan int, NCPU)   //用于接受每个cpu的任务完成信号
	 for i := 0; i < NCPU; i++ {
	 	go v.DoSome(i * len(v) / NCPU, (i + 1) * len(v) /NCPU, u, c)
	 }
	 //等待所有cpu的任务完成
	 for i := 0; i < NCPU; i++ {
	 	<- c    //获取到一个数据,表示一个cpu计算完成
	 }
}

//runtime.NumCPU()获取cpu核心数量
//runtime.Gosched()使goroutine主动让出时间片
//要精细地控制goroutine的行为,了解runtime包

//同步锁,解决多个goroutine共享数据问题
//sync.Mutex   一个goroutine获得该锁并操作共享数据,其他goroutine只能等待该锁被释放,才能使用共享数据
//sync.RWMutex   单写多读模型,一个goroutine获得该所并操作共享数据时,其他goroutine不等不能对锁住的数据进行写操作,但是可以读
var mux sync.Mutex

func Foo() {
	mux.Lock()
	defer mux.Unlock()
	//操作共享数据
}

//全局唯一性操作(只需要运行一次的代码)
var (
	a string
    once sync.Once
)

func setup() {
 	a = "hello world"
 }

 func doPrint() {
 	once.Do(setup)
 	print(a)
 }

 func twoPrint() {
 	//两次调用doPrint(),但是setup()只执行一次
 	go doPrint()
 	go doPrint()
 }