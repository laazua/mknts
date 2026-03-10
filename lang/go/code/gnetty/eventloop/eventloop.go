package eventloop

import (
	"sync"
	"time"
)

// Task 事件循环任务
type Task struct {
	Name     string
	Callback func()
	Delay    time.Duration
}

// EventLoop 事件循环
type EventLoop struct {
	taskChan chan *Task
	stopChan chan struct{}
	wg       sync.WaitGroup
	once     sync.Once
	closed   bool
	mu       sync.RWMutex
}

// NewEventLoop 创建新的 EventLoop
func NewEventLoop() *EventLoop {
	return &EventLoop{
		taskChan: make(chan *Task, 1000),
		stopChan: make(chan struct{}),
	}
}

// Submit 提交任务
func (el *EventLoop) Submit(task *Task) error {
	el.mu.RLock()
	defer el.mu.RUnlock()

	if el.closed {
		return ErrEventLoopClosed
	}

	select {
	case el.taskChan <- task:
		return nil
	case <-el.stopChan:
		return ErrEventLoopClosed
	}
}

// Start 启动事件循环
func (el *EventLoop) Start() {
	el.mu.Lock()
	defer el.mu.Unlock()

	if el.closed {
		return
	}

	el.wg.Add(1)
	go el.run()
}

// Stop 停止事件循环
func (el *EventLoop) Stop() {
	el.mu.Lock()
	if el.closed {
		el.mu.Unlock()
		return
	}
	el.closed = true
	el.mu.Unlock()

	el.once.Do(func() {
		close(el.stopChan)
	})
	el.wg.Wait()
}

func (el *EventLoop) run() {
	defer el.wg.Done()

	for {
		select {
		case task := <-el.taskChan:
			if task != nil && task.Callback != nil {
				if task.Delay > 0 {
					time.Sleep(task.Delay)
				}
				task.Callback()
			}
		case <-el.stopChan:
			return
		}
	}
}

// IsClosed 检查 EventLoop 是否关闭
func (el *EventLoop) IsClosed() bool {
	el.mu.RLock()
	defer el.mu.RUnlock()
	return el.closed
}
