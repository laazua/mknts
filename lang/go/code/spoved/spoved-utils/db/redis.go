package db

import (
	"spoved-utils/config"

	"github.com/redis/go-redis/v9"
)

var rds *redis.Client

// 缓存实现
type Redis struct {
	Host     string
	Port     int
	Password string
	DB       int
}

func NewRedis() *Redis {
	return &Redis{
		Host:     "",
		Port:     6379,
		Password: "",
		DB:       0,
	}
}

func InitRedis() error {
	redisInstance := NewRedis()
	if err := redisInstance.connect(); err != nil {
		return err
	}
	return nil
}

// 连接缓存的逻辑
func (r *Redis) connect() error {
	opt, err := redis.ParseURL(config.Get().RdsAddr())
	if err != nil {
		panic(err)
	}
	rds = redis.NewClient(opt)
	return nil
}

// 获取缓存连接
func (r *Redis) Operate() *redis.Client {
	if rds != nil {
		return rds
	}
	err := r.connect()
	if err != nil {
		return nil
	}
	return rds
}

// 关闭缓存连接
func CloseRedis() error {
	if rds != nil {
		return rds.Close()
	}
	return nil
}
