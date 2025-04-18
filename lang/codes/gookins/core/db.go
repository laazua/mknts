package core

import (
	"fmt"
	"gookins/model"
	"log/slog"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func init() {
	dsn := fmt.Sprintf("host=%v user=%v password=%v dbname=%v port=%v sslmode=disable TimeZone=Asia/Shanghai",
		Config.DbHost, Config.DbUser, Config.DbPass, Config.DbName, Config.DbPort)
	// once.Do(func() {
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic(err)
	}
	Db = db
	// Db.AutoMigrate(&model.User{})
	// Db.AutoMigrate(&model.Task{})
	if !Db.Migrator().HasTable("users") {
		slog.Info("迁移用户表")
		Db.AutoMigrate(&model.User{})
	}
	if !Db.Migrator().HasTable("tasks") {
		slog.Info("迁移任务表")
		Db.AutoMigrate(&model.Task{})
	}

	// })

}
