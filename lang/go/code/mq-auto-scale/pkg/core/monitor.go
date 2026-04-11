// 主机资源监控
package core

import (
	"fmt"
	"log/slog"
	"sync"
	"time"

	"github.com/shirou/gopsutil/v3/cpu"
	"github.com/shirou/gopsutil/v3/disk"
	"github.com/shirou/gopsutil/v3/load"
	"github.com/shirou/gopsutil/v3/mem"
)

// HostMonitorConfig 主机监控配置
type HostMonitorConfig struct {
	Enable            bool          // 是否启用资源监控
	CPUThreshold      float64       // CPU使用率阈值（百分比），超过则禁止扩容
	MemThreshold      float64       // 内存使用率阈值（百分比），超过则禁止扩容
	DiskThreshold     float64       // 磁盘使用率阈值（百分比）
	LoadThreshold     float64       // 系统负载阈值
	CheckInterval     time.Duration // 检查间隔
	ScaleUpBlockWait  time.Duration // 资源不足时阻塞扩容的最大等待时间
	EnableAutoRecover bool          // 是否启用自动恢复
}

// HostResourceStats 主机资源统计
type HostResourceStats struct {
	CPUUsage     float64 // CPU使用率百分比
	MemUsage     float64 // 内存使用率百分比
	MemAvailable uint64  // 可用内存（字节）
	MemTotal     uint64  // 总内存（字节）
	DiskUsage    float64 // 磁盘使用率百分比
	LoadAvg1     float64 // 1分钟平均负载
	LoadAvg5     float64 // 5分钟平均负载
	LoadAvg15    float64 // 15分钟平均负载
	Timestamp    time.Time
}

// ScaleUpRequest 扩容请求
type ScaleUpRequest struct {
	QueueName string
	RequestID string
	CreatedAt time.Time
	Callback  chan bool
}

// HostMonitor 主机监控器
type HostMonitor struct {
	config         *HostMonitorConfig
	currentStats   *HostResourceStats
	mu             sync.RWMutex
	stopChan       chan struct{}
	pendingReqs    map[string]*ScaleUpRequest
	pendingMu      sync.Mutex
	alertCallbacks []func(stats *HostResourceStats)
}

// NewHostMonitor 创建主机监控器
func NewHostMonitor(config *HostMonitorConfig) *HostMonitor {
	if config == nil {
		config = &HostMonitorConfig{
			Enable:            false,
			CPUThreshold:      80.0,
			MemThreshold:      85.0,
			DiskThreshold:     90.0,
			LoadThreshold:     10.0,
			CheckInterval:     5 * time.Second,
			ScaleUpBlockWait:  30 * time.Second,
			EnableAutoRecover: true,
		}
	}

	monitor := &HostMonitor{
		config:      config,
		pendingReqs: make(map[string]*ScaleUpRequest),
		stopChan:    make(chan struct{}),
	}

	if config.Enable {
		go monitor.startMonitoring()
		slog.Info("Host monitor started",
			slog.Float64("cpu_threshold", config.CPUThreshold),
			slog.Float64("mem_threshold", config.MemThreshold),
			slog.Duration("check_interval", config.CheckInterval),
		)
	}

	return monitor
}

// startMonitoring 启动资源监控
func (m *HostMonitor) startMonitoring() {
	ticker := time.NewTicker(m.config.CheckInterval)
	defer ticker.Stop()

	for {
		select {
		case <-m.stopChan:
			slog.Info("Host monitor stopped")
			return
		case <-ticker.C:
			m.collectStats()
		}
	}
}

// collectStats 收集资源统计信息
func (m *HostMonitor) collectStats() {
	stats := &HostResourceStats{
		Timestamp: time.Now(),
	}

	// 获取CPU使用率
	cpuPercent, err := cpu.Percent(0, false)
	if err != nil {
		slog.Warn("Failed to get CPU usage", "error", err)
	} else if len(cpuPercent) > 0 {
		stats.CPUUsage = cpuPercent[0]
	}

	// 获取内存使用率
	memInfo, err := mem.VirtualMemory()
	if err != nil {
		slog.Warn("Failed to get memory info", "error", err)
	} else {
		stats.MemUsage = memInfo.UsedPercent
		stats.MemAvailable = memInfo.Available
		stats.MemTotal = memInfo.Total
	}

	// 获取磁盘使用率（根分区）
	diskInfo, err := disk.Usage("/")
	if err != nil {
		slog.Warn("Failed to get disk info", "error", err)
	} else {
		stats.DiskUsage = diskInfo.UsedPercent
	}

	// 获取系统负载
	loadAvg, err := load.Avg()
	if err != nil {
		slog.Warn("Failed to get load average", "error", err)
	} else {
		stats.LoadAvg1 = loadAvg.Load1
		stats.LoadAvg5 = loadAvg.Load5
		stats.LoadAvg15 = loadAvg.Load15
	}

	m.mu.Lock()
	oldStats := m.currentStats
	m.currentStats = stats
	m.mu.Unlock()

	// 检查资源是否恢复正常
	if oldStats != nil && m.isResourceExhausted() && !m.isResourceExhaustedWithStats(oldStats) {
		slog.Info("Resource recovered",
			slog.Float64("cpu_usage", stats.CPUUsage),
			slog.Float64("mem_usage", stats.MemUsage),
		)
		m.notifyWaitingRequests()
	}

	// 触发告警回调
	if m.isResourceExhausted() {
		m.triggerAlerts(stats)
	}

	slog.Debug("Host resource stats",
		slog.Float64("cpu_usage", stats.CPUUsage),
		slog.Float64("mem_usage", stats.MemUsage),
		slog.Float64("disk_usage", stats.DiskUsage),
		slog.Float64("load_avg_1", stats.LoadAvg1),
	)
}

