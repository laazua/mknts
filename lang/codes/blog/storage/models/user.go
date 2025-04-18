package models

type User struct {
	Name     string `gorm:"name"`
	Email    string `gorm:"email"`
	Password string `gorm:"password"`
	Avator   string `gorm:"avator"`
}
