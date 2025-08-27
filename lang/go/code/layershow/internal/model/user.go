package model

// User 数据库实体
type User struct {
	ID       int    `gorm:"primaryKey;column:id"`
	Name     string `gorm:"column:name"`
	Email    string `gorm:"column:email"`
	Password string `gorm:"column:password"`
}
