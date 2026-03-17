package repository

import (
	"spoved-user/internal/model"

	"spoved-utils/db"
)

type AuthRepository struct {
	dB *db.MySQL
}

func NewAuthRepository() *AuthRepository {
	return &AuthRepository{
		dB: db.NewMySQL(),
	}
}

// 根据手机号查询用户
func (r *AuthRepository) GetUserByPhone(phone string) (*model.User, error) {
	var user *model.User
	err := r.dB.Operate().Where("phone = ?", phone).First(&user).Error
	if err != nil {
		return nil, err
	}
	return user, nil
}

// 根据用户名查询用户
func (r *AuthRepository) GetUserByUsername(username string) (*model.User, error) {
	var user *model.User
	err := r.dB.Operate().Where("name = ?", username).First(&user).Error
	if err != nil {
		return nil, err
	}
	return user, nil
}
