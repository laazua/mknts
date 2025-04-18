package utils

import (
	"golang.org/x/crypto/bcrypt"
)

type Password interface {
	HashAndSalt(pwd []byte) string
	ComparePassword(hashedPwd, plainPwd string) bool
}

func NewPassword() Password {
	return &passwd{}
}

type passwd struct{}

// 哈希密码
func (*passwd) HashAndSalt(pwd []byte) string {
	if hash, err := bcrypt.GenerateFromPassword(pwd,
		bcrypt.MinCost); err != nil {
		return ""
	} else {
		return string(hash)
	}
}

// 验证密码
func (*passwd) ComparePassword(hashedPwd, plainPwd string) bool {
	if err := bcrypt.CompareHashAndPassword([]byte(hashedPwd),
		[]byte(plainPwd)); err != nil {
		return false
	}
	return true
}
