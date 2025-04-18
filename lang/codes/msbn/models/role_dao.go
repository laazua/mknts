package models

// 添加角色
func AddSysRole(rolename, desc string) bool {
	r := Role{
		Name: rolename,
		Desc: desc,
	}
	if err := db.Create(&r).Error; err != nil {
		return false
	} else {
		return true
	}
}

// 查询角色列表
func QuerySysRoleList() []Role {
	var roles []Role
	result := db.Debug().Select("id", "name", "desc").Find(&roles)
	if result.Error != nil {
		return nil
	}
	return roles
}

// 更新角色
func UpdateSysRole(name, desc string) bool {
	if name != "" {
		db.Model(&Role{}).Where("desc = ?", name).Update("name", name)
	} else {
		return false
	}
	if desc != "" {
		db.Model(&Role{}).Where("desc = ?", desc).Update("desc", desc)
	} else {
		return false
	}
	return true
}

// 删除角色
func DeleteSysRole(rolename string) bool {
	result := db.Debug().Model(&Role{}).Where("name = ?", rolename).Delete(&Role{})
	if result.Error != nil {
		return false
	} else {
		return true
	}
}

// 根据id查询角色
// func GetSysRoleById(id uint64) Role {
// 	var r Role
// 	// db.Debug().Where("id = ?", id).First(&r)
// 	// db.Debug().Model(&r).Association("Permisson").Find(&r.Permisson)
// 	return *&r
// }

// 给角色分配权限
func DistributeMenus(rolename, mainmenu string) bool {
	rp := RolePermisson{
		Rolename: rolename,
		Mainmenu: mainmenu,
	}
	if err := db.Create(&rp).Error; err != nil {
		return false
	} else {
		return true
	}
}
