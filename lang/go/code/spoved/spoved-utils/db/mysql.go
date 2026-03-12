// 数据库实现
package db

import (
	"database/sql"
	"time"

	"spoved-utils/config"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var (
	sqlDB  *sql.DB
	gormDB *gorm.DB
)

type MySQL struct {
	host     string
	port     int
	user     string
	password string
	dbName   string
}

func NewMySQL() *MySQL {
	return &MySQL{
		host:     config.Get().Database.Host,
		port:     config.Get().Database.Port,
		user:     config.Get().Database.Username,
		password: config.Get().Database.Password,
		dbName:   config.Get().Database.DBName,
	}
}

func InitMySQL() error {
	mysqlInstance := NewMySQL()
	if err := mysqlInstance.connect(); err != nil {
		return err
	}
	return nil
}

// 连接数据库的逻辑
func (m *MySQL) connect() error {
	gormDB, err := gorm.Open(mysql.New(mysql.Config{
		DSN:                       config.Get().DbDSN(),
		SkipInitializeWithVersion: false,
	}), &gorm.Config{
		// Logger: logger.Default.LogMode(logger.Info),
	})
	if err != nil {
		return err
	}

	sqlDB, err := gormDB.DB()
	if err != nil {
		return err
	}
	// 设置连接池参数
	sqlDB.SetMaxIdleConns(100)                 // 最大空闲连接数
	sqlDB.SetMaxOpenConns(50)                  // 最大打开连接数
	sqlDB.SetConnMaxLifetime(5 * time.Second)  // 连接的最大存活时间
	sqlDB.SetConnMaxIdleTime(30 * time.Second) // 最大空闲连接时间
	// Ping 数据库检查连接是否正常
	if err := sqlDB.Ping(); err != nil {
		return err
	}
	return nil
}

// 数据库操作方法
func (m *MySQL) Operate() *gorm.DB {
	if gormDB != nil {
		return gormDB
	}
	err := m.connect()
	if err != nil {
		return nil
	}
	return gormDB
}

func SqlOpt() *gorm.DB {
	if gormDB != nil {
		return gormDB
	}
	return nil
}

// 关闭数据库连接
func CloseMySQL() error {
	if sqlDB != nil {
		if err := sqlDB.Close(); err != nil {
			return err
		} else {
			return nil
		}
	}
	return nil
}
