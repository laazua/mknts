package repository

import (
	"errors"

	"spoved-user/internal/model"
	"spoved-utils/db"
	"spoved-utils/xlog"

	"gorm.io/gorm"
)

type AuthRepository struct {
	db *gorm.DB // 直接存储 *gorm.DB，而不是 *db.MySQL
}

func NewAuthRepository() (*AuthRepository, error) {
	// 在初始化时获取数据库连接
	gormDB, err := db.GetDB() // 假设你有这个函数
	if err != nil {
		xlog.Errorf("初始化AuthRepository失败，获取数据库连接错误: %v", err)
		return nil, err
	}

	return &AuthRepository{
		db: gormDB,
	}, nil
}

// 根据手机号查询用户
func (r *AuthRepository) GetUserByPhone(phone string) (*model.User, error) {
	var user model.User

	err := r.db.Where("phone = ?", phone).First(&user).Error
	if err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return nil, nil
		}
		xlog.Errorf("根据手机号查询用户失败: %v", err)
		return nil, err
	}

	return &user, nil
}

// 根据用户名查询用户
func (r *AuthRepository) GetUserByUsername(username string) (*model.User, error) {
	var user model.User

	err := r.db.Where("name = ?", username).First(&user).Error
	if err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return nil, nil
		}
		xlog.Errorf("根据用户名查询用户失败: %v", err)
		return nil, err
	}

	return &user, nil
}
