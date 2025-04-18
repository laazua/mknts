package dto

import "cmsmanager/model"

type UserDto struct {
	Username    string `json:"username"`
}

func ToUserDto(user model.User) UserDto {
	return UserDto{
		Username: user.Username,
	}
}