package storage

import (
	"schema"
	"storage/models"
)

type Blog struct {
	storage *Storage
}

func NewBlog(storage *Storage) *Blog {
	return &Blog{storage: storage}
}

func (b *Blog) Create(role schema.Blog) error {

	return nil
}

func (b *Blog) Delete(id int) error {

	return nil
}

func (b *Blog) Update(role schema.Blog) error {
	return nil
}

func (b *Blog) Query() []models.Blog {

	return nil
}

func (b *Blog) QueryId(id uint) models.Blog {
	return models.Blog{}
}
