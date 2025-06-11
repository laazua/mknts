package handler

import (
	"fmt"

	"sksrv/pkg/comm"
	"sksrv/pkg/server"
)

// EchoHandler 回显处理器
type EchoHandler struct{}

// NewEchoHandler 创建回显处理器
func NewEchoHandler() *EchoHandler {
	return &EchoHandler{}
}

// Handle 处理消息
func (h *EchoHandler) Handle(conn *server.Conn, msg *comm.Message) error {
	// 只处理数据消息
	if msg.Type != comm.DataMsg {
		return nil
	}

	fmt.Printf("Received message from %s: %s\n", conn.GetRemoteAddress(), string(msg.Data))

	// 回显消息
	response := &comm.Message{
		Type:     comm.DataMsg,
		Data:     msg.Data,
		CreateAt: msg.CreateAt,
	}

	return conn.SendMessage(response)
}
