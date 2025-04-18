//竟态条件：多个线程共享一份数据，会产生争用和冲突，这种情况被称为竟态条件；它会破坏数据的一致性。
//同步：控制多个线程对共享数据资源对访问；避免多个线程在同一时刻操作同一个数据块；协调多个线程，避免它们同一时刻执行相同的代码块。
//互斥锁：保证同一时刻只有一个goroutine操作共享数据块(对共享资进行操作的代码片段视为一个临界区)，每当有goroutine要操作共享数据块时,要先加锁，操作完毕要解锁。
package main

import (
	"fmt"
	"sync"
)

//Mutex的使用,互斥锁都是成对出现(上锁与解锁)
 var mutex sync.Mutex

 func updatePublicResource(){
	 mutex.Lock()
	 doUpdate()
	 mutex.Unlock()
 }


 //RWMutex的使用，读写锁是读/写互斥锁的简称，是互斥锁的一种扩展；一个读写锁中包含两个锁，即：读锁和写锁
 //读写锁可以对共享资源的读操作和写操作进行区别，实现更加细腻的访问控制
 //对于某个受到读写锁保护的共享资源，多个写操作不能同时进行，写操作和读操作也不能同时进行，多个读操作可以同时进行
 //对写锁进行解锁，会唤醒"所有因试图锁定的读锁，而被阻塞的goroutine“，通常他们都能完成对读锁的锁定
 //读读锁进行解锁，会在没有其他锁定中读锁的前提下，唤醒"因试图锁定的写锁，而被阻塞的goroutine"；只有一个等待时间最长的被唤醒的goroutine能够成功完成对写锁的锁定
 var rwmutex sync.RWMutex

 func updatePublicResource{
	 rwmutex.Lock()
	 doUpdate()
	 rwmutex.Unlock()
 }

 func readPublicResource(){
	 rwmutex.RLock()
	 read()
	 rwmutex.RUnlock()
 }


 //条件变量sync.Cond,基于互斥锁，用于协调想要访问共享资源的线程；当共享资源发生变化时，它可以通知被互斥锁阻塞的线程
 //io.Pipe的实现就是基于sync.Cond
 //sync.Cond需要sync.Locker类型的参数用于初始化
 type Locker interface{
	 Lock()
	 Unlock()
 }

 //sync.Cond提供3个方法
 //Broadcast(): 唤醒所有等待Cond的goroutine.不需要在锁的保护下进行
 //Signal(): 唤醒一个等待Cond的goroutine.不需要在锁的保护下进行
 //Wait(): 解锁互斥锁，挂起当前goroutine.当Broadcast或Signal唤醒这个goroutine,Wait在返回前会再锁定互斥锁。因此Wait()需要在锁的保护下进行.
 var(
	lock sync.RWMutex
	sendCond, recvCond *sync.Cond 
 )

 func init(){
	 sendCond = sync.NewCond(&lock)
	 recvCond = sync.NewCond(&lock)  //获取读写锁中的读锁
 }

 func send(){
	 lock.Lock()
	 for !writeCondition(){
		 sendCond.Wait()
	 }
	 writeResource()
	 lock.Unlock()
	 recvCond.Signal()    //如果有多个接收的goroutine就使用recvCond.Broadcast()
 }

 func receive(){
	 lock.Lock()
	 for !readCondition(){
		 recvCond.Wait()
	 }
	 receiveResource()
	 lock.Unlock()
	 sendCond.Signal()    //如果有多个发送的goroutine就使用sendCond.Broadcast()
 }
 
 
//sync.WaitGroup
wg := &sync.WaitGroup{}
fori := 0; i < 8; i++{
	wg.Add(1)	//增加wg内部计数器
	go func(){
		//Do something
		wg.Done()	//减少wg内部计数器
	}()
}

wg.Wait()   //等待wg内部计数器为0


//sync.Map
m := &sync.Map{}
//添加元素
m.Store(1, "one")
m.Store(2, "two")
//获取元素1
value, contains := m.Load(1)
if contains {
	fmt.Printf("%s\n", value.(string))
}
//返回已存在value,否则把指定的键值存储到map中
value, loaded := m.LoadOrStore(3, "threee")
if !loaded{
	fmt.Printf("%s\n", value.(string))
}
m.Delete(3)
//迭代所有元素
m.Range(func(key, value interface{}) bool{
	fmt.Printf("%d: %s\n", key.(int), value.(string))
	return true
})


//sync.Pool
pool := &sync.Pool{}
for i := 1; i <=3; i++{
	pool.Put(NewConnection(i))
}
connection := pool.Get().(*Connection)
fmt.Printf("%d\n", connection.id)
connection = pool.Get().(*Connection)
fmt.Printf("%d\n", connection.id)
connection = pool.Get().(*Connection)
fmt.Printf("%d\n", connection.id)


//sync.Once
once := &sync.Once{}
for i := 0; i < 4; i++{
	i := i
	go func(){
		once.Do(func(){
			fmt.Printf("first %d\n", i)
		})
	}()
}

//sync.Cond
...