package models

import (
	"gorm.io/gorm"
)

// 用户表
type User struct {
	gorm.Model
	Username string `gorm:"column:username; unique; size:256"`
	Hspass   string `gorm:"column:hspass; is null; size:512"`
	Role     string `gorm:"column:rolename; not null; size:256"`
}

// 角色表
type Role struct {
	gorm.Model
	Rolename string `gorm:"column:rolename; not null; size:256"`
	Roledesc string `gorm:"column:roledesc; not null; size:256"`
	MainMenu string `gorm:"column:mainmenu; not null; size:256"`
}

// 权限表
type Permission struct {
	gorm.Model
	Permdesc string `gorm:"column:permdesc; not null; size:256"`
	Namepath string `gorm:"column:namepath; not null; size:256"`
	SubDesc  string `gorm:"column:subdesc; not null; size:64"`
	Subpath  string `gorm:"column:subpath; not null; size:64"`
}

// 用户信息结果
type UserMsg struct {
	UserName string `gorm:"column:username"`
	RoleRole string `gorm:"column:rolename"`
	RoleDesc string `gorm:"column:roledesc"`
	PermDesc string `gorm:"column:permdesc"`
	NamePath string `gorm:"column:namepath"`
	SubDesc  string `gorm:"column:subdesc"`
	SubPath  string `gorm:"column:subpath"`
}

// 区服信息表
type Zone struct {
	gorm.Model
	Ip       string `gorm:"column:ip; not null; size:256"`
	ChanName string `gorm:"column:channame; not null; size:128"`
	Zone     string `gorm:"column:zone; not null; size:256"`
}

// 初始化表结构
// func init() {
// 	db := global.DB
// 	db.AutoMigrate(&User{})
// 	db.AutoMigrate(&Role{})
// 	db.AutoMigrate(&Permission{})
// 	db.AutoMigrate(&Zone{})
// }

// 定义表名
func (u User) TableName() string {
	return "user"
}

func (r Role) TableName() string {
	return "role"
}

func (p Permission) TableName() string {
	return "permission"
}

func (z Zone) TableName() string {
	return "zone"
}
