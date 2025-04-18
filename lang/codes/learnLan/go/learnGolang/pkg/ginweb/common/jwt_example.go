package common

import (
	"fmt"
	"time"

	"github.com/dgrijalva/jwt-go"
)

// json web token

type MyClaims struct {
	jwt.StandardClaims
	Username string `json:"username"`
}

var SECRETKEY = []byte("123456")

func EncodeToken1() string {
	t := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"exp":      time.Now().Unix() + 10,
		"iss":      "test",
		"nbf":      time.Now().Unix() - 10,
		"username": "test",
	})

	tokenString, err := t.SignedString(SECRETKEY)
	if err != nil {
		panic("signed string error")
	}

	return tokenString
}

func DecodeToken1(tokentString string) {
	token, err := jwt.ParseWithClaims(tokentString, &MyClaims{}, func(token *jwt.Token) (interface{}, error) {
		return SECRETKEY, nil
	})
	if err != nil {
		panic("Parse claims error.")
	}
	data := token.Claims.(*jwt.MapClaims) // data是一个map
	fmt.Println(data)
}
