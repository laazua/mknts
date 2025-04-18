package datapack

import (
	"bytes"
	"encoding/binary"
	"errors"
)

var (
	HeadLen       uint32 = 8
	MaxPacketSize        = 512
)

type IMsg interface {
	GetDataLen() uint32
	GetDataId() uint32
	GetData() []byte

	SetDataLen(uint32)
	SetDataId(uint32)
	SetData([]byte)
}

type IData interface {
	GetHeadLen() uint32
	Pack(msg IMsg) ([]byte, error)
	UnPack([]byte) (IMsg, error)
}

type Msg struct {
	Id   uint32
	Len  uint32
	Data []byte
}

func NewMsg(id uint32, data []byte) *Msg {
	return &Msg{
		Id:   id,
		Len:  uint32(len(data)),
		Data: data,
	}
}

func (m Msg) GetDataLen() uint32 {
	return m.Len
}

func (m Msg) GetDataId() uint32 {
	return m.Id
}

func (m Msg) GetData() []byte {
	return m.Data
}

func (m *Msg) SetDataLen(len uint32) {
	m.Len = len
}

func (m *Msg) SetDataId(id uint32) {
	m.Id = id
}

func (m *Msg) SetData(data []byte) {
	m.Data = data
}

type DataPack struct{}

func NewDataPack() IData {
	return &DataPack{}
}

func (d *DataPack) GetHeadLen() uint32 {
	return HeadLen
}

// 封包
func (m *DataPack) Pack(msg IMsg) ([]byte, error) {
	dataBuffer := bytes.NewBuffer([]byte{})

	// 写长度
	if err := binary.Write(dataBuffer, binary.BigEndian, msg.GetDataLen()); err != nil {
		return nil, err
	}
	// 写类型
	if err := binary.Write(dataBuffer, binary.BigEndian, msg.GetDataId()); err != nil {
		return nil, err
	}
	// 写数据
	if err := binary.Write(dataBuffer, binary.BigEndian, msg.GetData()); err != nil {
		return nil, err
	}

	return dataBuffer.Bytes(), nil
}

// 拆包
func (m *DataPack) UnPack(data []byte) (IMsg, error) {
	dataBuffer := bytes.NewReader(data)

	msg := &Msg{}

	// 读长度
	if err := binary.Read(dataBuffer, binary.BigEndian, &msg.Len); err != nil {
		return nil, err
	}
	// 读类型
	if err := binary.Read(dataBuffer, binary.BigEndian, &msg.Id); err != nil {
		return nil, err
	}
	// 判断数据长度是否超出允许的最大包长度
	if msg.Len > uint32(MaxPacketSize) {
		return nil, errors.New("too large data received")
	}

	return msg, nil
}
