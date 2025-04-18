package models

import (
	"msbn/global"
)

var db = global.DB

func init() {
	// migraTable(global.DB, User{}, Role{},
	// 	Permisson{})
	db.AutoMigrate(&User{})
	db.AutoMigrate(&UserRole{})
	db.AutoMigrate(&Role{})
	db.AutoMigrate(&RolePermisson{})
	db.AutoMigrate(&Permisson{})
}

// func migraTable(db *gorm.DB, tables ...interface{}) {
// 	for _, table := range tables {
// 		db.AutoMigrate(&table)
// 	}
// }
