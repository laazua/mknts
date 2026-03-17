package service

import "spoved-user/internal/repository"

type UserService struct {
	repository *repository.UserRepository
}

func NewUserService() (*UserService, error) {
	repo, err := repository.NewUserRepository()
	if err != nil {
		return nil, err
	}
	return &UserService{
		repository: repo,
	}, nil
}

// GetUserInfo 获取用户信息
func (s *UserService) GetUserInfo(userID int64) (any, error) {
	// Implement logic to fetch and return user information
	return nil, nil
}
