// 调度器实现 - 支持多队列
package core

import (
	"context"
	"log/slog"
	"sync"
	"time"
)

// QueueConfig 队列配置
type QueueConfig struct {
	Name               string
	ProgramName        string // 对应的 Supervisor 程序名
	MinConsumers       int
	MaxConsumers       int
	ScaleUpThreshold   int
	ScaleDownThreshold int
}

// SchedulerConfig 调度器配置
type SchedulerConfig struct {
	CheckInterval  time.Duration
	CooldownPeriod time.Duration

	// 队列配置列表
	Queues []QueueConfig

	// 资源监控相关配置
	EnableResourceMonitor bool
	CPUThreshold          float64
	MemThreshold          float64
	ResourceCheckInterval time.Duration
	ScaleUpBlockWait      time.Duration
}

// QueueMonitor 队列监控器
type QueueMonitor struct {
	config      QueueConfig
	rabbitMQ    *MQMetrics
	supervisor  *SupervisorManage
	currentSize int
	lastScale   time.Time
	mu          sync.RWMutex
}

// Scheduler 调度器
type Scheduler struct {
	config      *SchedulerConfig
	rabbitMQ    *MQMetrics
	supervisor  *SupervisorManage
	hostMonitor *HostMonitor
	monitors    map[string]*QueueMonitor
	ctx         context.Context
	cancel      context.CancelFunc
	wg          sync.WaitGroup
}

func NewScheduler(config *SchedulerConfig, mqConfig *MQMetricsConfig, supervisorConfig *SupervisorConfig) *Scheduler {
	ctx, cancel := context.WithCancel(context.Background())

	// 创建主机监控器
	monitorConfig := &HostMonitorConfig{
		Enable:           config.EnableResourceMonitor,
		CPUThreshold:     config.CPUThreshold,
		MemThreshold:     config.MemThreshold,
		CheckInterval:    config.ResourceCheckInterval,
		ScaleUpBlockWait: config.ScaleUpBlockWait,
	}

	scheduler := &Scheduler{
		config:      config,
		rabbitMQ:    NewMQMetrics(mqConfig),
		supervisor:  NewSupervisorManage(supervisorConfig),
		hostMonitor: NewHostMonitor(monitorConfig),
		monitors:    make(map[string]*QueueMonitor),
		ctx:         ctx,
		cancel:      cancel,
	}

	// 初始化所有队列监控器
	for _, queueConfig := range config.Queues {
		monitor := &QueueMonitor{
			config:      queueConfig,
			rabbitMQ:    scheduler.rabbitMQ,
			supervisor:  scheduler.supervisor,
			currentSize: 0,
			lastScale:   time.Now(),
		}
		scheduler.monitors[queueConfig.Name] = monitor
	}

	return scheduler
}

func (s *Scheduler) Start() {
	slog.Info("Scheduler started",
		slog.Int("queue_count", len(s.config.Queues)),
		slog.Duration("check_interval", s.config.CheckInterval),
	)

	// 打印所有队列配置
	for _, queue := range s.config.Queues {
		slog.Info("Queue configured",
			slog.String("queue_name", queue.Name),
			slog.String("program_name", queue.ProgramName),
			slog.Int("min_consumers", queue.MinConsumers),
			slog.Int("max_consumers", queue.MaxConsumers),
			slog.Int("scale_up_threshold", queue.ScaleUpThreshold),
			slog.Int("scale_down_threshold", queue.ScaleDownThreshold),
		)
	}

	// 初始化所有队列：确保最小消费者数量
	s.ensureMinConsumers()

	// 启动监控循环
	ticker := time.NewTicker(s.config.CheckInterval)
	defer ticker.Stop()

	for {
		select {
		case <-s.ctx.Done():
			slog.Info("Scheduler stopping...")
			s.hostMonitor.Stop()
			s.wg.Wait()
			return
		case <-ticker.C:
			s.reconcileAll()
		}
	}
}

// reconcileAll 协调所有队列
func (s *Scheduler) reconcileAll() {
	var wg sync.WaitGroup

	for _, monitor := range s.monitors {
		wg.Add(1)
		go func(m *QueueMonitor) {
			defer wg.Done()
			m.reconcile(s.config, s.hostMonitor)
		}(monitor)
	}

	wg.Wait()
}

// reconcile 单个队列的协调逻辑
func (m *QueueMonitor) reconcile(schedulerConfig *SchedulerConfig, hostMonitor *HostMonitor) {
	// 获取队列深度
	depth, err := m.rabbitMQ.GetQueueDepth("/", m.config.Name)
	if err != nil {
		slog.Error("Failed to get queue depth",
			slog.String("queue", m.config.Name),
			slog.String("error", err.Error()),
		)
		return
	}

	// 获取当前运行的消费者数量
	current, err := m.supervisor.GetRunningConsumerCount(m.config.ProgramName)
	if err != nil {
		slog.Error("Failed to get consumer count",
			slog.String("program", m.config.ProgramName),
			slog.String("error", err.Error()),
		)
		return
	}

	m.mu.Lock()
	m.currentSize = current
	m.mu.Unlock()

	slog.Info("Monitoring metrics",
		slog.String("queue", m.config.Name),
		slog.Int("queue_depth", depth),
		slog.Int("active_consumers", current),
		slog.Int("scale_up_threshold", m.config.ScaleUpThreshold),
		slog.Int("scale_down_threshold", m.config.ScaleDownThreshold),
	)

	// 检查冷却期
	if time.Since(m.lastScale) < schedulerConfig.CooldownPeriod {
		slog.Debug("In cooldown period, skipping scaling",
			slog.String("queue", m.config.Name),
			slog.Duration("remaining", schedulerConfig.CooldownPeriod-time.Since(m.lastScale)),
		)
		return
	}

	// 检查是否需要扩容
	if depth > m.config.ScaleUpThreshold && current < m.config.MaxConsumers {
		m.scaleUp(current, depth, schedulerConfig, hostMonitor)
		return
	}

	// 检查是否需要缩容
	if depth < m.config.ScaleDownThreshold && current > m.config.MinConsumers {
		m.scaleDown(current, depth, schedulerConfig)
		return
	}
}

