package utils

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"errors"
	"os"
	"strings"
	"time"

	"gkins/env"
)

type payLoad struct {
	Email     string
	ExpiresAt int64
}

// CreateToken 创建token
func CreateToken(email string) (string, error) {
	payload := payLoad{
		Email:     email,
		ExpiresAt: time.Now().Add(env.ParseTDuration(os.Getenv("app.token.expires"))).Unix(),
	}
	payLoadBytes, err := json.Marshal(payload)
	if err != nil {
		return "", err
	}
	// 对 payload 进行 Base64 编码
	encodedPayload := base64.URLEncoding.EncodeToString(payLoadBytes)
	// 生成签名
	signature := generateSignature(encodedPayload, os.Getenv("app.secret.key"))
	// 返回 token
	return encodedPayload + "." + signature, nil
}

// ParseToken 解析token
func ParseToken(token string) (*payLoad, error) {
	parts := strings.Split(token, ".")
	if len(parts) != 2 {
		return nil, errors.New("invalid token format")
	}
	encodedPayload := parts[0]
	signature := parts[1]
	// 验证签名
	expectedSignature := generateSignature(encodedPayload, os.Getenv("app.secret.key"))
	if signature != expectedSignature {
		return nil, errors.New("invalid token signature")
	}
	// 解码 payload
	payloadBytes, err := base64.URLEncoding.DecodeString(encodedPayload)
	if err != nil {
		return nil, errors.New("failed to decode payload")
	}
	// 解析 JSON
	var payload payLoad
	err = json.Unmarshal(payloadBytes, &payload)
	if err != nil {
		return nil, errors.New("failed to parse payload")
	}
	// 检查是否过期
	if payload.ExpiresAt < time.Now().Unix() {
		return nil, errors.New("token has expired")
	}
	return &payload, nil
}

// generateSignature 生成签名
func generateSignature(payload string, secretKey string) string {
	h := hmac.New(sha256.New, []byte(secretKey))
	h.Write([]byte(payload))
	return base64.URLEncoding.EncodeToString(h.Sum(nil))
}
