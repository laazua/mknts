/*
接口参数校验模型
json标签对应 application/json
form标签对应 multipart/form-data
*/
package models

// 删除用户表单
type DelUserSchema struct {
	Username string `json:"username"`
}

// 添加用户表单
type AddUserSchema struct {
	DelUserSchema
	PassOne string `json:"passone"`
	PassTow string `json:"passtow"`
}

// 更新用户表单
type UpUserSchema struct {
	AddUserSchema
}

// 用户分配角色表单
type UrSchema struct {
	Username string `json:"username"`
	Rolename string `json:"rolename"`
}

// 添加角色表单
type AddRoleSchema struct {
	Rolename string `json:"rolename"`
	Desc     string `json:"desc"`
}

// 删除角色表单
type DelRoleSchema struct {
	Rolename string `json:"rolename"`
}

// 更新角色表单
type UpRoleSchema struct {
	AddRoleSchema
}

// 给角色分配权限表单
type RpSchema struct {
	Rolename string `json:"rolename"`
	MainMenu string `json:"mainmenu"`
}

// 添加权限表单
type AddPerSchema struct {
	Desc     string `json:"desc"`
	Namepath string `json:"namepath"`
	Mainmenu string `json:"mainmenu"`
	Subdesc  string `json:"subdesc"`
	Subpath  string `json:"subpath"`
}

// 登录表单校验
type UserLoginSchema struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

// 根据用户id查询用户的表单
type QUserByidSchema struct {
	Id uint `uri:"id" binding:"required"`
}

// 根据角色id查询角色的表单
type QRoleBuIdSchema struct {
	QUserByidSchema
}
