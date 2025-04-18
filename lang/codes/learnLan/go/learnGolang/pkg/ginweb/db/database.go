// db operation
package db

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type Users struct {
	gorm.Model
	Username string `gorm:"type:varchar(128);NOT NULL"`
	Password string `gorm:"size:256;NOT NULL"`
	Role     string `gorm:"type:varchar(128);NOT NULL"`
}

func getDB() *gorm.DB {
	db, err := gorm.Open(mysql.Open("test:123456@tcp(192.168.7.21:3306)/ginweb?charset=utf8mb4&parseTime=True&loc=Local"), &gorm.Config{
		CreateBatchSize: 1000,
		PrepareStmt:     true, // 执行任何 SQL 时都创建并缓存预编译语句，可以提高后续的调用速度
	})

	if err != nil {
		panic("Failed to connect to database!")
	}

	// 自动迁移.
	// 是否有users表,没有就按照Users结构体中的字段创建表.
	db.AutoMigrate(&Users{})

	return db
}

var DB = getDB()

// 查询用户
func QueryUser(name, password string) bool {
	var user Users
	result := DB.Where("username = ? AND password = ?", name, password).First(&user)
	if result.Error != nil {
		return false
	} else {
		return true
	}
}

// 添加用户
func AddUser(name, password, Role string) bool {
	user := Users{Username: name, Password: password, Role: Role}
	result := DB.Create(&user)
	if result.Error != nil {
		return false
	}
	return true
}

// 删除用户
func DelUser(name, password string) bool {
	var user Users
	result := DB.Where("username = ? AND password = ?", name, password).Unscoped().Delete(&user)
	if result.Error != nil {
		return false
	} else {
		return true
	}
}

// 更改密码
func ChangePwd(username, password, newPassword string) bool {
	var user Users
	result := DB.Model(&user).Where("username = ? AND password = ?", username, password).Update("password", newPassword)
	if result.Error != nil {
		return false
	} else {
		return true
	}
}
