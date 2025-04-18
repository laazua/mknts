package common

import (
	"crypto/md5"
	"encoding/hex"
	"ginweb/db"
	"time"

	"github.com/dgrijalva/jwt-go"
)

var JWT_KEY = []byte("secret_key")

type Claims struct {
	UserID uint
	jwt.StandardClaims
}

// token编码
func EnCodeToken(user db.Users) (string, error) {
	expirationTime := time.Now().Add(7 * 24 * time.Hour)
	claims := &Claims{
		UserID: user.ID,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
			IssuedAt:  time.Now().Unix(),
			Issuer:    "ginweb",
			Subject:   "ginweb token",
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	if tokenString, err := token.SignedString(JWT_KEY); err != nil {
		return "", err
	} else {
		return tokenString, nil
	}
}

// token解码
func DeCodeToken(tokenString string) (*jwt.Token, *Claims, error) {
	claims := &Claims{}

	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (i interface{}, e error) {
		return JWT_KEY, nil
	})

	return token, claims, err
}

// password hash
func HashPassword(password string) string {
	h := md5.New()
	h.Write([]byte(password))
	return hex.EncodeToString(h.Sum(nil))
}
