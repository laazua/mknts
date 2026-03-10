package codec

import (
    "bytes"
    "encoding/binary"
)

// Encoder 编码器接口
type Encoder interface {
    Encode(data interface{}) ([]byte, error)
}

// ByteEncoder 字节编码器
type ByteEncoder struct{}

// Encode 将数据编码为字节
func (be *ByteEncoder) Encode(data interface{}) ([]byte, error) {
    if b, ok := data.([]byte); ok {
        return b, nil
    }
    if s, ok := data.(string); ok {
        return []byte(s), nil
    }
    return nil, ErrInvalidData
}

// StringEncoder 字符串编码器
type StringEncoder struct{}

// Encode 将数据编码为字符串字节
func (se *StringEncoder) Encode(data interface{}) ([]byte, error) {
    if s, ok := data.(string); ok {
        return []byte(s), nil
    }
    if b, ok := data.([]byte); ok {
        return b, nil
    }
    return nil, ErrInvalidData
}

// IntEncoder 整数编码器（大端序）
type IntEncoder struct{}

// Encode 将整数编码为字节
func (ie *IntEncoder) Encode(data interface{}) ([]byte, error) {
    var buf bytes.Buffer

    switch v := data.(type) {
    case int32:
        binary.Write(&buf, binary.BigEndian, v)
    case int64:
        binary.Write(&buf, binary.BigEndian, v)
    case int:
        binary.Write(&buf, binary.BigEndian, int64(v))
    default:
        return nil, ErrInvalidData
    }

    return buf.Bytes(), nil
}

// LengthFieldEncoder 长度前缀编码器
// 格式: [长度(4字节)][数据]
type LengthFieldEncoder struct {
    lengthSize int // 长度字段大小（字节）
}

// NewLengthFieldEncoder 创建长度前缀编码器
func NewLengthFieldEncoder(lengthSize int) *LengthFieldEncoder {
    if lengthSize <= 0 {
        lengthSize = 4
    }
    return &LengthFieldEncoder{lengthSize: lengthSize}
}

// Encode 编码数据
func (lfe *LengthFieldEncoder) Encode(data interface{}) ([]byte, error) {
    var payload []byte

    switch v := data.(type) {
    case []byte:
        payload = v
    case string:
        payload = []byte(v)
    default:
        return nil, ErrInvalidData
    }

    var buf bytes.Buffer
    length := int32(len(payload))

    // 写入长度字段
    switch lfe.lengthSize {
    case 2:
        binary.Write(&buf, binary.BigEndian, int16(length))
    case 4:
        binary.Write(&buf, binary.BigEndian, length)
    case 8:
        binary.Write(&buf, binary.BigEndian, int64(length))
    default:
        binary.Write(&buf, binary.BigEndian, length)
    }

    // 写入数据
    buf.Write(payload)

    return buf.Bytes(), nil
}