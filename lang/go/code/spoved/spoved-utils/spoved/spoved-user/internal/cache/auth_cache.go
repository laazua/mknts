package cache

import (
	"context"
	"errors"
	"time"

	"spoved-utils/db"

	"github.com/redis/go-redis/v9"
)

type RedisCache struct {
	client *redis.Client
}

func NewRedisCache() (*RedisCache, error) {
	if err := db.InitRedis(); err != nil {
		return nil, err
	}

	client := db.GetRedis()
	if client == nil {
		return nil, errors.New("failed to get redis client")
	}

	return &RedisCache{
		client: client,
	}, nil
}

// 所有方法都支持传入context
func (c *RedisCache) Set(ctx context.Context, key string, value interface{}, exp time.Duration) error {
	if c.client == nil {
		return errors.New("redis client is nil")
	}
	return c.client.Set(ctx, key, value, exp).Err()
}

func (c *RedisCache) Get(ctx context.Context, key string) (string, error) {
	if c.client == nil {
		return "", errors.New("redis client is nil")
	}

	value, err := c.client.Get(ctx, key).Result()
	if err != nil {
		if err == redis.Nil {
			return "", nil
		}
		return "", err
	}
	return value, nil
}

func (c *RedisCache) Delete(ctx context.Context, key string) error {
	if c.client == nil {
		return errors.New("redis client is nil")
	}
	return c.client.Del(ctx, key).Err()
}
