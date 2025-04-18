package core

import (
	"context"
	"fmt"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

type Db struct {
	Pool *pgxpool.Pool
}

func NewDb() (*Db, error) {
	postgresUri := fmt.Sprintf(
		"postgres://%v:%v@%v:%v/%v?sslmode=disable",
		Setting.DbUser, Setting.DbPass, Setting.DbHost, Setting.DbPort, Setting.DbName,
	)
	conn, err := pgxpool.ParseConfig(postgresUri)
	if err != nil {
		// slog.Error(fmt.Sprintf("## 解析Postgresql配置失败: %v", err))
		panic(fmt.Sprintf("## 解析Postgresql配置失败: %v", err))
	}

	conn.MaxConns = Setting.DbConNum
	conn.MaxConnIdleTime = time.Duration(Setting.DbConIdleTime) * time.Minute

	dbPool, err := pgxpool.NewWithConfig(context.Background(), conn)
	if err != nil {
		// slog.Error(fmt.Sprintf("## 创建Postgresql连接池失败: %v", err))
		panic(fmt.Sprintf("## 创建Postgresql连接池失败: %v", err))
	}

	if err := dbPool.Ping(context.Background()); err != nil {
		panic(fmt.Sprintf("## Ping Postgres数据库失败: %v\n", err))
	}

	return &Db{dbPool}, err
}
