package core

import (
	"context"
	"errors"
	"fmt"
	"log/slog"
	"os/exec"
	"sync"

	"gookins/model"

	"gopkg.in/yaml.v3"
)

type TaskJob model.TaskForm

var (
	ErrTaskPoolFull = errors.New("task pool is full")
)

const (
	StrategyBlock  = "block"
	StrategyDrop   = "drop"
	StrategyExpand = "expand"

	TaskPending   = "pending"
	TaskRunning   = "running"
	TaskFailure   = "failure"
	TaskCancelled = "cancelled"
	TaskCompleted = "completed"
)

type TaskPool struct {
	queue       chan *TaskJob
	wg          sync.WaitGroup
	cancelFuncs sync.Map
	states      sync.Map
	strategy    string
	ctx         context.Context
	cancel      context.CancelFunc
	mu          sync.Mutex
}

func NewTaskPool(ctx context.Context) *TaskPool {
	ctx, cancel := context.WithCancel(ctx)
	return &TaskPool{
		queue:    make(chan *TaskJob, Config.TaskPoolSize),
		strategy: Config.Strategy,
		ctx:      ctx,
		cancel:   cancel,
	}
}

func (tp *TaskPool) AddTask(task *TaskJob) error {
	tp.states.Store(task.Name, TaskPending)

	switch tp.strategy {
	case StrategyBlock:
		tp.queue <- task
		slog.Info(fmt.Sprintf("Task: %s is added to the pool", task.Name))
	case StrategyDrop:
		select {
		case tp.queue <- task:
			slog.Info(fmt.Sprintf("Task %s added to the pool", task.Name))
		default:
			slog.Info(fmt.Sprintf("Task pool is full, task %s dropped", task.Name))
			return ErrTaskPoolFull
		}
	case StrategyExpand:
		tp.mu.Lock()
		select {
		case tp.queue <- task:
			slog.Info(fmt.Sprintf("Task %s added to the pool", task.Name))
		default:
			slog.Info("Task pool is full, expanding...")
			newTasks := make(chan *TaskJob, cap(tp.queue)*2)
			close(tp.queue)
			for t := range tp.queue {
				newTasks <- t
			}
			tp.queue = newTasks
			tp.queue <- task
			slog.Info(fmt.Sprintf("Task pool expanded, task %s added", task.Name))
		}
		tp.mu.Unlock()
	}
	return nil
}

func (tp *TaskPool) start() {
	for i := 0; i < Config.WorkerCount; i++ {
		tp.wg.Add(1)
		go tp.worker()
	}
}

func (tp *TaskPool) Stop() {
	tp.cancel()
	// close(tp.queue)
	tp.wg.Wait()
}

func (tp *TaskPool) worker() {
	slog.Info("worker ...")
	defer tp.wg.Done()
	for {
		select {
		case <-tp.ctx.Done():
			return
		case task, ok := <-tp.queue:
			if !ok {
				slog.Info(fmt.Sprintf("Task: %s in worker!!", task.Name))
				return
			}
			ctx, cancel := context.WithCancel(tp.ctx)
			tp.cancelFuncs.Store(task.Name, cancel)
			slog.Info(fmt.Sprintf("run task: %v", task.Name))

			tp.executeTask(ctx, task)

			tp.cancelFuncs.Delete(task.Name)
		}
	}
}

func (tp *TaskPool) CancelTask(taskName string) bool {
	if cancel, ok := tp.cancelFuncs.Load(taskName); ok {
		cancel.(context.CancelFunc)()
		tp.cancelFuncs.Delete(taskName)
		return true
	}
	return false
}

func (tp *TaskPool) GetTaskStatus(name string) (string, bool) {
	status, exists := tp.states.Load(name)
	if !exists {
		return "", false
	}
	return status.(string), true
}

type pipeLine struct {
	Name  string `yaml:"name"`
	Steps []step `yaml:"steps"`
}

type step struct {
	Name    string `yaml:"name"`
	Command string `yaml:"command"`
}

func (tp *TaskPool) executeTask(ctx context.Context, task *TaskJob) {
	var pipeline pipeLine
	err := yaml.Unmarshal([]byte(task.PipeLine), &pipeline)
	if err != nil {
		slog.Error(fmt.Sprintf("Failed to unmarshal pipeline: %v", err))
		tp.states.Store(task.Name, TaskFailure)
		return
	}
	for _, step := range pipeline.Steps {
		select {
		case <-ctx.Done():
			slog.Info(fmt.Sprintf("Cancelled: %v", step.Name))
			tp.states.Store(task.Name, TaskCancelled)
			return
		default:
			tp.states.Store(task.Name, TaskRunning)
			slog.Info(fmt.Sprintf("Executing step: %v, Command: %v", step.Name, step.Command))
			cmd := exec.CommandContext(ctx, "bash", "-c", step.Command)
			output, err := cmd.CombinedOutput()
			if err != nil {
				tp.states.Store(task.Name, TaskFailure)
				slog.Error(fmt.Sprintf("Error executing command: %v, Output: %s", err, output))
				return
			}
			slog.Info(fmt.Sprintf("Step: %v, Command: %v, Output: %s", step.Name, step.Command, output))
		}
	}
	tp.states.Store(task.Name, TaskCompleted)
}

func init() {
	Tp = NewTaskPool(context.Background())
	go Tp.start()
}
