package codec

import (
    "bytes"
    "encoding/binary"
)

// Decoder 解码器接口
type Decoder interface {
    Decode(data []byte) (interface{}, error)
}

// ByteDecoder 字节解码器
type ByteDecoder struct{}

// Decode 将字节解码为字节
func (bd *ByteDecoder) Decode(data []byte) (interface{}, error) {
    return data, nil
}

// StringDecoder 字符串解码器
type StringDecoder struct{}

// Decode 将字节解码为字符串
func (sd *StringDecoder) Decode(data []byte) (interface{}, error) {
    return string(data), nil
}

// IntDecoder 整数解码器（大端序）
type IntDecoder struct {
    size int // 整数大小（字节）
}

// NewIntDecoder 创建整数解码器
func NewIntDecoder(size int) *IntDecoder {
    if size <= 0 {
        size = 4
    }
    return &IntDecoder{size: size}
}

// Decode 将字节解码为整数
func (id *IntDecoder) Decode(data []byte) (interface{}, error) {
    if len(data) < id.size {
        return nil, ErrInsufficientData
    }

    buf := bytes.NewReader(data[:id.size])

    switch id.size {
    case 2:
        var v int16
        binary.Read(buf, binary.BigEndian, &v)
        return v, nil
    case 4:
        var v int32
        binary.Read(buf, binary.BigEndian, &v)
        return v, nil
    case 8:
        var v int64
        binary.Read(buf, binary.BigEndian, &v)
        return v, nil
    default:
        var v int32
        binary.Read(buf, binary.BigEndian, &v)
        return v, nil
    }
}

// LengthFieldDecoder 长度前缀解码器
// 格式: [长度(lengthSize字节)][数据]
type LengthFieldDecoder struct {
    lengthSize int // 长度字段大小（字节）
    buffer     *bytes.Buffer
}

// NewLengthFieldDecoder 创建长度前缀解码器
func NewLengthFieldDecoder(lengthSize int) *LengthFieldDecoder {
    if lengthSize <= 0 {
        lengthSize = 4
    }
    return &LengthFieldDecoder{
        lengthSize: lengthSize,
        buffer:     bytes.NewBuffer([]byte{}),
    }
}

// Decode 解码数据
func (lfd *LengthFieldDecoder) Decode(data []byte) (interface{}, error) {
    if len(data) < lfd.lengthSize {
        return nil, ErrInsufficientData
    }

    // 读取长度字段
    lengthBuf := bytes.NewReader(data[:lfd.lengthSize])
    var length int32

    switch lfd.lengthSize {
    case 2:
        var v int16
        binary.Read(lengthBuf, binary.BigEndian, &v)
        length = int32(v)
    case 4:
        binary.Read(lengthBuf, binary.BigEndian, &length)
    case 8:
        var v int64
        binary.Read(lengthBuf, binary.BigEndian, &v)
        length = int32(v)
    default:
        binary.Read(lengthBuf, binary.BigEndian, &length)
    }

    // 检查数据是否完整
    totalLength := lfd.lengthSize + int(length)
    if len(data) < totalLength {
        return nil, ErrInsufficientData
    }

    // 提取数据部分
    payload := data[lfd.lengthSize : lfd.lengthSize+int(length)]
    return payload, nil
}