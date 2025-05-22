package service

import (
	"show/internal/dao"
	"show/internal/model"
)

type UserService struct {
	dao *dao.UserDAO
}

func NewUserService(dao *dao.UserDAO) *UserService {
	return &UserService{dao: dao}
}

func (s *UserService) CreateUser(u *model.User) {
	s.dao.Create(u)
}

func (s *UserService) GetUser(id int) *model.User {
	return s.dao.Get(id)
}

func (s *UserService) UpdateUser(u *model.User) {
	s.dao.Update(u)
}

func (s *UserService) DeleteUser(id int) {
	s.dao.Delete(id)
}
