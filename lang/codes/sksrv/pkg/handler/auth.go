package handler

import (
	"encoding/json"
	"fmt"
	"time"

	"sksrv/pkg/comm"
	"sksrv/pkg/server"
)

// AuthHandler 认证处理器
type AuthHandler struct {
	next    server.Handler
	tokens  map[string]bool
	timeout time.Duration
}

// NewAuthHandler 创建认证处理器
func NewAuthHandler(tokens []string, next server.Handler) *AuthHandler {
	tokenMap := make(map[string]bool)
	for _, token := range tokens {
		tokenMap[token] = true
	}

	return &AuthHandler{
		next:    next,
		tokens:  tokenMap,
		timeout: comm.AuthTimeout,
	}
}

// Handle 处理消息
func (h *AuthHandler) Handle(conn *server.Conn, msg *comm.Message) error {
	// 如果已经认证，直接交给下一个处理器
	if conn.IsAuthenticated() {
		return h.next.Handle(conn, msg)
	}

	// 检查是否为认证消息
	if msg.Type != comm.AuthMsg {
		return fmt.Errorf("unauthenticated connection")
	}

	// 解析认证信息
	var authInfo comm.AuthInfo
	if err := json.Unmarshal(msg.Data, &authInfo); err != nil {
		return fmt.Errorf("invalid auth message: %v", err)
	}

	// 验证token
	if !h.tokens[authInfo.Token] {
		return fmt.Errorf("authentication failed")
	}

	// 设置认证状态
	conn.SetAuthenticked(true)
	fmt.Printf("Client %s authenticated successfully\n", conn.GetRemoteAddress())

	// 发送认证成功响应
	response := &comm.Message{
		Type:     comm.AuthMsg,
		Data:     []byte(`{"status":"success"}`),
		CreateAt: time.Now(),
	}

	return conn.SendMessage(response)
}
