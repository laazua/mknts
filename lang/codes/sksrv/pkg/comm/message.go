package comm

import "time"

// 消息长度
const MsgLength = 4

const (
	BeatInterval = 30 * time.Second
	AuthTimeout  = 5 * time.Second
	ReadTimeout  = 60 * time.Second
	WriteTimeout = 60 * time.Second
)

// 消息体类型
const (
	AuthMsg = 0x01
	BeatMsg = 0x02
	DataMsg = 0x03
)

type Message struct {
	Type     uint8     // message type
	Length   uint      // message length
	Data     []byte    // menssage content
	CreateAt time.Time // created time
}

// AuthInfo 认证信息
type AuthInfo struct {
	Token string `json:"token"`
}
