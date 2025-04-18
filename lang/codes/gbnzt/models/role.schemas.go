package models

// 获取角色校验表单
type Grs struct {
	Name string `json:"name" binding:"required"`
}

// 添加角色校验表单
type Ars struct {
	Name string `json:"name" binding:"required"`
	Desc string `json:"desc" binding:"required"`
	Menu string `json:"menu" binding:"required"`
}

// 删除角色校验表单
type Drs struct {
	Name string `json:"name" binding:"required"`
}

// 更改角色表单校验
type Urs struct {
	Name   string `json:"name" binding:"required"`
	Column string `json:"column" binding:"required"`
	Value  string `json:"value" binding:"required"`
}
