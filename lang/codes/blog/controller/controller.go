package controller

import (
	"storage"
	"utils"

	"github.com/gin-gonic/gin"
	"github.com/sirupsen/logrus"
)

type Controller interface {
	ApiName() string
	ApiInit(*gin.RouterGroup)
}

type Auth struct {
	Logger      *logrus.Logger
	StorageAuth *storage.Auth
	Heper       *utils.Helper
}

type User struct {
	Logger      *logrus.Logger
	StorageUser *storage.User
}

type Role struct {
	Logger      *logrus.Logger
	StorageRole *storage.Role
}

type Blog struct {
	Logger      *logrus.Logger
	StorageBlog *storage.Blog
}