// isResourceExhausted 检查资源是否耗尽（禁止扩容）
func (m *HostMonitor) isResourceExhausted() bool {
	m.mu.RLock()
	defer m.mu.RUnlock()
	return m.isResourceExhaustedWithStats(m.currentStats)
}

// isResourceExhaustedWithStats 使用给定的统计信息检查资源是否耗尽
func (m *HostMonitor) isResourceExhaustedWithStats(stats *HostResourceStats) bool {
	if !m.config.Enable || stats == nil {
		return false
	}

	if stats.CPUUsage >= m.config.CPUThreshold {
		return true
	}

	if stats.MemUsage >= m.config.MemThreshold {
		return true
	}

	if stats.DiskUsage >= m.config.DiskThreshold {
		return true
	}

	// 检查系统负载
	if stats.LoadAvg1 >= m.config.LoadThreshold {
		return true
	}

	return false
}

// CanScaleUp 检查是否可以扩容
func (m *HostMonitor) CanScaleUp() bool {
	return !m.isResourceExhausted()
}

// GetCurrentStats 获取当前资源统计
func (m *HostMonitor) GetCurrentStats() *HostResourceStats {
	m.mu.RLock()
	defer m.mu.RUnlock()

	if m.currentStats == nil {
		return nil
	}

	// 返回副本
	stats := *m.currentStats
	return &stats
}

// RequestScaleUp 请求扩容（非阻塞）
func (m *HostMonitor) RequestScaleUp(queueName, requestID string) <-chan bool {
	ch := make(chan bool, 1)

	if m.CanScaleUp() {
		ch <- true
		return ch
	}

	// 加入等待队列
	req := &ScaleUpRequest{
		QueueName: queueName,
		RequestID: requestID,
		CreatedAt: time.Now(),
		Callback:  ch,
	}

	m.pendingMu.Lock()
	m.pendingReqs[requestID] = req
	m.pendingMu.Unlock()

	// 设置超时
	go func() {
		time.Sleep(m.config.ScaleUpBlockWait)
		m.pendingMu.Lock()
		if req, exists := m.pendingReqs[requestID]; exists {
			delete(m.pendingReqs, requestID)
			req.Callback <- false
			close(req.Callback)
		}
		m.pendingMu.Unlock()
	}()

	return ch
}

// WaitForScaleUp 等待直到可以扩容（阻塞）
func (m *HostMonitor) WaitForScaleUp(queueName string, timeout time.Duration) bool {
	if !m.config.Enable || m.CanScaleUp() {
		return true
	}

	slog.Info("Waiting for resources to scale up",
		slog.String("queue", queueName),
		slog.Duration("timeout", timeout),
	)

	requestID := fmt.Sprintf("%s-%d", queueName, time.Now().UnixNano())
	ch := m.RequestScaleUp(queueName, requestID)

	select {
	case result := <-ch:
		if result {
			slog.Info("Resource recovered, proceeding with scale up", "queue", queueName)
		} else {
			slog.Warn("Scale up timeout due to resource constraints", "queue", queueName)
		}
		return result
	case <-time.After(timeout):
		slog.Warn("Scale up timeout", "queue", queueName, "timeout", timeout)
		return false
	}
}

// notifyWaitingRequests 通知所有等待的扩容请求
func (m *HostMonitor) notifyWaitingRequests() {
	m.pendingMu.Lock()
	defer m.pendingMu.Unlock()

	for id, req := range m.pendingReqs {
		select {
		case req.Callback <- true:
			close(req.Callback)
			delete(m.pendingReqs, id)
			slog.Info("Notified waiting scale up request",
				slog.String("request_id", id),
				slog.String("queue", req.QueueName),
			)
		default:
		}
	}
}

// RegisterAlertCallback 注册告警回调
func (m *HostMonitor) RegisterAlertCallback(callback func(stats *HostResourceStats)) {
	m.alertCallbacks = append(m.alertCallbacks, callback)
}

// triggerAlerts 触发告警
func (m *HostMonitor) triggerAlerts(stats *HostResourceStats) {
	for _, callback := range m.alertCallbacks {
		go callback(stats)
	}
}

// GetResourceStatus 获取资源状态描述
func (m *HostMonitor) GetResourceStatus() string {
	if !m.config.Enable {
		return "disabled"
	}

	stats := m.GetCurrentStats()
	if stats == nil {
		return "unknown"
	}

	if m.isResourceExhausted() {
		return fmt.Sprintf("exhausted (CPU: %.1f%%, MEM: %.1f%%)", stats.CPUUsage, stats.MemUsage)
	}

	return fmt.Sprintf("healthy (CPU: %.1f%%, MEM: %.1f%%)", stats.CPUUsage, stats.MemUsage)
}

// Stop 停止监控
func (m *HostMonitor) Stop() {
	close(m.stopChan)
}
