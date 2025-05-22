package dao

import "show/internal/model"

type UserDAO struct {
	data map[int]*model.User
}

func NewUserDAO() *UserDAO {
	return &UserDAO{data: make(map[int]*model.User)}
}

func (dao *UserDAO) Create(u *model.User) {
	dao.data[u.ID] = u
}

func (dao *UserDAO) Get(id int) *model.User {
	return dao.data[id]
}

func (dao *UserDAO) Update(u *model.User) {
	dao.data[u.ID] = u
}

func (dao *UserDAO) Delete(id int) {
	delete(dao.data, id)
}
