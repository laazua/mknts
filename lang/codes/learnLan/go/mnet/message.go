// 消息封装
package mnet

import (
	"bytes"
	"encoding/binary"
)

// 消息对象
type Message struct {
	MsgLen  uint
	MsgData []byte
}

// 抽象消息对象行为
type IMessage interface {
	GetMsgLen() uint
	GetMsgData() []byte
	SetMsgLen(len uint)
	SetMsgData(msg []byte)
}

// 获取消息长度
func (m Message) GetMsgLen() uint {
	return m.MsgLen
}

// 获取消息内容
func (m Message) GetMsgData() []byte {
	return m.MsgData
}

// 设置消息长度
func (m *Message) SetMsgLen(len uint) {
	m.MsgLen = len
}

// 设置消息内容
func (m *Message) SetMsgData(data []byte) {
	m.MsgData = data
}

// 消息封包解包 //
var defaultHeadLen uint = 12

type Packet struct{}

type IPacket interface {
	GetHeadLen() uint
	Pack(msg IMessage) ([]byte, error)
	UnPack([]byte) (IMessage, error)
}

// 获取消息头长度
func (p *Packet) GetHeadLen() uint {
	return defaultHeadLen
}

// 封包
func (p *Packet) Pack(msg IMessage) ([]byte, error) {
	// 创建缓存
	Buffer := bytes.NewBuffer([]byte{})
	// 写入消息内容长度
	if err := binary.Write(Buffer, binary.BigEndian, msg.GetMsgLen()); err != nil {
		return nil, err
	}
	// 写入消息内容
	if err := binary.Write(Buffer, binary.BigEndian, msg.GetMsgData()); err != nil {
		return nil, err
	}
	return Buffer.Bytes(), nil
}

// func (p *Packet) UnPack(data []byte, conn net.Conn) (IMessage, error) {
// 	headData := make([]byte, defaultHeadLen)
//     if _, err := io.ReadFull(conn, headData); err != nil {
// 		return nil, err
// 	}

//     Buffer := bytes.NewReader(headData)
// 	msg := &Message{}
// 	if err := binary.Read(Buffer, binary.BigEndian, &msg.MsgLen); err != nil {
// 		return nil, err
// 	}
//     // 判断消息长度是否超出conn创建的大小，假如大小为1024
// 	if msg.MsgLen > 1024 {
// 		return nil, errors.New("msg too large")
// 	}
// 	return msg
// }
