package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// 定义任务的状态
const (
	TaskStatusPending   = "Pending"
	TaskStatusRunning   = "Running"
	TaskStatusCompleted = "Completed"
	TaskStatusCancelled = "Cancelled"
	TaskStatusFailed    = "Failed"
)

// 定义任务池满时的处理策略
const (
	StrategyBlock      = "Block"      // 阻塞等待
	StrategyDrop       = "Drop"       // 丢弃新任务
	StrategyDropOldest = "DropOldest" // 丢弃最旧的任务
	StrategyExpand     = "Expand"     // 动态扩容
)

// Step 表示一个任务中的步骤
type Step struct {
	Name string
	Cmd  string
}

// Task 表示一个任务
type Task struct {
	ID     string
	Name   string
	Steps  []Step
	Status string // 任务状态
	mu     sync.Mutex
}

// TaskPool 表示任务池
type TaskPool struct {
	tasks       chan *Task                    // 存储待执行任务的 channel
	workerCount int                           // 并发任务数
	mu          sync.Mutex                    // 用于任务池并发控制
	cancelFuncs map[string]context.CancelFunc // 存储每个任务的取消函数
	taskStatus  map[string]*Task              // 存储任务状态
	strategy    string                        // 任务池满时的处理策略
}

// NewTaskPool 创建一个新的任务池
func NewTaskPool(size, workerCount int, strategy string) *TaskPool {
	return &TaskPool{
		tasks:       make(chan *Task, size), // 设置任务池的容量
		workerCount: workerCount,            // 设置并发任务数量
		cancelFuncs: make(map[string]context.CancelFunc),
		taskStatus:  make(map[string]*Task), // 存储任务状态
		strategy:    strategy,               // 设置策略
	}
}

// AddTask 添加任务到任务池
func (p *TaskPool) AddTask(task *Task) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	// 设置任务初始状态为 Pending
	task.Status = TaskStatusPending
	p.taskStatus[task.ID] = task

	switch p.strategy {
	case StrategyBlock:
		// 阻塞直到任务池有空间
		p.tasks <- task
		fmt.Printf("任务 %s 已加入任务池（阻塞策略）\n", task.Name)
	case StrategyDrop:
		// 尝试放入任务池，满了就丢弃
		select {
		case p.tasks <- task:
			fmt.Printf("任务 %s 已加入任务池\n", task.Name)
		default:
			fmt.Printf("任务池已满，任务 %s 被丢弃\n", task.Name)
			return fmt.Errorf("任务池已满")
		}
	case StrategyDropOldest:
		// 如果任务池满了，丢弃最早的任务，加入新任务
		select {
		case p.tasks <- task:
			fmt.Printf("任务 %s 已加入任务池\n", task.Name)
		default:
			// 丢弃最早的任务并插入新任务
			<-p.tasks
			p.tasks <- task
			fmt.Printf("任务池已满，丢弃最旧任务，任务 %s 已加入任务池\n", task.Name)
		}
	case StrategyExpand:
		// 动态扩容任务池
		select {
		case p.tasks <- task:
			fmt.Printf("任务 %s 已加入任务池\n", task.Name)
		default:
			// 动态增加池容量
			fmt.Println("任务池已满，动态扩容中...")
			newTasks := make(chan *Task, cap(p.tasks)*2)
			close(p.tasks)
			for t := range p.tasks {
				newTasks <- t
			}
			p.tasks = newTasks
			p.tasks <- task
			fmt.Printf("任务池扩容后，任务 %s 已加入任务池\n", task.Name)
		}
	}
	return nil
}

// Start 开始处理任务池中的任务
func (p *TaskPool) Start() {
	for i := 0; i < p.workerCount; i++ {
		go p.worker()
	}
}

// worker 表示具体的任务处理逻辑
func (p *TaskPool) worker() {
	for task := range p.tasks {
		p.runTask(task)
	}
}

