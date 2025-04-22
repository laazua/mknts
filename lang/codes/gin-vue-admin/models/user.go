package models

import "time"

type User struct {
	UserID   int    `gorm:"primaryKey;autoIncrement;column:user_id"`
	UserName string `gorm:"size:100;not null;column:user_name"`
	Email    string `gorm:"size:255;unique;column:email"`
	Password string `gorm:"size:255;not null;column:password"`
	Avatar   string `gorm:"size:255;default:'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif';column:avatar"`
	Token    string `gorm:"size:255;unique;column:token"`
	Roles    []Role `gorm:"many2many:user_role;foreignKey:UserID;joinForeignKey:UserID;References:RoleID;JoinReferences:RoleID"`
}

type Role struct {
	RoleID   int    `gorm:"primaryKey;autoIncrement;column:role_id"`
	RoleName string `gorm:"size:100;not null;column:role_name"`
	Users    []User `gorm:"many2many:user_role;foreignKey:RoleID;joinForeignKey:RoleID;References:UserID;JoinReferences:UserID"`
}

type UserRole struct {
	RoleID int `gorm:"column:role_id"`
	UserID int `gorm:"column:user_id"`
}

type Menu struct {
	MenuID    int       `gorm:"primaryKey;autoIncrement;column:menu_id"`
	Name      string    `gorm:"size:100;column:name"`
	Redirect  string    `gorm:"size:100;column:redirect"`
	Path      string    `gorm:"size:255;column:path"`
	Component string    `gorm:"size:255;column:component"`
	Meta      string    `gorm:"type:json;column:meta"`
	ParentID  int       `gorm:"default:0;column:parent_id"`
	CreatedAt time.Time `gorm:"autoCreateTime"`
	UpdatedAt time.Time `gorm:"autoUpdateTime"`
}
