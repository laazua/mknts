package dao

import (
	"layershow/internal/model"

	"gorm.io/gorm"
)

type UserDao interface {
	Create(user *model.User) error
	FindById(id int) (*model.User, error)
}

func NewUserDao(db *gorm.DB) UserDao {
	return &UserDaoImpl{db: db}
}
