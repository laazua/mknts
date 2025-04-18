package storage

import (
	"os"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Storage struct {
	db *gorm.DB
}

func New() (*Storage, error) {

	db, err := gorm.Open(postgres.Open(os.Getenv("storage.db.uri")), &gorm.Config{})
	if err != nil {
		return nil, err
	}
	return &Storage{db: db}, nil
}
