package models

import (
	"msbn/utils"
)

// 添加用户
func AddSysUser(username, password string) bool {
	u := User{
		Name:   username,
		Hspass: utils.HashAndSalt([]byte(password)),
	}
	if err := db.Create(&u).Error; err != nil {
		return false
	} else {
		return true
	}
}

// 查询用户列表
func QuerySysUserList() []User {
	var users []User
	result := db.Debug().Select("id", "name", "rolename").Find(&users)
	if result.Error != nil {
		return nil
	}
	return users
}

// 更新用户
func UpdateSysUser(username, password string) bool {
	hspass := utils.HashAndSalt([]byte(password))
	if hspass == "" {
		return false
	}
	db.Model(&User{}).Where("name = ?", username).Update("hspass", hspass)
	return true
}

// 删除用户
func DeleteSysUser(username string) bool {
	result := db.Debug().Model(&User{}).Where("name = ?", username).Delete(&User{})
	if result.Error != nil {
		return false
	} else {
		return true
	}
}

// 根据id查询用户
func GetSysUserById(id uint64) User {
	var u User
	db.Debug().
		Select("id", "name").
		Where("id = ?", id).First(&u)

	return u
}

// 根据名字查询用户
func GetUserByName(username string) ([]RolePermisson, []Permisson) {
	var u User
	db.Debug().Select("rolename").Where("name = ?", username).First(&u)
	var rp []RolePermisson
	db.Debug().Select("mainmenu").Where("rolename = ?", u.Rolename).Find(&rp)
	var p []Permisson
	db.Debug().Select("id", "desc", "namepath", "mainmenu", "subdesc", "subpath").
		Find(&p)
	return rp, p
}

// 根据username查询用户
func CheckUser(username, password string) bool {
	var user User
	db.Debug().Select("name", "hspass").
		Where("name = ?", username).First(&user)
	return utils.ComparePassword(user.Hspass, password)
}

// 给用户分配角色
func UserAndRole(username, rolename string) bool {
	result := db.Debug().Model(&User{}).
		Where("name = ?", username).Update("rolename", rolename)
	if result.Error != nil {
		return false
	} else {
		return true
	}
}
