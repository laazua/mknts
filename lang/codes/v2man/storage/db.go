package storage

import (
	"fmt"
	"log"
	"v2man/pkg/config"
	"v2man/storage/model"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type DbHandler struct {
	DB *gorm.DB
}

func NewDbHandler(cfg *config.Config) *DbHandler {
	dsn := fmt.Sprintf("host=%v user=%v password=%v dbname=%v port=%v sslmode=disable TimeZone=Asia/Shanghai",
		cfg.DbHost, cfg.DbUser, cfg.DbPass, cfg.DbName, cfg.DbPort)
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		return nil
	}
	if !db.Migrator().HasTable("users") {
		db.AutoMigrate(&model.User{})
	}

	return &DbHandler{DB: db}
}

func (dbHandler *DbHandler) Close() {
	// 获取 *sql.DB 实例
	sqlDB, err := dbHandler.DB.DB()
	if err != nil {
		log.Fatalf("failed to get DB instance: %v", err)
	}

	// 确保在程序结束时关闭数据库连接
	defer func() {
		if err := sqlDB.Close(); err != nil {
			log.Fatalf("failed to close database: %v", err)
		}
		log.Println("Database connection closed.")
	}()
}
