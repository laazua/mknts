package model

import (
	"time"

	"gorm.io/gorm"
)

func init() {
	fmt.Print("xxxxxxxxxxx")
	// 迁移表
	tables := []any{&User{}}
	for _, table := range tables {
		// log.Printf("MIGRATING table: %T", table)
		if !db.SqlOpt().Migrator().HasTable(table) {
			if err := db.SqlOpt().Migrator().CreateTable(table); err != nil {
				xlog.Errorf("迁移表出错: %v", err)
			}
		}
	}
	if err := db.SqlOpt().AutoMigrate(&User{}); err != nil {
		xlog.Errorf("迁移表失败: %v", err)
	}
}

type User struct {
	ID        uint           `gorm:"primarykey" json:"id"`
	Phone     string         `gorm:"uniqueIndex;size:11" json:"phone"`
	Email     string         `gorm:"uniqueIndex;size:100" json:"email"`
	Password  string         `json:"-"` // 密码不输出到JSON
	Name      string         `gorm:"size:50" json:"name"`
	CreatedAt time.Time      `json:"created_at"`
	UpdatedAt time.Time      `json:"updated_at"`
	DeletedAt gorm.DeletedAt `gorm:"index" json:"-"`
}

func (User) TableName() string {

	return "sys_user"
}
