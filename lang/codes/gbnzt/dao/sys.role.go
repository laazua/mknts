package dao

import (
	"bnzt/models"
)

// 对外暴露的接口
type DbRole interface {
	AddRole(name, desc, menu string) bool
	DelRole(name string) bool
	UpdRole(name, column, value string) bool
	GetRole(name string) ([]models.Role, error)
	RoleList() []models.Role
}

func NewDbRole() DbRole {
	return &dbRole{}
}

// 实现DbRole的类
type dbRole struct {
	models.Role
}

// 添加角色
func (d *dbRole) AddRole(name,
	desc, menu string) bool {
	// DB.Raw(`
	//     SELECT * FROM role WHERE rolename = ?
	// `, name).Find(&d.Role)
	// if d.Role.Rolename != "" {
	// 	return DB.Unscoped().Model(&d.Role).
	// 		Where("rolename = ?", name).
	// 		Update("deleted_at", nil).Error == nil
	// }
	d.Rolename = name
	d.Roledesc = desc
	d.MainMenu = menu
	return DB.Create(&d).Error == nil
}

// 删除角色
func (d *dbRole) DelRole(name string) bool {
	return DB.Debug().
		Where("rolename = ?", name).
		Delete(&d.Role).Error == nil
}

// 更新角色
func (d *dbRole) UpdRole(name, column, value string) bool {
	return DB.Debug().Model(&d.Role).
		Where("rolename = ?", name).
		Update(column, value).Error == nil
}

// 查询角色
func (d *dbRole) GetRole(name string) ([]models.Role, error) {
	var rmsg []models.Role
	result := DB.Debug().Select("id", "rolename", "roledesc", "mainmenu").
		Where("rolename = ?", name).Find(&rmsg)
	if result.Error != nil {
		return nil, result.Error
	}
	return rmsg, nil
}

// 角色列表
func (d *dbRole) RoleList() []models.Role {
	var role []models.Role
	if DB.Debug().Select("id", "rolename", "roledesc", "mainmenu").
		Find(&role).Error != nil {
		return nil
	}
	return role
}
