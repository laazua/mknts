// 队列指标采集
package core

import (
	"crypto/tls"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"time"
)

type QueueStats struct {
	Name            string `json:"name"`
	Messages        int    `json:"messages"`
	MessagesReady   int    `json:"messages_ready"`
	MessagesUnacked int    `json:"messages_unacknowledged"`
	Consumers       int    `json:"consumers"`
	Memory          int64  `json:"memory"`
	IdleSince       string `json:"idle_since"`
}

type MQMetricsConfig struct {
	Host       string
	Port       int
	User       string
	Password   string
	Vhost      string
	Timeout    time.Duration
	MaxRetries int           // 最大重试次数
	RetryDelay time.Duration // 重试延迟
	UseSSL     bool          // 是否使用SSL
	Consumers  []any
}

type MQMetrics struct {
	config  *MQMetricsConfig
	client  *http.Client
	baseURL string
}

func NewMQMetrics(config *MQMetricsConfig) *MQMetrics {
	// 构建基础URL
	scheme := "http"
	if config.UseSSL {
		scheme = "https"
	}

	// URL编码vhost（vhost可能包含特殊字符如"/"）
	// encodedVhost := url.PathEscape(config.Vhost)
	baseURL := fmt.Sprintf("%s://%s:%d/api", scheme, config.Host, config.Port)

	// 创建HTTP客户端
	client := &http.Client{
		Timeout: config.Timeout,
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{InsecureSkipVerify: !config.UseSSL},
		},
	}

	return &MQMetrics{
		config:  config,
		client:  client,
		baseURL: baseURL,
	}
}

// doRequest 执行HTTP请求，支持重试
func (m *MQMetrics) doRequest(req *http.Request) (*http.Response, error) {
	var lastErr error

	for i := 0; i <= m.config.MaxRetries; i++ {
		if i > 0 {
			time.Sleep(m.config.RetryDelay)
		}

		resp, err := m.client.Do(req)
		if err == nil {
			return resp, nil
		}
		lastErr = err
	}

	return nil, fmt.Errorf("failed after %d retries: %w", m.config.MaxRetries, lastErr)
}

func (m *MQMetrics) GetQueueStats(vhost, queueName string) (*QueueStats, error) {
	// URL编码vhost和queueName
	encodedVhost := url.PathEscape(vhost)
	encodedQueue := url.PathEscape(queueName)
	url := fmt.Sprintf("%s/queues/%s/%s", m.baseURL, encodedVhost, encodedQueue)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}
	fmt.Println(m.config.User, m.config.Password)
	req.SetBasicAuth(m.config.User, m.config.Password)
	req.Header.Set("Content-Type", "application/json")

	resp, err := m.doRequest(req)
	if err != nil {
		return nil, fmt.Errorf("failed to execute request: %w", err)
	}
	defer resp.Body.Close()

	// 检查响应状态码
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	var stats QueueStats
	if err := json.NewDecoder(resp.Body).Decode(&stats); err != nil {
		return nil, fmt.Errorf("failed to decode response: %w", err)
	}
	fmt.Println("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
	return &stats, nil
}

func (m *MQMetrics) GetQueueDepth(vhost, queueName string) (int, error) {
	stats, err := m.GetQueueStats(vhost, queueName)
	if err != nil {
		return 0, err
	}
	return stats.MessagesReady, nil
}

// GetConsumerCount 获取队列的消费者数量
func (m *MQMetrics) GetConsumerCount(vhost, queueName string) (int, error) {
	stats, err := m.GetQueueStats(vhost, queueName)
	if err != nil {
		return 0, err
	}
	return stats.Consumers, nil
}

// IsQueueIdle 检查队列是否空闲
func (m *MQMetrics) IsQueueIdle(vhost, queueName string) (bool, error) {
	stats, err := m.GetQueueStats(vhost, queueName)
	if err != nil {
		return false, err
	}
	return stats.IdleSince != "", nil
}

// HealthCheck 健康检查
func (m *MQMetrics) HealthCheck() error {
	url := fmt.Sprintf("%s/health/checks/alarms", m.baseURL)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return err
	}
	req.SetBasicAuth(m.config.User, m.config.Password)

	resp, err := m.client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("rabbitMQ health check failed: %d", resp.StatusCode)
	}
	return nil
}
