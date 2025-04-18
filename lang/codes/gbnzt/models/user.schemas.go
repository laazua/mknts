package models

// 删除用户的表单校验
type Dus struct {
	Name string `json:"name" binding:"required"`
}

// 更新用户的表单校验
type Uus struct {
	Name   string `json:"name" binding:"required"`
	Column string `json:"column" binding:"required"`
	Value  string `json:"value" binding:"required"`
}

// 添加用户的表单校验
type Aus struct {
	Name    string `json:"name" binding:"required"`
	PassOne string `json:"passone" binding:"required"`
	PassTow string `json:"passtow" binding:"required"`
}

// 用户登录的表单校验
type Uls struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}
