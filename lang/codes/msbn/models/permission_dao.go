package models

// 添加权限
func AddSysPermisson(desc, namepath, mainmenu, subdesc, subpath string) bool {
	p := &Permisson{
		Desc:     desc,
		NamePath: namepath,
		MainMenu: mainmenu,
		SubDesc:  subdesc,
		SubPath:  subpath,
	}
	if result := db.Create(&p); result.Error != nil {
		return false
	} else {
		return true
	}
}

// 查询菜单列表
func QuerySysPermisson() []Permisson {
	var permisson []Permisson
	result := db.Debug().
		Select("id", "desc", "namepath", "mainmenu", "subdesc", "subpath").
		Find(&permisson)
	if result.Error != nil {
		return nil
	}
	return permisson
}

// 更新菜单
func UpdateSysPermisson(id int) {

}

// 删除菜单
func DeleteSysPermisson(id int) {

}

// 根据id查询菜单
func GetSysPermissonById(id int) {

}
