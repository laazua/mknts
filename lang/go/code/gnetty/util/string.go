package util

import (
    "fmt"
    "strings"
)

// BytesToHex 将字节转换为十六进制字符串
func BytesToHex(data []byte) string {
    return fmt.Sprintf("%x", data)
}

// HexToBytes 将十六进制字符串转换为字节
func HexToBytes(hexStr string) ([]byte, error) {
    hexStr = strings.TrimSpace(hexStr)
    if len(hexStr)%2 != 0 {
        hexStr = "0" + hexStr
    }

    result := make([]byte, len(hexStr)/2)
    for i := 0; i < len(hexStr); i += 2 {
        var b byte
        fmt.Sscanf(hexStr[i:i+2], "%x", &b)
        result[i/2] = b
    }

    return result, nil
}

// Contains 检查字符串是否包含子字符串
func Contains(s, substr string) bool {
    return strings.Contains(s, substr)
}

// TrimSpace 删除首尾空格
func TrimSpace(s string) string {
    return strings.TrimSpace(s)
}