package storage

import (
	"context"
	"database/sql"
	"log"
	"msite/pkg/env"
	"msite/pkg/storage/model"
	"os"
	"os/signal"
	"syscall"
	"time"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

var db *gorm.DB

func LoadGdb() {
	gdb, err := gorm.Open(postgres.Open(os.Getenv("storage.db.uri")), &gorm.Config{
		Logger: logger.Default.LogMode(logger.Silent), // 不输出日志

	})
	if err != nil {
		panic(err)
	}
	sqlGdb, err := gdb.DB()
	if err != nil {
		panic(err)
	}
	defer sqlGdb.Close()

	sqlGdb.SetConnMaxLifetime(env.ParseTDuration(os.Getenv("storage.db.conn.lifetime")))
	sqlGdb.SetMaxIdleConns(env.StoInt(os.Getenv("storage.db.conn.max.idle")))
	sqlGdb.SetMaxOpenConns(env.StoInt(os.Getenv("storage.db.conn.max.open")))

	ctx, stop := context.WithCancel(context.Background())
	defer stop()

	appSignal := make(chan os.Signal, 3)
	signal.Notify(appSignal, os.Interrupt, syscall.SIGABRT, syscall.SIGINT)

	go func() { <-appSignal; stop() }()

	ping(ctx, sqlGdb)

	db = gdb

	// 迁移表
	if !gdb.Migrator().HasTable("user") {
		gdb.AutoMigrate(&model.User{})
	}
}

func ping(ctx context.Context, db *sql.DB) {
	ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
	defer cancel()

	if err := db.PingContext(ctx); err != nil {
		log.Fatalf("unable to connect to database: %v", err)
	}
}
