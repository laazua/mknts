package codec

import (
    "bytes"
    "encoding/binary"
    "encoding/json"
)

// StructEncoder 结构体编码器（使用 JSON 格式）
type StructEncoder struct {
    lengthFieldSize int // 长度字段大小
}

// NewStructEncoder 创建结构体编码器
func NewStructEncoder(lengthFieldSize int) *StructEncoder {
    if lengthFieldSize <= 0 {
        lengthFieldSize = 4
    }
    return &StructEncoder{lengthFieldSize: lengthFieldSize}
}

// Encode 将结构体编码为带长度前缀的 JSON 字节
// 格式: [长度(lengthFieldSize字节)][JSON数据]
func (se *StructEncoder) Encode(data interface{}) ([]byte, error) {
    jsonData, err := json.Marshal(data)
    if err != nil {
        return nil, err
    }

    var buf bytes.Buffer
    length := int32(len(jsonData))

    // 写入长度字段
    switch se.lengthFieldSize {
    case 2:
        binary.Write(&buf, binary.BigEndian, int16(length))
    case 4:
        binary.Write(&buf, binary.BigEndian, length)
    case 8:
        binary.Write(&buf, binary.BigEndian, int64(length))
    default:
        binary.Write(&buf, binary.BigEndian, length)
    }

    // 写入 JSON 数据
    buf.Write(jsonData)

    return buf.Bytes(), nil
}

// StructDecoder 结构体解码器
type StructDecoder struct {
    lengthFieldSize int
    buffer          *bytes.Buffer
}

// NewStructDecoder 创建结构体解码器
func NewStructDecoder(lengthFieldSize int) *StructDecoder {
    if lengthFieldSize <= 0 {
        lengthFieldSize = 4
    }
    return &StructDecoder{
        lengthFieldSize: lengthFieldSize,
        buffer:          bytes.NewBuffer([]byte{}),
    }
}

// Decode 解码为 map[string]interface{}
func (sd *StructDecoder) Decode(data []byte) (interface{}, error) {
    if len(data) < sd.lengthFieldSize {
        return nil, ErrInsufficientData
    }

    // 读取长度字段
    lengthBuf := bytes.NewReader(data[:sd.lengthFieldSize])
    var length int32

    switch sd.lengthFieldSize {
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
    totalLength := sd.lengthFieldSize + int(length)
    if len(data) < totalLength {
        return nil, ErrInsufficientData
    }

    // 提取 JSON 数据部分
    jsonData := data[sd.lengthFieldSize : sd.lengthFieldSize+int(length)]

    var result map[string]interface{}
    err := json.Unmarshal(jsonData, &result)
    if err != nil {
        return nil, err
    }

    return result, nil
}

// DecodeToStruct 解码为指定结构体
func (sd *StructDecoder) DecodeToStruct(data []byte, v interface{}) error {
    if len(data) < sd.lengthFieldSize {
        return ErrInsufficientData
    }

    // 读取长度字段
    lengthBuf := bytes.NewReader(data[:sd.lengthFieldSize])
    var length int32

    switch sd.lengthFieldSize {
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
    totalLength := sd.lengthFieldSize + int(length)
    if len(data) < totalLength {
        return ErrInsufficientData
    }

    // 提取 JSON 数据部分
    jsonData := data[sd.lengthFieldSize : sd.lengthFieldSize+int(length)]

    return json.Unmarshal(jsonData, v)
}