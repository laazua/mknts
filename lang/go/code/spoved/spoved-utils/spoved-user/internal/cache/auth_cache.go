package cache

import (
	"context"
	"time"

	"spoved-utils/db"
)

type RedisCache struct {
	rds *db.Redis
}

func NewRedisCache() *RedisCache {
	return &RedisCache{
		rds: db.NewRedis(),
	}
}

func (c *RedisCache) Set(key string, value string, exp time.Duration) error {
	ctx := context.Background()
	if _, err := c.rds.Operate().Set(ctx, key, value, exp).Result(); err != nil {
		return err
	}
	return nil
}

func (c *RedisCache) Get(key string) (string, error) {
	ctx := context.Background()
	value, err := c.rds.Operate().Get(ctx, key).Result()
	if err != nil {
		return "", err
	}
	return value, nil
}

func (c *RedisCache) Delete(key string) error {
	ctx := context.Background()
	_, err := c.rds.Operate().Del(ctx, key).Result()
	if err != nil {
		return err
	}
	return nil
}
