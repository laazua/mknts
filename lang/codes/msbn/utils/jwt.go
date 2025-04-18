package utils

import (
	"msbn/global"
	"time"

	"github.com/golang-jwt/jwt"
)

type mClaims struct {
	UserName string `json:"username"`
	jwt.StandardClaims
}

// 生成token
func CreateToken(userName string) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodHS256, mClaims{
		userName,
		jwt.StandardClaims{
			NotBefore: int64(time.Now().Unix()),        // token生效时间
			ExpiresAt: int64(time.Now().Unix() + 7200), // token失效时间
		},
	}).SignedString([]byte(global.AppCon.GetString("app.securekey")))
}

// 解析token
func ParseToken(tokenString string) (*mClaims, error) {
	token, err := jwt.ParseWithClaims(tokenString, &mClaims{}, func(token *jwt.Token) (interface{}, error) {
		return []byte(global.AppCon.GetString("app.securekey")), nil
	})

	if claims, ok := token.Claims.(*mClaims); ok && token.Valid {
		//fmt.Printf("%v, %v, %v\n", claims.UserName, claims.RoleName, claims.ExpiresAt)
		return claims, nil
	} else {
		//fmt.Println(err)
		return nil, err
	}
}

// 更新token
func UpdateToken(tokenString string) (string, error) {
	jwt.TimeFunc = func() time.Time {
		return time.Unix(0, 0)
	}
	token, err := jwt.ParseWithClaims(tokenString, &mClaims{}, func(token *jwt.Token) (interface{}, error) {
		return []byte(global.AppCon.GetString("app.securekey")), nil
	})
	if claims, ok := token.Claims.(*mClaims); ok && token.Valid {
		jwt.TimeFunc = time.Now
		claims.StandardClaims.ExpiresAt = int64(time.Now().Add(1 * time.Hour).Unix())
		return CreateToken(claims.UserName)
	}
	return "", err
}
