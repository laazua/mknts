// 一个用户对应一个角色
// 一个角色对应多个权限
package models

import "gorm.io/gorm"

// 用户表
type User struct {
	gorm.Model
	Name     string `gorm:"column:name; unique; size:256"`
	Hspass   string `gorm:"column:hspass; is null; size:512"`
	Rolename string `gorm:"column:rolename; size:512"`
}

// 用户角色关联表
type UserRole struct {
	gorm.Model
	UserId uint `gorm:"column:userid; not null; size:64"`
	RoleId uint `gorm:"column:roleid; not null; size:64"`
}

// 角色表
type Role struct {
	gorm.Model
	Name string `gorm:"column:name; not null; size:256"`
	Desc string `gorm:"column:desc; not null; size:256"`
	// Permisson []Permisson `gorm:"FOREIGNKEY:RoleId; ASSOCIATION_FOREIGNKEY:ID"`
}

// 角色权限关联表
type RolePermisson struct {
	gorm.Model
	Rolename string `gorm:"column:rolename; not null; size:64"`
	Mainmenu string `gorm:"column:mainmenu; not null; size:64"`
}

// 权限表
type Permisson struct {
	gorm.Model
	Desc     string `gorm:"column:desc; not null; size:256"`
	NamePath string `gorm:"column:namepath; not null; size:256"`
	MainMenu string `gorm:"column:mainmenu; not null; size:256"`
	SubDesc  string `gorm:"column:subdesc; not null; size:64"`
	SubPath  string `gorm:"column:subpath; not null; size:64"`
	// CNode    []CNode `gorm:"FOREIGNKEY:PermissId; ASSOCIATION_FOREIGNKEY:ID"`
}

// 定义表名
func (u User) TableName() string {
	return "user"
}

func (u UserRole) TableName() string {
	return "userole"
}

func (r Role) TableName() string {
	return "role"
}

func (r RolePermisson) TableName() string {
	return "rolepermisson"
}

func (p Permisson) TableName() string {
	return "permisson"
}
