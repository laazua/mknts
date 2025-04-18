package models

// 订单查询表单
type OrderSchema struct {
	Zone  string `json:"zone"`
	Uid   string `json:"uid"`
	Order string `json:"order"`
}

// 角色查询表单
type RoleSchema struct {
	Zone string `json:"zone"`
	Uid  string `json:"uid"`
}
