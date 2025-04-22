package core

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"time"

	"github.com/golang-jwt/jwt"
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

// 生成token
func GenerateToken(username string) (string, error) {
	// 创建一个声明
	claims := jwt.MapClaims{}
	claims["username"] = username
	claims["exp"] = time.Now().Add(time.Hour * time.Duration(Setting.SignExpireTime)).Unix() // 过期时间

	// 创建一个token对象
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	// 用密钥签名token
	tokenString, err := token.SignedString([]byte(Setting.SecurityKey))
	if err != nil {
		return "", err
	}

	return tokenString, nil
}

// 认证token
func ValidateToken(tokenString string) (*jwt.Token, error) {
	// 解析token
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (any, error) {
		// 只允许使用HS256签名方法
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return []byte(Setting.SecurityKey), nil
	})

	if err != nil {
		return nil, err
	}

	// 验证token是否有效
	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		// 你可以在这里访问claims中的数据
		username := claims["username"].(string)
		fmt.Println("Username:", username)

		// 你可以在这里检查token的过期时间等
		if exp, ok := claims["exp"].(float64); ok {
			expTime := time.Unix(int64(exp), 0)
			if time.Now().After(expTime) {
				return nil, fmt.Errorf("token has expired")
			}
		}

		return token, nil
	} else {
		return nil, err
	}
}
