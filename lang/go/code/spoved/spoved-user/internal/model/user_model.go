package model

import (
	"time"

	"gorm.io/gorm"
)

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
