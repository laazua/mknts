package dao

import "bnzt/models"

// 暴露的接口
type DbPerm interface {
	AddPerm(permdesc, namepath, subdesc, subpath string) bool
	DelPerm(permdesc string) bool
	UpdPerm(permdesc, column, value string) bool
	GetPerm(permdesc string) ([]models.Permission, error)
	PermList() []models.Permission
}

func NewDbPerm() DbPerm {
	return &dbPerm{}
}

type dbPerm struct {
	models.Permission
}

// 添加菜单
func (d *dbPerm) AddPerm(permdesc,
	namepath, subdesc,
	subpath string) bool {
	return DB.Create(&models.Permission{
		Permdesc: permdesc,
		Namepath: namepath,
		SubDesc:  subdesc,
		Subpath:  subpath,
	}).Error == nil
}

// 删除菜单
func (d *dbPerm) DelPerm(permdesc string) bool {
	return DB.Debug().
		Where("permdesc = ?", permdesc).
		Delete(d.Permission).Error == nil
}

// 更改菜单
func (d *dbPerm) UpdPerm(permdesc, column, value string) bool {
	return DB.Debug().Model(&d.Permission).
		Where("rolename = ?", permdesc).
		Update(column, value).Error == nil
}

// 查询菜单
func (d *dbPerm) GetPerm(permdesc string) ([]models.Permission, error) {
	var pmsg []models.Permission
	result := DB.Debug().Select(
		"id", "permdesc", "namepath", "subdesc", "subpath").
		Where("rolename = ?", permdesc).Find(&pmsg)
	if result.Error != nil {
		return nil, result.Error
	}
	return pmsg, nil
}

// 菜单列表
func (d *dbPerm) PermList() []models.Permission {
	var perm []models.Permission
	if DB.Debug().Select(
		"id", "permdesc", "namepath",
		"subdesc", "subpath").
		Find(&perm).Error != nil {
		return nil
	}
	return perm
}
