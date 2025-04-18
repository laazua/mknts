package models

// 添加菜单的表单校验
type Ams struct {
	Permdesc string `json:"permdesc" binding:"required"`
	Namepath string `json:"namepath" binding:"required"`
	Subdesc  string `json:"subdesc" binding:"required"`
	Subpath  string `json:"subpath" binding:"required"`
}

// 删除菜单的表单校验
type Dms struct {
	Permdesc string `json:"permdesc" binding:"required"`
}

// 更菜菜单的表单校验
type Ums struct {
	Permdesc string `json:"permdesc" binding:"required"`
	Column   string `json:"column" binding:"required"`
	Value    string `json:"value" binding:"required"`
}

// 查询菜单的表单校验
type Gms struct {
	Dms
}
