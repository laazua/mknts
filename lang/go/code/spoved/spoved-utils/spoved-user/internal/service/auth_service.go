package service

import (
	"errors"
	"time"

	"spoved-user/internal/cache"
	"spoved-user/internal/repository"
	"spoved-utils/config"

	"github.com/golang-jwt/jwt/v5"
	"golang.org/x/crypto/bcrypt"
)

type AuthService struct {
	cache          *cache.RedisCache
	authRepository *repository.AuthRepository
}

func NewAuthService() *AuthService {
	return &AuthService{
		cache:          cache.NewRedisCache(),
		authRepository: repository.NewAuthRepository(),
	}
}

// PwdLogin 用户登录
func (s *AuthService) PwdLogin(username, password string) (string, error) {
	// 查询数据库
	userRepo, err := s.authRepository.GetUserByUsername(username)
	if err != nil {
		return "", err
	}
	// 验证密码
	if err := s.compareHashPwd(userRepo.Password, password); err != nil {
		return "", errors.New("invalid username or password")
	}
	// 生成JWT令牌
	token, err := s.generateToken(userRepo.ID, userRepo.Phone, userRepo.Email)
	if err != nil {
		return "", err
	}
	return token, nil
}

func (s *AuthService) SmsLogin(phone, code string) (string, error) {
	storedCode, err := s.cache.Get(phone)
	if err != nil && storedCode != code {
		return "", errors.New("invalid verification code")
	}
	s.cache.Delete("sms:" + phone) // 删除验证码，防止重复使用
	// 查询数据库
	userRepo, err := s.authRepository.GetUserByPhone(phone)
	if err != nil {
		return "", err
	}
	// 生成JWT令牌
	token, err := s.generateToken(userRepo.ID, userRepo.Phone, userRepo.Email)
	if err != nil {
		return "", err
	}
	return token, nil
}

func (s *AuthService) SendSmsCode(phone string) error {
	// Implement logic to send an SMS code to the user's phone number
	return nil
}

func (s *AuthService) EmailLogin(email string) (string, error) {
	// Implement logic to authenticate the user via email and return a JWT token or session ID
	return "", nil
}

// 生成JWT令牌
func (s *AuthService) generateToken(userID uint, phone, email string) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"user_id": userID,
		"phone":   phone,
		"email":   email,
		"exp":     time.Now().Add(config.Get().Server.TokenExpireTime).Unix(),
	})

	return token.SignedString(config.Get().Server.JwtSecret)
}

func (s *AuthService) generateHashPwd(password string) (string, error) {
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}

	return string(hashedPassword), nil
}

func (s *AuthService) compareHashPwd(hashedPassword, password string) error {
	return bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(password))
}

// Logout 用户登出
func (s *AuthService) Logout(token string) error {
	// Implement logic to invalidate the user's session or token
	return nil
}
