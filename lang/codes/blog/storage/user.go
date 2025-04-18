package storage

import (
	"schema"
	"storage/models"
)

type User struct {
	storage *Storage
}

func NewUser(storage *Storage) *User {
	return &User{storage: storage}
}

func (u *User) Create(user schema.User) error {
	return u.storage.db.Create(user).Error
}

func (u *User) Delete(id int) error {
	return u.storage.db.Delete(&models.User{}).Where("id = ?", id).Error
}

func (u *User) Update(user schema.User) error {
	return u.storage.db.Save(user).Error
}

func (u *User) Select() []models.User {
	var users []models.User
	if err := u.storage.db.Find(&users).Error; err != nil {
		return nil
	}
	return users
}

func (u *User) SelectId(id int) (models.User, error) {
	var user models.User
	if err := u.storage.db.Find(user, "id = ?", id).Error; err != nil {
		return models.User{}, err
	}
	return user, nil
}
