package utils

import (
	"fmt"
	"gin-vue-admin/models"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var Db *gorm.DB

// 由于数据库连接信息依赖于配置
// 所以应该先初始化配置,再初始化数据库;
// 因为config.go文件的首字母在db.go文件首字母
// 之前,所以先执行的config.go中的init(),在执行
// 的db.go中的init();若非如此,应该显示指明执行顺序
func init() {
	print("init db")
	username := GetEnv("DB_USER")
	password := GetEnv("DB_PASS")
	host := GetEnv("DB_HOST")
	port := GetEnv("DB_PORT")
	dbName := GetEnv("DB_NAME")
	dsn := fmt.Sprintf("%v:%v@tcp(%v:%v)/%v?charset=utf8mb4&parseTime=True&loc=Local", username, password, host, port, dbName)
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic(err)
	}

	// 自动迁移
	db.AutoMigrate(&models.User{}, &models.Role{}, &models.UserRole{}, &models.Menu{})

	Db = db
}
