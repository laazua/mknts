package dao

import (
	"bnzt/global"
	"bnzt/models"
	"bnzt/utils"
)

var DB = global.DB

type DbUser interface {
	GetUser(name string) ([]models.UserMsg, error)
	AddUser(name, pass string) bool
	DelUser(name string) bool
	UpdUser(name, column, value string) bool
	ChkUser(name, pass string) bool
	UserList() []models.User
}

func NewDbUser() DbUser {
	return &dbUser{}
}

type dbUser struct {
	models.User
	models.Role
}

// 添加用户
func (d *dbUser) AddUser(name,
	pass string) bool {
	p := utils.NewPassword()
	DB.Raw(`
	    SELECT * FROM user WHERE username = ?
	`, name).Find(&d.User)
	if d.User.Username != "" {
		return DB.Unscoped().Model(&d.User).
			Where("username = ?", name).
			Update("deleted_at", nil).Error == nil
	}
	return DB.Create(&models.User{
		Username: name,
		Hspass:   p.HashAndSalt([]byte(pass)),
	}).Error == nil
}

// 验证用户
func (d *dbUser) ChkUser(name, pass string) bool {
	DB.Debug().Select("hspass").
		Where("username = ?", name).First(&d.User)
	p := utils.NewPassword()

	return p.ComparePassword(d.User.Hspass, pass)
}

// 删除用户
func (d *dbUser) DelUser(name string) bool {
	return DB.Debug().
		Where("username = ?", name).
		Delete(&d.User).Error == nil
}

// 更新用户
func (d *dbUser) UpdUser(name, column, value string) bool {
	if column == "hspass" {
		p := utils.NewPassword()
		if ret := p.HashAndSalt([]byte(value)); ret == "" {
			return false
		} else {
			return DB.Debug().Model(&d.User).
				Where("username = ?", name).
				Update(column, ret).Error == nil
		}
	}
	if column == "deleted_at" {
		// 操作 deleted_at不为Null的字段
		return DB.Debug().Unscoped().Model(&d.User).
			Where("username = ?", name).
			Update(column, nil).Error == nil
	}
	return DB.Debug().Model(&d.User).
		Where("username = ?", name).
		Update(column, value).Error == nil
}

// 获取用户列表
func (d *dbUser) UserList() []models.User {
	var user []models.User
	if DB.Debug().
		Select("id", "username", "rolename").
		Find(&user).Error != nil {
		return nil
	}
	return user
}

// 根据名字获取单个用户信息
func (d *dbUser) GetUser(name string) ([]models.UserMsg, error) {
	var umsg []models.UserMsg
	result := DB.Raw(`
	    SELECT u.username, u.rolename, r.roledesc, 
		  p.namepath, p.permdesc, p.subdesc, p.subpath 
		FROM user u LEFT JOIN role r
	    ON u.rolename = r.rolename
	    LEFT JOIN permission p
	    ON r.mainmenu = p.permdesc
		WHERE username = ?`, name).
		Find(&umsg)
	if result.Error != nil {
		return nil, result.Error
	}
	return umsg, nil
}
