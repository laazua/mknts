package db

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// 表关联,一个结构体对应一张表
type Student struct {
}

type Teacher struct {
}

type Class struct {
}

type IDCard struct {
}

func init() {
	db, _ := gorm.Open(mysql.Open("username:password@tcp(host:port)/dbname?charset=utf8mb4&parseTime=True&loc=Local"))

	db.AutoMigrate(&Student{}, &Teacher{}, &Class{}, &IDCard{})
}

// create table
// db.Create(&Users{
//     Username: "wangwu",
//     Password: "123456",
//     Role: "yunwei",
// })
//
// select
// var user Users
// db.First(&Users, "username = ?", "wangwu")
// db.Where("username = ?", "wangwu").First(&user)
// var user []Users
// db.Find(&user, "username = ?", "zhangsan")  Find接收切片类型的user
// db.Where("username = ?", "zhangsan").Find(&user)
//
// update
// db.Where().First(&Users{}).Update()
// db.Where().First(&Users{}).Updates(map[string]interface{}{})
//
// Delete
// db.Where().Delete(&Users{}) 软删除
// db.Where().Unscoped().Delete(&Users{})  硬删除

// 实现了接口中的TableName方法
// func (u Users)TableName() string {
//     return "user"    创建指定表名
// }
