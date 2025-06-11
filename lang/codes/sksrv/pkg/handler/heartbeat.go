package handler

import (
	"time"

	"sksrv/pkg/comm"
	"sksrv/pkg/server"
)

// HeartbeatHandler 心跳处理器
type HeartbeatHandler struct {
	next server.Handler
}

// NewHeartbeatHandler 创建心跳处理器
func NewHeartbeatHandler(next server.Handler) *HeartbeatHandler {
	return &HeartbeatHandler{next: next}
}

// Handle 处理消息
func (h *HeartbeatHandler) Handle(conn *server.Conn, msg *comm.Message) error {
	// 如果是心跳消息，直接响应
	if msg.Type == comm.BeatMsg {
		response := &comm.Message{
			Type:     comm.BeatMsg,
			CreateAt: time.Now(),
		}
		return conn.SendMessage(response)
	}

	// 否则交给下一个处理器
	return h.next.Handle(conn, msg)
}
