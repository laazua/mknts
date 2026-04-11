package main

import (
	"fmt"
	"log/slog"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"

	"mq-auto-scale/pkg/comm"
	"mq-auto-scale/pkg/core"
)

func main() {
	// 配置日志
	setupLogging()

	// 验证必要配置
	if err := validateConfig(); err != nil {
		slog.Error("Configuration validation failed", "error", err)
		return
	}
	if err := comm.LoadDefaultEnv(); err != nil {
		slog.Error("加载配置失败", "error", err)
		return
	}
	// supervisor配置
	supervisorConfig := &core.SupervisorConfig{
		URL:       comm.Env().Str("SUPERVISOR_URL", "http://localhost:9001/RPC2"),
		Username:  comm.Env().Str("SUPERVISOR_USER", ""),
		Password:  comm.Env().Str("SUPERVISOR_PASSWORD", ""),
		Timeout:   comm.Env().Duration("SUPERVISOR_TIMEOUT", 10*time.Second),
		ConfigDir: comm.Env().Str("SUPERVISOR_CONFIG_DIR", "/etc/supervisord.d/"),
	}

	// mq配置
	mqConfig := &core.MQMetricsConfig{
		Host:       comm.Env().Str("MQ_HOST", ""),
		Port:       comm.Env().Int("MQ_PORT", 5672),
		User:       comm.Env().Str("MQ_USER", "guest"),
		Password:   comm.Env().Str("MQ_PASSWD", "123456"),
		Vhost:      comm.Env().Str("MQ_VHOST", "/"),
		Timeout:    comm.Env().Duration("MQ_TIMEOUT", 5*time.Second),
		MaxRetries: comm.Env().Int("MQ_MAX_RETRIES", 3),
		RetryDelay: comm.Env().Duration("MQ_RETRY_DELAY", 1*time.Second),
		UseSSL:     comm.Env().Bool("MQ_USE_SSL", false),
		Consumers:  comm.Env().List("CONSUMER_QUEUES"),
	}

	// 调度器配置
	schedulerConfig := &core.SchedulerConfig{
		CheckInterval:         comm.Env().Duration("CHECK_INTERVAL", 5*time.Second),
		CooldownPeriod:        comm.Env().Duration("COOLDOWN_PERIOD", 30*time.Second),
		EnableResourceMonitor: comm.Env().Bool("ENABLE_RESOURCE_MONITOR", true),
		CPUThreshold:          comm.Env().Float("CPU_THRESHOLD", 80.0),
		MemThreshold:          comm.Env().Float("MEM_THRESHOLD", 85.0),
		ResourceCheckInterval: comm.Env().Duration("RESOURCE_CHECK_INTERVAL", 5*time.Second),
		ScaleUpBlockWait:      comm.Env().Duration("SCALE_UP_BLOCK_WAIT", 30*time.Second),
		Queues:                loadQueueConfigs(), // 从环境变量加载队列配置
	}

	// 打印配置信息
	printConfig(schedulerConfig, mqConfig, supervisorConfig)

	// 创建调度器
	scheduler := core.NewScheduler(schedulerConfig, mqConfig, supervisorConfig)

	// 设置信号处理
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)

	// 启动调度器
	go scheduler.Start()

	// 等待信号
	<-sigChan
	slog.Info("Shutting down...")
	scheduler.Stop()
	time.Sleep(5 * time.Second)
	slog.Info("Shutdown complete")
}

// loadQueueConfigs 加载队列配置
func loadQueueConfigs() []core.QueueConfig {
	queues := []core.QueueConfig{}

	// 方式1：从环境变量读取队列列表
	queueNames := comm.Env().Str("QUEUE_NAMES", "")
	if queueNames != "" {
		for queueName := range strings.SplitSeq(queueNames, ",") {
			queueName = strings.TrimSpace(queueName)
			programName := comm.Env().Str(queueName+"_PROGRAM", queueName)

			queue := core.QueueConfig{
				Name:               queueName,
				ProgramName:        programName,
				MinConsumers:       comm.Env().Int(queueName+"_MIN_CONSUMER", 1),
				MaxConsumers:       comm.Env().Int(queueName+"_MAX_CONSUMER", 5),
				ScaleUpThreshold:   comm.Env().Int(queueName+"_SCALE_UP_THRESHOLD", 10),
				ScaleDownThreshold: comm.Env().Int(queueName+"_SCALE_DOWN_THRESHOLD", 2),
			}
			queues = append(queues, queue)
		}
	}

	// 方式2：如果没有配置队列列表，尝试自动发现 Supervisor 配置
	if len(queues) == 0 {
		slog.Info("No queue names configured, will auto-discover from Supervisor")
		// 可以在运行时自动发现
	}

	return queues
}

func setupLogging() {
	logLevel := slog.LevelInfo
	if comm.Env().Bool("DEBUG", false) {
		logLevel = slog.LevelDebug
	}

	jsonHandler := slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
		Level: logLevel,
	})
	textHandler := slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{
		Level: logLevel,
	})
	if comm.Env().Str("LOG_FORMAT", "text") == "json" {
		slog.SetDefault(slog.New(jsonHandler))
	} else {
		slog.SetDefault(slog.New(textHandler))
	}
}

func validateConfig() error {
	// 验证必要配置
	if comm.Env().Str("QUEUE_NAMES", "") == "" {
		slog.Warn("QUEUE_NAMES not set, will auto-discover programs")
	}
	return nil
}

func printConfig(schedulerConfig *core.SchedulerConfig, mqConfig *core.MQMetricsConfig, supervisorConfig *core.SupervisorConfig) {
	// slog.Info("Configuration loaded",
	// 	slog.Int("queue_count", len(schedulerConfig.Queues)),
	// 	slog.Duration("check_interval", schedulerConfig.CheckInterval),
	// 	slog.Bool("resource_monitor_enabled", schedulerConfig.EnableResourceMonitor),
	// 	slog.String("mq_host", mqConfig.Host),
	// 	slog.String("supervisor_config_dir", supervisorConfig.ConfigDir),
	// )
	slog.Info("Queue Count", "queue_count", len(schedulerConfig.Queues))
	slog.Info("Check Interval", "check_interval", schedulerConfig.CheckInterval)
	slog.Info("Resource Monitor Enabled", "resource_monitor_enabled", schedulerConfig.EnableResourceMonitor)
	slog.Info("MQ Host", "mq_host", mqConfig.Host)
	slog.Info("Supervisor Config Dir", "supervisor_config_dir", supervisorConfig.ConfigDir)

	// 测试列表
	for _, queue := range comm.Env().List("CONSUMER_QUEUES") {
		q := queue.(map[string]any)
		fmt.Println(q)
	}
}
