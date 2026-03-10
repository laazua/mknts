package codec

import (
    "encoding/json"
)

// JSONEncoder JSON 编码器
type JSONEncoder struct{}

// Encode 将结构体编码为 JSON 字节
func (je *JSONEncoder) Encode(data interface{}) ([]byte, error) {
    return json.Marshal(data)
}

// JSONDecoder JSON 解码器
type JSONDecoder struct{}

// Decode 将 JSON 字节解码为 map[string]interface{}
func (jd *JSONDecoder) Decode(data []byte) (interface{}, error) {
    var result map[string]interface{}
    err := json.Unmarshal(data, &result)
    if err != nil {
        return nil, err
    }
    return result, nil
}

// DecodeToStruct 将 JSON 字节解码为指定结构体
func (jd *JSONDecoder) DecodeToStruct(data []byte, v interface{}) error {
    return json.Unmarshal(data, v)
}