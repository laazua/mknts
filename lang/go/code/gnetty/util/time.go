package util

import (
	"sync"
	"time"
)

// Timer 计时器
type Timer struct {
	startTime time.Time
}

// NewTimer 创建新的计时器
func NewTimer() *Timer {
	return &Timer{
		startTime: time.Now(),
	}
}

// Elapsed 获取经过的时间
func (t *Timer) Elapsed() time.Duration {
	return time.Since(t.startTime)
}

// ElapsedMillis 获取经过的毫秒数
func (t *Timer) ElapsedMillis() int64 {
	return t.Elapsed().Milliseconds()
}

// Reset 重置计时器
func (t *Timer) Reset() {
	t.startTime = time.Now()
}

// RateLimiter 速率限制器
type RateLimiter struct {
	capacity  int64
	fillRate  int64
	tokens    int64
	lastRefil time.Time
	mu        sync.Mutex
}

// NewRateLimiter 创建新的速率限制器
// capacity: 桶容量
// fillRate: 每秒填充的令牌数
func NewRateLimiter(capacity int64, fillRate int64) *RateLimiter {
	return &RateLimiter{
		capacity:  capacity,
		fillRate:  fillRate,
		tokens:    capacity,
		lastRefil: time.Now(),
	}
}

// Allow 检查是否允许操作
func (rl *RateLimiter) Allow() bool {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	now := time.Now()
	elapsed := now.Sub(rl.lastRefil).Seconds()
	rl.tokens += int64(elapsed * float64(rl.fillRate))

	if rl.tokens > rl.capacity {
		rl.tokens = rl.capacity
	}

	rl.lastRefil = now

	if rl.tokens > 0 {
		rl.tokens--
		return true
	}

	return false
}

// AllowN 检查是否允许 n 个操作
func (rl *RateLimiter) AllowN(n int64) bool {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	now := time.Now()
	elapsed := now.Sub(rl.lastRefil).Seconds()
	rl.tokens += int64(elapsed * float64(rl.fillRate))

	if rl.tokens > rl.capacity {
		rl.tokens = rl.capacity
	}

	rl.lastRefil = now

	if rl.tokens >= n {
		rl.tokens -= n
		return true
	}

	return false
}
