package db

import (
	"database/sql"
	"sync"
	"time"

	"spoved-utils/config"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var (
	dbInstance *MySQL
	dbOnce     sync.Once
	dbInitErr  error
)

type MySQL struct {
	host     string
	port     int
	user     string
	password string
	dbName   string
	gormDB   *gorm.DB
	sqlDB    *sql.DB
	mu       sync.RWMutex // 用于保护内部连接
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
	dbOnce.Do(func() {
		dbInstance = NewMySQL()
		dbInitErr = dbInstance.connect()
	})
	return dbInitErr
}

func (m *MySQL) connect() error {
	m.mu.Lock()
	defer m.mu.Unlock()

	if m.gormDB != nil {
		return nil
	}

	gormDB, err := gorm.Open(mysql.New(mysql.Config{
		DSN: config.Get().DbDSN(),
	}), &gorm.Config{})
	if err != nil {
		return err
	}

	sqlDB, err := gormDB.DB()
	if err != nil {
		return err
	}

	// 调整连接池参数
	sqlDB.SetMaxIdleConns(25)                 // 空闲连接数建议小于最大连接数
	sqlDB.SetMaxOpenConns(50)                 // 最大打开连接数
	sqlDB.SetConnMaxLifetime(5 * time.Minute) // 增加存活时间
	sqlDB.SetConnMaxIdleTime(30 * time.Minute)

	if err := sqlDB.Ping(); err != nil {
		return err
	}

	m.gormDB = gormDB
	m.sqlDB = sqlDB
	return nil
}

func (m *MySQL) Operate() (*gorm.DB, error) {
	m.mu.RLock()
	if m.gormDB != nil {
		defer m.mu.RUnlock()
		return m.gormDB, nil
	}
	m.mu.RUnlock()

	// 尝试重新连接
	m.mu.Lock()
	defer m.mu.Unlock()

	if m.gormDB != nil {
		return m.gormDB, nil
	}

	err := m.connect()
	if err != nil {
		return nil, err
	}
	return m.gormDB, nil
}

// 获取默认实例（单例）
func GetDB() (*gorm.DB, error) {
	if dbInstance == nil {
		if err := InitMySQL(); err != nil {
			return nil, err
		}
	}
	return dbInstance.Operate()
}

func MergeTable(tables ...interface{}) error {
	db, err := GetDB()
	if err != nil {
		return err
	}

	for _, table := range tables {
		// 创建表
		if !db.Migrator().HasTable(table) {
			if err := db.Migrator().CreateTable(table); err != nil {
				return err
			}
		}
		// 自动迁移 - 直接传递 table，而不是 &table
		if err := db.AutoMigrate(table); err != nil {
			return err
		}
	}
	return nil
}

func CloseMySQL() error {
	if dbInstance == nil {
		return nil
	}

	dbInstance.mu.Lock()
	defer dbInstance.mu.Unlock()

	if dbInstance.sqlDB != nil {
		if err := dbInstance.sqlDB.Close(); err != nil {
			return err
		}
		dbInstance.gormDB = nil
		dbInstance.sqlDB = nil
	}
	return nil
}
