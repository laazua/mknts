package storage

import (
	"schema"
	"storage/models"
)

type Role struct {
	storage *Storage
}

func NewRole(storage *Storage) *Role {

	return &Role{storage: storage}
}

func (r *Role) Create(role schema.Role) error {
	return r.storage.db.Create(role).Error
}

func (r *Role) Delete(id int) error {
	return r.storage.db.Delete(models.Role{}).Where("id = ?", id).Error
}

func (r *Role) Update(role schema.Role) error {
	return nil
}

func (r *Role) Query() []models.Role {

	return nil
}

func (r *Role) QueryId(id int) (models.Role, error) {

	return models.Role{}, nil
}
