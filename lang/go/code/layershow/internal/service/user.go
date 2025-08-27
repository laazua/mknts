package service

import (
	"layershow/internal/dao"
	"layershow/internal/dto"
	"layershow/internal/mapper"
)

// UserService 依赖接口
type UserService struct {
	userDao dao.UserDao
}

func NewUserService(userDao dao.UserDao) *UserService {
	return &UserService{userDao: userDao}
}

func (s *UserService) CreateUser(req *dto.UserCreateRequest) (*dto.UserResponse, error) {
	user := mapper.UserDTOToModel(req)
	if err := s.userDao.Create(user); err != nil {
		return nil, err
	}
	return mapper.UserModelToDTO(user), nil
}

func (s *UserService) GetUser(id int) (*dto.UserResponse, error) {
	user, err := s.userDao.FindById(id)
	if err != nil {
		return nil, err
	}
	return mapper.UserModelToDTO(user), nil
}