// scaleUp 扩容
func (m *QueueMonitor) scaleUp(current int, queueDepth int, schedulerConfig *SchedulerConfig, hostMonitor *HostMonitor) {
	// 检查资源是否允许扩容
	if schedulerConfig.EnableResourceMonitor && !hostMonitor.CanScaleUp() {
		slog.Warn("Resource exhausted, waiting for scale up",
			slog.String("queue", m.config.Name),
		)

		if !hostMonitor.WaitForScaleUp(m.config.Name, schedulerConfig.ScaleUpBlockWait) {
			slog.Warn("Scale up cancelled due to resource constraints",
				slog.String("queue", m.config.Name),
			)
			return
		}
	}

	// 计算目标数量
	target := m.calculateTargetCount(current, true, queueDepth)
	if target <= current {
		return
	}

	slog.Info("Scaling up consumers",
		slog.String("queue", m.config.Name),
		slog.String("program", m.config.ProgramName),
		slog.Int("from", current),
		slog.Int("to", target),
		slog.Int("queue_depth", queueDepth),
	)

	// 更新 Supervisor 配置
	if err := m.supervisor.UpdateConsumerCount(m.config.ProgramName, target); err != nil {
		slog.Error("Failed to update consumer count",
			slog.String("program", m.config.ProgramName),
			slog.String("error", err.Error()),
		)
		return
	}

	m.mu.Lock()
	m.currentSize = target
	m.lastScale = time.Now()
	m.mu.Unlock()

	slog.Info("Scale up completed",
		slog.String("queue", m.config.Name),
		slog.Int("total_consumers", target),
	)
}

// scaleDown 缩容
func (m *QueueMonitor) scaleDown(current int, queueDepth int, schedulerConfig *SchedulerConfig) {
	target := m.calculateTargetCount(current, false, queueDepth)
	if target >= current {
		return
	}

	slog.Info("Scaling down consumers",
		slog.String("queue", m.config.Name),
		slog.String("program", m.config.ProgramName),
		slog.Int("from", current),
		slog.Int("to", target),
		slog.Int("queue_depth", queueDepth),
	)

	// 更新 Supervisor 配置
	if err := m.supervisor.UpdateConsumerCount(m.config.ProgramName, target); err != nil {
		slog.Error("Failed to update consumer count",
			slog.String("program", m.config.ProgramName),
			slog.String("error", err.Error()),
		)
		return
	}

	m.mu.Lock()
	m.currentSize = target
	m.lastScale = time.Now()
	m.mu.Unlock()

	slog.Info("Scale down completed",
		slog.String("queue", m.config.Name),
		slog.Int("total_consumers", target),
	)
}

// calculateTargetCount 计算目标消费者数量
func (m *QueueMonitor) calculateTargetCount(current int, isScaleUp bool, queueDepth int) int {
	if isScaleUp {
		// 根据队列深度动态计算扩容数量
		excess := queueDepth - m.config.ScaleUpThreshold
		increment := excess / m.config.ScaleUpThreshold
		if increment < 1 {
			increment = 1
		}
		if increment > 5 {
			increment = 5 // 单次最多增加5个
		}

		target := current + increment
		if target > m.config.MaxConsumers {
			target = m.config.MaxConsumers
		}
		return target
	}

	// 缩容：每次减少1个
	target := current - 1
	if target < m.config.MinConsumers {
		target = m.config.MinConsumers
	}
	return target
}

// ensureMinConsumers 确保最小消费者数量
func (s *Scheduler) ensureMinConsumers() {
	for _, monitor := range s.monitors {
		current, err := s.supervisor.GetRunningConsumerCount(monitor.config.ProgramName)
		if err != nil {
			slog.Error("Failed to get consumer count",
				slog.String("program", monitor.config.ProgramName),
				slog.String("error", err.Error()),
			)
			continue
		}

		if current < monitor.config.MinConsumers {
			slog.Info("Ensuring minimum consumers",
				slog.String("queue", monitor.config.Name),
				slog.String("program", monitor.config.ProgramName),
				slog.Int("current", current),
				slog.Int("minimum", monitor.config.MinConsumers),
			)
			monitor.scaleUp(current, 0, s.config, s.hostMonitor)
		}
	}
}

// Stop 停止调度器
func (s *Scheduler) Stop() {
	s.cancel()
}

// GetStatus 获取所有队列状态
func (s *Scheduler) GetStatus() map[string]any {
	status := make(map[string]any)

	for name, monitor := range s.monitors {
		monitor.mu.RLock()
		status[name] = map[string]any{
			"current_consumers": monitor.currentSize,
			"last_scale":        monitor.lastScale,
			"config":            monitor.config,
		}
		monitor.mu.RUnlock()
	}

	status["resource_status"] = s.hostMonitor.GetResourceStatus()

	return status
}
