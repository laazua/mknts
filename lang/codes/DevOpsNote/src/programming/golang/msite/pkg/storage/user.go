package storage

import (
	"msite/pkg/schema"
	"msite/pkg/storage/model"
)

type User struct {
}

func (u *User) Create(user schema.User) error {
	return db.Create(user).Error
}

func (u *User) Delete(id int) error {
	return db.Delete(&model.User{}).Where("id = ?", id).Error
}

func (u *User) Update(schema.User) error {

	return nil
}

func (u *User) Query() ([]model.User, error) {

	return []model.User{}, nil
}

func (u *User) QueryId(id int) (model.User, error) {
	return model.User{}, nil
}
