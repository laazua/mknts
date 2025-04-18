package utils

import (
	"bnzt/global"
	"time"

	"github.com/golang-jwt/jwt"
)

type TokeN interface {
	Create(username string) (string, error)
	Parse(tokenstr string) (*mClaims, error)
	Update(tkstr string) (string, error)
}

type token struct {
	Key []byte
}

type mClaims struct {
	jwt.StandardClaims
	Username string `json:"username"`
}

func NewToken() TokeN {
	return &token{
		Key: []byte(global.AppCon.GetString("app.securekey")),
	}
}

func (t *token) Create(username string) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodHS256, mClaims{
		jwt.StandardClaims{
			NotBefore: int64(time.Now().Unix()),
			ExpiresAt: int64(time.Now().Unix() + 86400),
		},
		username,
	}).SignedString(t.Key)
}

func (t *token) Parse(tokestr string) (*mClaims, error) {
	token, err := jwt.ParseWithClaims(tokestr, &mClaims{}, func(token *jwt.Token) (interface{}, error) {
		return []byte(t.Key), nil
	})
	if claims, ok := token.Claims.(*mClaims); ok && token.Valid {
		return claims, nil
	} else {
		return nil, err
	}
}

func (t *token) Update(tkstr string) (string, error) {
	jwt.TimeFunc = func() time.Time {
		return time.Unix(0, 0)
	}
	tk, err := jwt.ParseWithClaims(tkstr, &mClaims{}, func(*jwt.Token) (interface{}, error) {
		return []byte(t.Key), nil
	})
	if claims, ok := tk.Claims.(*mClaims); ok && tk.Valid {
		jwt.TimeFunc = time.Now
		claims.StandardClaims.ExpiresAt = int64(time.Now().Add(1 * time.Hour).Unix())
		return t.Create(claims.Username)
	}
	return "", err
}
