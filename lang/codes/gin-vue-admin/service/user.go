package service

import (
	"gin-vue-admin/api/form"
	"gin-vue-admin/models"
	"gin-vue-admin/utils"
)

type UserService struct {
	User models.User
}

func (us UserService) UserLogin(LoginForm form.LoginForm) {
    utils.Db.Model(&us.User).Find(&LoginForm)
}
