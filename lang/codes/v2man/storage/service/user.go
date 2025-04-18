package service

import (
	"errors"
	"v2man/pkg/utils"
	"v2man/storage"
	"v2man/storage/model"

	"github.com/google/uuid"
)

type UserService struct {
	Helper    *utils.Helpers
	DbHandler *storage.DbHandler
}

func NewUserService(dbHandler *storage.DbHandler, helper *utils.Helpers) *UserService {
	return &UserService{DbHandler: dbHandler, Helper: helper}
}

// 登陆认证
func (u *UserService) Auth(user model.LoginRequest) error {
	if user.Username == "" || user.Password == "" {
		return errors.New("username or password invaild")
	}
	var dbUser model.User
	if err := u.DbHandler.DB.Find(&dbUser).Where("name = ?", user.Username).Error; err != nil {
		return errors.New("user not exist")
	}
	if u.Helper.VeryPasswd(user.Password, dbUser.Password) {
		return errors.New("password is error")
	}
	return nil
}

// 添加用户
func (u *UserService) Add(user model.User) error {
	user.Uuid = uuid.New()
	user.Password = u.Helper.HashPasswd(user.Password)
	return u.DbHandler.DB.Create(&user).Error
}

// 删除用户
func (u *UserService) Delete(name string) error {
	return u.DbHandler.DB.Delete(&model.User{}, name).Error
}

// 更新用户
func (u *UserService) Update(user model.User) error {
	return u.DbHandler.DB.Save(user).Error
}

// 查询用户列表
func (u *UserService) Query() ([]model.User, error) {
	var users []model.User
	if err := u.DbHandler.DB.Find(&users).Error; err != nil {
		return nil, err
	}
	return users, nil
}
