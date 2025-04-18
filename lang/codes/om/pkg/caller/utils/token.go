package utils

import (
	"time"

	"github.com/golang-jwt/jwt"
	"github.com/spf13/viper"
)

type user struct {
	Name string
	Role []string
}

type mClaims struct {
	jwt.StandardClaims
	User user
}

func CreateToken(username string, roles []string) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodES256, mClaims{
		jwt.StandardClaims{
			NotBefore: int64(time.Now().Unix()),
			ExpiresAt: int64(time.Now().Unix() + viper.GetInt64("jwt_timeout")*60*60),
		},
		user{
			Name: username,
			Role: roles,
		},
	}).SignedString(viper.GetString("jwt_secret"))
}

func ParseToken(token string) (*mClaims, error) {
	t, err := jwt.ParseWithClaims(token, &mClaims{}, func(t *jwt.Token) (interface{}, error) {
		return []byte(viper.GetString("jwt_secret")), nil
	})
	if claims, ok := t.Claims.(*mClaims); ok && t.Valid {
		return claims, nil
	} else {
		return nil, err
	}
}
