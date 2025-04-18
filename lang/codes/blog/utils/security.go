package utils

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"env"
	"errors"
	"log/slog"
	"os"
	"time"

	"github.com/golang-jwt/jwt"
)

type Helper struct {
	secuKey      string
	tokenSign    string
	tokenExpored int
}

func NewHelper() *Helper {
	return &Helper{
		secuKey:      os.Getenv("app.security.key"),
		tokenSign:    os.Getenv("app.token.sign"),
		tokenExpored: env.Atoint(os.Getenv("app.token.expored")),
	}
}

func (h Helper) HashPasswd(passwd string) string {
	hm := hmac.New(sha256.New, []byte(h.secuKey))
	hm.Write([]byte(passwd))
	hashedPasswd := hm.Sum(nil)
	return base64.StdEncoding.EncodeToString(hashedPasswd)
}

func (h Helper) VeryPasswd(passwd, hashPasswd string) bool {
	newHash := h.HashPasswd(passwd)
	return hmac.Equal([]byte(hashPasswd), []byte(newHash))
}

func (h Helper) CreateToken(email string) (string, error) {
	claims := &jwt.MapClaims{
		"email": email,
		"exp":   time.Now().Add(time.Minute * time.Duration(h.tokenExpored)).Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenStr, err := token.SignedString([]byte(h.tokenSign))
	if err != nil {
		return "", errors.New("token签名失败")
	}
	return tokenStr, nil
}

func (h Helper) ParseToken(tokenStr string) (string, error) {
	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (any, error) {
		// 确保签名方法是我们所期望的
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, errors.New("未知的签名方法")
		}
		return []byte("cZZVHDkiwWg"), nil
	})
	if err != nil {
		slog.Error(err.Error())
		return "", errors.New("解析token失败")
	}
	// 读取 claims
	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		// 检查过期时间
		if exp, ok := claims["exp"].(float64); ok {
			if time.Unix(int64(exp), 0).Before(time.Now()) {
				return "", errors.New("token时间过期")
			}
		}
		// 返回用户名
		if username, ok := claims["username"].(string); ok {
			return username, nil
		}
	}
	return "", errors.New("token不可用")
}
