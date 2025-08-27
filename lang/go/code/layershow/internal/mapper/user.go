package mapper

import (
	"layershow/internal/dto"
	"layershow/internal/model"
)

func UserDTOToModel(req *dto.UserCreateRequest) *model.User {
	return &model.User{
		Name:  req.Name,
		Email: req.Email,
	}
}

func UserModelToDTO(u *model.User) *dto.UserResponse {
	return &dto.UserResponse{
		ID:    u.ID,
		Name:  u.Name,
		Email: u.Email,
	}
}
