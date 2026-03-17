package db

import (
	"spoved-utils/config"
	"sync"

	"github.com/redis/go-redis/v9"
)

var (
	rds     *redis.Client
	once    sync.Once
	initErr error
)

// 简化为单例模式
func InitRedis() error {
	once.Do(func() {
		opt, err := redis.ParseURL(config.Get().RdsAddr())
		if err != nil {
			initErr = err
			return
		}
		rds = redis.NewClient(opt)
	})
	return initErr
}

// 获取客户端
func GetRedis() *redis.Client {
	return rds
}

// 关闭连接
func CloseRedis() error {
	if rds != nil {
		return rds.Close()
	}
	return nil
}
