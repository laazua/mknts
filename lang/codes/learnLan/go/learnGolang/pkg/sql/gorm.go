// sql操作禁止SQL拼接语句
package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type Apple struct {
	gorm.Model // 继承gorm.Model
	Color      string
	Price      float64
}

var DB *gorm.DB

func init() {
	// 数据库连接
	dsn := "user:pass@tcp(127.0.0.1:3306)/dbname?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		return
	}
	if db != nil {
		DB = db
	}
}

func main() {
	defer DB.Close()

	// 迁移
	DB.AutoMigrate(&Apple{})

	// 增
	apple := Apple{Color: "red", Price: 5.5}
	DB.Create(&apple)

	// 读
	DB.First(&apple, 1)                  // 根据主键查找
	DB.First(&apple, "color = ?", "red") // 根据字段查找

	// 更新
	DB.Model(&apple).Update("Price", 6.5) // 更新单个字段
	DB.Model(&apple).Updates(Apple{Color: "green", Price: 3.5})
	DB.Model(&apple).Updates(map[string]interface{}{"Color": "red", "Price": 4.5})
	apple.Color = "green"
	apple.Price = 4.5
	DB.Save(&apple)

	// 删除
	DB.Delete(&apple, 1)

	// 使用结构体创建表名为apple的表
	DB.Table("apple").CreateTable(&Apple{})

	var aa []Apple
	DB.Table("apple").Find(&aa)

	DB.Table("apple").Where("id = ?", 1).Delete()
}
