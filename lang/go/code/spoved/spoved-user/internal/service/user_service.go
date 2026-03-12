package service

import "spoved-user/internal/repository"

type UserService struct {
	repository *repository.UserRepository
}

func NewUserService() *UserService {
	return &UserService{
		repository: repository.NewUserRepository(),
	}
}

// GetUserInfo 获取用户信息
func (s *UserService) GetUserInfo(userID int64) (any, error) {
	// Implement logic to fetch and return user information
	return nil, nil
}
