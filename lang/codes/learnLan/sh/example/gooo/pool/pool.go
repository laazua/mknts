//管理用户定义的一组资源
package pool

import (
	"errors"
	"log"
	"io"
	"sync"
)

//pool管理一组可以安全地在多个goroutine间共享的资源。被管理的资源必须实现io.Closer接口
type Pool struct {
	m            sync.Mutex     //保证多个goroutine访问资源池时，池内的值是安全的
	resources    chan io.Closer    //io.Closer接口类型,来保存共享的资源
	factory      func() (io.Closer, error)  //函数类型
	closed       bool
}

//ErrPoolClosed表示请求(Acquire)了一个已经关闭的池
var ErrPoolClosed = errors.New("Pool has bee closed.")

//New创建一个用来管理资源的池，这个池需要一个可以分配心资源的函数，并规定池的大小
func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
	if size <= 0 {
		return nil, errors.New("size value too small.")
	}
	return &Pool {
		factory:    fn,

		resources:  make(chan io.Closer, size)
	}, nil
}

//Acquire从池中获取一个资源
func (p *Pool) Acquire() (io.Closer, error) {
	select {
	//检查是否有空闲的资源
	case r, ok := <-p.resources:
		log.Println("Acquire: ", "Shared Resource")
		if !ok {
			return nil, ErrPoolClosed
		}
		return r, nil
	//因为没有空闲资源可用,所以提供一个新资源
	default:
		log.Println("Acquire:", "New Resource")
		return p.factory()
	}
}

//Release将一个使用后的资源放回池里
func (p *Pool) Release(r io.Closer) {
	//保证本操作和Close操作安全
	p.m.Lock()
	defer p.m.Unlock()
	//如果池已经关闭,销毁这个资源
	if p.closed {
		r.Close()
		return
	}
	select {
		//试图将这个资源放入队列
	case p.resources <- r:
		log.Println("Release:", "In Queue")
	//如果队列已经满了,则关闭这个资源
	default:
		log.Println("Release:", "Closing")
		r.Close()
	}
}

//Close会让资源池停止工作，并关闭所有现有资源
func (p *Pool) Close() {
	//保证本操作与Release操作的安全
	p.m.Lock()
	defer p.m.Unlock()
	//如果pool已经关闭,什么也不做
	if p.closed {
		return
	}
	//将池关闭
	p.closed = true
	//在清空通道里的资源前，将通道关闭，如果不这样做发生死锁
	close(p.resources)
	//关闭资源
	for r:= range p.resources {
		r.Close()
	}
}