package core

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"log/slog"
	"net/http"
	"time"

	"gookins/model"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt"
)

// 哈希用户密码
func HashPassword(password string) string {
	h := hmac.New(sha256.New, []byte(Config.SaltKey))
	h.Write([]byte(password))
	hashedPasswd := h.Sum(nil)
	return base64.StdEncoding.EncodeToString(hashedPasswd)
}

// 验证用户密码
func VerifyPassword(hashPasswd, password string) bool {
	newHash := HashPassword(password)
	return hmac.Equal([]byte(hashPasswd), []byte(newHash))
}

// 生成token
func CreateToken(username string) (string, error) {
	claims := &jwt.MapClaims{
		"username": username,
		"exp":      time.Now().Add(time.Minute * time.Duration(Config.ExpiredTime)).Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenStr, err := token.SignedString([]byte(Config.JwtKey))
	if err != nil {
		slog.Error(err.Error())
		return "", ErrCreateToken
	}
	return tokenStr, nil
}

func ParseToken(tokenStr string) (string, error) {
	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (any, error) {
		// 确保签名方法是我们所期望的
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, ErrUnexpSigMethod
		}
		return []byte(Config.JwtKey), nil
	})
	if err != nil {
		slog.Error(err.Error())
		return "", ErrParseToken
	}
	// 读取 claims
	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		// 检查过期时间
		if exp, ok := claims["exp"].(float64); ok {
			if time.Unix(int64(exp), 0).Before(time.Now()) {
				return "", ErrTokenExpire
			}
		}
		// 返回用户名
		if username, ok := claims["username"].(string); ok {
			return username, nil
		}
	}
	return "", ErrTokenVaild
}

// curl -H "Authorization: valid-token"
func AuthMiddleware() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		tokenStr := ctx.GetHeader("Authorization")
		_, err := ParseToken(tokenStr)
		if err != nil {
			ctx.JSON(http.StatusUnauthorized, model.ApiRespone{Code: http.StatusUnauthorized, Message: err.Error()})
			ctx.Abort()
			return
		}
		ctx.Next()
	}
}

func CorMiddleware() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// 设置允许的源
		ctx.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		// 设置允许的请求方法
		ctx.Writer.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
		// 设置允许的请求头
		ctx.Writer.Header().Set("Access-Control-Allow-Headers", "Origin, Content-Type, Accept, Authorization, X-Token")
		// 允许带有凭证的请求
		ctx.Writer.Header().Set("Access-Control-Allow-Credentials", "true")

		// 如果是 OPTIONS 请求，直接返回 204 状态码
		if ctx.Request.Method == "OPTIONS" {
			ctx.AbortWithStatus(204)
			return
		}

		// 继续处理其他请求
		ctx.Next()
	}
}