// runTask 执行任务，并更新任务状态
func (p *TaskPool) runTask(task *Task) {
	ctx, cancel := context.WithCancel(context.Background())
	p.mu.Lock()
	p.cancelFuncs[task.ID] = cancel
	p.mu.Unlock()

	// 设置任务状态为 Running
	task.mu.Lock()
	task.Status = TaskStatusRunning
	task.mu.Unlock()

	fmt.Printf("开始执行任务 %s\n", task.Name)
	for _, step := range task.Steps {
		select {
		case <-ctx.Done():
			// 设置任务状态为 Cancelled
			task.mu.Lock()
			task.Status = TaskStatusCancelled
			task.mu.Unlock()

			fmt.Printf("任务 %s 被取消\n", task.Name)
			return
		default:
			fmt.Printf("执行步骤 %s: %s\n", step.Name, step.Cmd)
			time.Sleep(1 * time.Second) // 模拟执行时间
		}
	}

	// 任务执行完成，更新任务状态为 Completed
	task.mu.Lock()
	task.Status = TaskStatusCompleted
	task.mu.Unlock()

	p.mu.Lock()
	delete(p.cancelFuncs, task.ID)
	p.mu.Unlock()

	fmt.Printf("任务 %s 执行完成\n", task.Name)
}

// CancelTask 取消指定任务
func (p *TaskPool) CancelTask(taskID string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	if cancel, exists := p.cancelFuncs[taskID]; exists {
		cancel()
		fmt.Printf("任务 %s 已取消\n", taskID)
	} else {
		fmt.Printf("任务 %s 未找到或已完成\n", taskID)
	}
}

// GetTaskStatus 获取任务状态
func (p *TaskPool) GetTaskStatus(taskID string) string {
	p.mu.Lock()
	defer p.mu.Unlock()
	if task, exists := p.taskStatus[taskID]; exists {
		task.mu.Lock()
		defer task.mu.Unlock()
		return task.Status
	}
	return "任务未找到"
}

func main() {
	// 创建任务池，容量为3，允许并发执行2个任务，策略为丢弃最旧任务
	pool := NewTaskPool(3, 2, StrategyDropOldest)

	// 启动任务池
	pool.Start()

	// 模拟从前端获取的任务数据
	task1 := &Task{
		ID:   "1",
		Name: "taskNameTest1",
		Steps: []Step{
			{Name: "stepNameOne", Cmd: "echo step one"},
			{Name: "stepNameTwo", Cmd: "echo step two"},
		},
	}

	task2 := &Task{
		ID:   "2",
		Name: "taskNameTest2",
		Steps: []Step{
			{Name: "stepNameOne", Cmd: "echo step one"},
			{Name: "stepNameThree", Cmd: "echo step three"},
		},
	}

	task3 := &Task{
		ID:   "3",
		Name: "taskNameTest3",
		Steps: []Step{
			{Name: "stepNameOne", Cmd: "echo step one"},
			{Name: "stepNameThree", Cmd: "echo step three"},
		},
	}

	task4 := &Task{
		ID:   "4",
		Name: "taskNameTest4",
		Steps: []Step{
			{Name: "stepNameOne", Cmd: "echo step one"},
			{Name: "stepNameThree", Cmd: "echo step three"},
		},
	}

	fmt.Println("xxxxxxxx: ", task4)
	// 添加任务到任务池
	pool.AddTask(task1)
	pool.AddTask(task2)
	pool.AddTask(task3)
	pool.AddTask(task4)

	// 获取任务状态
	fmt.Println("任务 1 状态:", pool.GetTaskStatus("1"))
	fmt.Println("任务 2 状态:", pool.GetTaskStatus("2"))
	fmt.Println("任务 3 状态:", pool.GetTaskStatus("3"))
	fmt.Println("任务 4 状态:", pool.GetTaskStatus("4"))

	// 防止主进程退出
	time.Sleep(10 * time.Second)
}
