package storage

import (
	"schema"
	"storage/models"
	"utils"
)

type Auth struct {
	helper  *utils.Helper
	storage *Storage
}

func NewAuth(storage *Storage) *Auth {
	return &Auth{helper: utils.NewHelper(), storage: storage}
}

func (a *Auth) Auth(auth schema.Auth) bool {
	if auth.Email == "" || auth.Password == "" {
		return false
	}
	var user models.User
	if err := a.storage.db.Find(&user).Where("email = ?", auth.Email).Error; err != nil {
		return false
	}
	return a.helper.VeryPasswd(auth.Password, user.Password)
}
