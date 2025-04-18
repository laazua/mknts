package model

import "gorm.io/gorm"

// 数据库模型
type User struct {
	gorm.Model
	Name     string `gorm:"name"`
	Password string `gorm:"password"`
	Avatar   string `gorm:"avatar"`
}

// 接口请求模型
type UserForm struct {
	Id       string `form:"id"`
	Name     string `form:"name" binding:"required"`
	Password string `form:"password" binding:"required"`
	Avatar   string `form:"avatar"`
}

type LoginForm struct {
	Name     string `form:"name" binding:"required"`
	Password string `form:"password" binding:"required"`
}

// 接口响应模型
type LoginRespon struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
	Token   string `json:"token"`
}

type ApiRespone struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
	Data    any    `json:"data"`
}
