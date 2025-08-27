package dao

import (
	"layershow/internal/model"

	"gorm.io/gorm"
)

type UserDaoImpl struct {
	db *gorm.DB
}

func (dao *UserDaoImpl) Create(user *model.User) error {
	return dao.db.Create(user).Error
}

func (dao *UserDaoImpl) FindById(id int) (*model.User, error) {
	var user model.User
	if err := dao.db.First(&user, id).Error; err != nil {
		return nil, err
	}
	return &user, nil
}
