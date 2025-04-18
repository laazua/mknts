package common

import (
	"cmsmanager/model"
	"github.com/dgrijalva/jwt-go"
	"time"
)

var jwtkey = []byte("secret_key")

type Claims struct {
	UserID    uint
	jwt.StandardClaims
}

func ReleaseToken(user model.User)  (string, error){
	expirationTime := time.Now().Add(7 * 24 * time.Hour)
	claims := &Claims{
		UserID:    user.ID,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
			IssuedAt: time.Now().Unix(),
			Issuer: "test",
			Subject: "user token",
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	if tokenString, err := token.SignedString(jwtkey); err != nil {
		return "", err
	} else {
		return tokenString, nil
	}
}

// 解析token
func ParseToken(tokenString string) (*jwt.Token, *Claims, error){
	claims := &Claims{}

	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (i interface{}, e error) {
		return jwtkey, nil
	})

	return token, claims, err
}