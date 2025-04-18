package global

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var DB *gorm.DB

// 数据库连接初始化
func init() {
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local",
		AppCon.GetString("mysql.user"), AppCon.GetString("mysql.pass"),
		AppCon.GetString("mysql.host"), AppCon.GetInt("mysql.port"), AppCon.GetString("mysql.name"))

	Db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{PrepareStmt: true})
	if err != nil {
		fmt.Println("数据库连接错误")
		panic(err)
	}
	// log.Println("Msql数据库连接成功!")
	// 数据库连接池参数设置
	sqlDB, err := Db.DB()
	if err != nil {
		panic(err)
	}
	DB = Db
	sqlDB.SetMaxOpenConns(50)
	sqlDB.SetMaxIdleConns(20)
}
