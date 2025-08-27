package db

import (
	"fmt"
	"layershow/internal/model"
	"layershow/pkg/config"
	"sync"
	"time"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var (
	db      *gorm.DB
	initErr error
	mu      sync.Mutex
)

func Init() error {
	mu.Lock()
	defer mu.Unlock()
	if db != nil && initErr == nil {
		return nil
	}
	dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%v sslmode=disable TimeZone=Asia/Shanghai",
		config.Get().DBHost, config.Get().DBUser, config.Get().DBPass, config.Get().DBName, config.Get().DBPort)
	var err error
	//db, err = gorm.Open(postgres.Open(dsn), &gorm.Config{
	//	Logger: logger.Default.LogMode(logger.Info),
	//})
	db, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		initErr = fmt.Errorf("打开数据库失败: %w", err)
		return initErr
	}
	sqlDB, err := db.DB()
	if err != nil {
		initErr = fmt.Errorf("获取数据库句柄失败: %w", err)
		return initErr
	}
	sqlDB.SetMaxIdleConns(config.Get().DBIdle)
	sqlDB.SetMaxOpenConns(config.Get().DBPool)
	sqlDB.SetConnMaxLifetime(time.Duration(config.Get().DBLifeTime))
	if err := sqlDB.Ping(); err != nil {
		initErr = fmt.Errorf("ping数据库连接失败: %w", err)
		return initErr
	}
	if err := db.AutoMigrate(&model.User{}); err != nil {
		initErr = fmt.Errorf("数据库表迁移失败: %w", err)
		return initErr
	}
	initErr = nil
	return nil
}

func Get() (*gorm.DB, error) {
	if err := Init(); err != nil {
		return nil, err
	}
	return db, nil
}

func Close() error {
	mu.Lock()
	defer mu.Unlock()

	if db != nil {
		sqlDB, err := db.DB()
		if err != nil {
			return err
		}
		return sqlDB.Close()
	}
	return nil
}
