package codec

import (
	"bytes"
	"encoding/binary"
	"errors"
)

// FrameDecoder 帧解码器，用于处理粘包问题
type FrameDecoder interface {
	// Decode 从字节数据中解码出完整的一个或多个帧
	// 返回：解码出的帧数据、消费的字节数、错误信息
	Decode(data []byte) ([][]byte, int, error)
}

// LengthFieldFrameDecoder 基于长度字段的帧解码器
// 格式: [长度(lengthSize字节)][数据]
type LengthFieldFrameDecoder struct {
	lengthSize      int // 长度字段大小
	maxFrameLength  int // 最大帧长度
	lengthByteOrder binary.ByteOrder
}

// NewLengthFieldFrameDecoder 创建长度字段帧解码器
func NewLengthFieldFrameDecoder(lengthSize int, maxFrameLength int) *LengthFieldFrameDecoder {
	if lengthSize <= 0 {
		lengthSize = 4
	}
	if maxFrameLength <= 0 {
		maxFrameLength = 1024 * 1024 // 1MB
	}

	return &LengthFieldFrameDecoder{
		lengthSize:      lengthSize,
		maxFrameLength:  maxFrameLength,
		lengthByteOrder: binary.BigEndian,
	}
}

// Decode 解码帧
func (lfd *LengthFieldFrameDecoder) Decode(data []byte) ([][]byte, int, error) {
	var frames [][]byte
	consumed := 0

	for consumed < len(data) {
		remaining := len(data) - consumed
		if remaining < lfd.lengthSize {
			// 数据不足以读取长度字段
			break
		}

		// 读取长度字段
		lengthData := data[consumed : consumed+lfd.lengthSize]
		var frameLength int32

		switch lfd.lengthSize {
		case 2:
			frameLength = int32(lfd.lengthByteOrder.Uint16(lengthData))
		case 4:
			frameLength = int32(lfd.lengthByteOrder.Uint32(lengthData))
		case 8:
			frameLength = int32(int64(lfd.lengthByteOrder.Uint64(lengthData)))
		default:
			frameLength = int32(lfd.lengthByteOrder.Uint32(lengthData))
		}

		// 检查帧长度合法性
		if frameLength < 0 || frameLength > int32(lfd.maxFrameLength) {
			return nil, 0, errors.New("invalid frame length")
		}

		totalLength := lfd.lengthSize + int(frameLength)

		if remaining < totalLength {
			// 数据不足以读取完整的帧
			break
		}

		// 提取帧数据
		frameData := make([]byte, frameLength)
		copy(frameData, data[consumed+lfd.lengthSize:consumed+totalLength])
		frames = append(frames, frameData)

		consumed += totalLength
	}

	return frames, consumed, nil
}

// LineBasedFrameDecoder 基于换行符的帧解码器
// 用于处理以换行符分隔的协议
type LineBasedFrameDecoder struct {
	maxLineLength int
}

// NewLineBasedFrameDecoder 创建基于换行符的帧解码器
func NewLineBasedFrameDecoder(maxLineLength int) *LineBasedFrameDecoder {
	if maxLineLength <= 0 {
		maxLineLength = 65536
	}
	return &LineBasedFrameDecoder{
		maxLineLength: maxLineLength,
	}
}

// Decode 解码帧
func (lfd *LineBasedFrameDecoder) Decode(data []byte) ([][]byte, int, error) {
	var frames [][]byte
	consumed := 0

	for consumed < len(data) {
		// 查找换行符
		idx := bytes.IndexByte(data[consumed:], '\n')
		if idx == -1 {
			// 没有找到换行符，检查是否超过最大行长
			if len(data)-consumed > lfd.maxLineLength {
				return nil, 0, errors.New("line too long")
			}
			break
		}

		// 提取一行数据
		lineLen := idx + 1
		if lineLen > lfd.maxLineLength {
			return nil, 0, errors.New("line too long")
		}

		line := data[consumed : consumed+lineLen]
		// 移除换行符
		line = bytes.TrimSuffix(line, []byte("\n"))
		line = bytes.TrimSuffix(line, []byte("\r"))

		frames = append(frames, line)
		consumed += lineLen
	}

	return frames, consumed, nil
}

// DelimiterFrameDecoder 基于分隔符的帧解码器
type DelimiterFrameDecoder struct {
	delimiter    []byte
	maxFrameSize int
}

// NewDelimiterFrameDecoder 创建基于分隔符的帧解码器
func NewDelimiterFrameDecoder(delimiter []byte, maxFrameSize int) *DelimiterFrameDecoder {
	if maxFrameSize <= 0 {
		maxFrameSize = 1024 * 1024
	}
	return &DelimiterFrameDecoder{
		delimiter:    delimiter,
		maxFrameSize: maxFrameSize,
	}
}

// Decode 解码帧
func (dfd *DelimiterFrameDecoder) Decode(data []byte) ([][]byte, int, error) {
	var frames [][]byte
	consumed := 0

	for consumed < len(data) {
		// 查找分隔符
		idx := bytes.Index(data[consumed:], dfd.delimiter)
		if idx == -1 {
			// 没有找到分隔符
			if len(data)-consumed > dfd.maxFrameSize {
				return nil, 0, errors.New("frame too large")
			}
			break
		}

		// 提取帧数据
		frameData := data[consumed : consumed+idx]
		frames = append(frames, frameData)

		consumed += idx + len(dfd.delimiter)
	}

	return frames, consumed, nil
}

// FixedLengthFrameDecoder 固定长度帧解码器
type FixedLengthFrameDecoder struct {
	frameLength int
}

// NewFixedLengthFrameDecoder 创建固定长度帧解码器
func NewFixedLengthFrameDecoder(frameLength int) *FixedLengthFrameDecoder {
	if frameLength <= 0 {
		frameLength = 1024
	}
	return &FixedLengthFrameDecoder{
		frameLength: frameLength,
	}
}

// Decode 解码帧
func (ffd *FixedLengthFrameDecoder) Decode(data []byte) ([][]byte, int, error) {
	var frames [][]byte
	consumed := 0

	for consumed+ffd.frameLength <= len(data) {
		frameData := make([]byte, ffd.frameLength)
		copy(frameData, data[consumed:consumed+ffd.frameLength])
		frames = append(frames, frameData)
		consumed += ffd.frameLength
	}

	return frames, consumed, nil
}
