package utils

import (
	"time"

	"github.com/golang-jwt/jwt"
)

type Token struct {
	Key []byte
}

type MClaims struct {
	jwt.StandardClaims
	Username string `json:"username"`
}

func NewToken() *Token {
	return &Token{
		Key: []byte(Setting.App.KeyWord),
	}
}

func (t *Token) Create(username string) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodHS256, MClaims{
		jwt.StandardClaims{
			NotBefore: int64(time.Now().Unix()),
			ExpiresAt: int64(time.Now().Unix() + 86400),
		},
		username,
	}).SignedString(t.Key)
}

func (t *Token) Parse(token string) (*MClaims, error) {
	tk, err := jwt.ParseWithClaims(token, &MClaims{}, func(token *jwt.Token) (interface{}, error) {
		return []byte(t.Key), nil
	})
	if claims, ok := tk.Claims.(*MClaims); ok && tk.Valid {
		return claims, nil
	} else {
		return nil, err
	}
}
