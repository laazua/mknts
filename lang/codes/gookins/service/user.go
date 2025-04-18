package service

import (
	"errors"
	"log/slog"

	"gookins/core"
	"gookins/model"
)

var (
	ErrUserForm     = errors.New("用户或密码为空")
	ErrUserNotFound = errors.New("用户不存在")
	ErrUserPassword = errors.New("用户密码错误")
	ErrCreateUser   = errors.New("创建用户失败")
	ErrDeleteUser   = errors.New("删除用户失败")
	ErrUpdateUser   = errors.New("更新用户失败")
	ErrUserLists    = errors.New("获取用户列表失败")
)

func UserSign(user model.LoginForm) error {
	if user.Name == "" || user.Password == "" {
		return ErrUserForm
	}
	var dbUser model.User
	result := core.Db.Where("name = ?", user.Name).Find(&dbUser)
	if result.Error != nil {
		return ErrUserNotFound
	}
	if !core.VerifyPassword(dbUser.Password, user.Password) {
		return ErrUserPassword
	}
	return nil
}

func CreateUser(user model.UserForm) error {
	dbUser := &model.User{
		Name:     user.Name,
		Password: core.HashPassword(user.Password),
		Avatar:   user.Avatar,
	}
	result := core.Db.Create(dbUser)
	if result.Error != nil {
		return ErrCreateUser
	}
	return nil
}

func DeleteUser(id uint64) error {
	var user model.User
	result := core.Db.Where("id = ?", id).Delete(&user)
	if result.Error != nil {
		slog.Error(result.Error.Error())
		return ErrDeleteUser
	}
	return nil
}

func UpdateUser(user model.UserForm) error {
	result := core.Db.Model(&model.User{}).Where("id = ?", user.Id).Updates(model.User{Name: user.Name, Password: core.HashPassword(user.Password), Avatar: user.Avatar})
	if result.Error != nil {
		return ErrUpdateUser
	}
	return nil
}

func UserLists() ([]model.User, error) {
	var users []model.User
	result := core.Db.Unscoped().Model(&model.User{}).Select("id, created_at, updated_at, deleted_at, name").Find(&users)
	if result.Error != nil {
		return nil, ErrUserLists
	}
	return users, nil
}
