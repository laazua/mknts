package core

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
)

// 生成哈希
func HashPassword(password string) string {
	// 创建 HMAC 哈希
	h := hmac.New(sha256.New, []byte(Setting.SaltKey))
	h.Write([]byte(password))
	hashedPasswd := h.Sum(nil)
	// 编码为 Base64
	return base64.StdEncoding.EncodeToString(hashedPasswd)
}

// 验证密码
func VerifyPassword(hashPasswd, password string) bool {
	// 生成哈希
	newHash := HashPassword(password)
	return hmac.Equal([]byte(hashPasswd), []byte(newHash))
}
