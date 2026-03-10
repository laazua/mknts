package util

import (
	"sync"
)

// BytePool 字节缓冲池
type BytePool struct {
	pool *sync.Pool
	size int
}

// NewBytePool 创建新的字节缓冲池
func NewBytePool(size int) *BytePool {
	return &BytePool{
		pool: &sync.Pool{
			New: func() interface{} {
				return make([]byte, size)
			},
		},
		size: size,
	}
}

// Get 获取字节缓冲
func (bp *BytePool) Get() []byte {
	return bp.pool.Get().([]byte)
}

// Put 归还字节缓冲
func (bp *BytePool) Put(buf []byte) {
	if cap(buf) >= bp.size {
		bp.pool.Put(buf[:bp.size])
	}
}

// GoroutinePool Goroutine 任务池
type GoroutinePool struct {
	taskChan chan func()
	workers  int
	wg       sync.WaitGroup
	closed   bool
	mu       sync.Mutex
}

// NewGoroutinePool 创建新的 Goroutine 任务池
func NewGoroutinePool(workers int) *GoroutinePool {
	if workers <= 0 {
		workers = 1
	}

	gp := &GoroutinePool{
		taskChan: make(chan func(), 100),
		workers:  workers,
	}

	// 启动工作线程
	for i := 0; i < workers; i++ {
		gp.wg.Add(1)
		go gp.worker()
	}

	return gp
}

// Submit 提交任务
func (gp *GoroutinePool) Submit(task func()) error {
	gp.mu.Lock()
	if gp.closed {
		gp.mu.Unlock()
		return ErrPoolClosed
	}
	gp.mu.Unlock()

	gp.taskChan <- task
	return nil
}

// Close 关闭任务池
func (gp *GoroutinePool) Close() {
	gp.mu.Lock()
	if gp.closed {
		gp.mu.Unlock()
		return
	}
	gp.closed = true
	gp.mu.Unlock()

	close(gp.taskChan)
	gp.wg.Wait()
}

func (gp *GoroutinePool) worker() {
	defer gp.wg.Done()

	for task := range gp.taskChan {
		if task != nil {
			task()
		}
	}
}
