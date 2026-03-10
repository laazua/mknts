package channel

import (
	"gnetty/buffer"
	"gnetty/codec"
	"net"
	"sync"
	"sync/atomic"
)

// FrameChannelConfig Channel 配置
type FrameChannelConfig struct {
	FrameDecoder codec.FrameDecoder
	ReadBufSize  int
}

// FrameChannel 支持帧处理的 Channel
type FrameChannel struct {
	conn         net.Conn
	id           string
	pipeline     *Pipeline
	readBuf      *buffer.ByteBuffer
	writeQueue   chan []byte
	closeChan    chan struct{}
	closed       int32
	attr         map[string]interface{}
	attrLock     sync.RWMutex
	frameDecoder codec.FrameDecoder
	readBufSize  int
}

// NewFrameChannel 创建支持帧处理的 Channel
func NewFrameChannel(conn net.Conn, config *FrameChannelConfig) *FrameChannel {
	if config == nil {
		config = &FrameChannelConfig{
			FrameDecoder: codec.NewLengthFieldFrameDecoder(4, 1024*1024),
			ReadBufSize:  4096,
		}
	}

	fc := &FrameChannel{
		conn:         conn,
		id:           conn.RemoteAddr().String(),
		pipeline:     NewPipeline(),
		readBuf:      buffer.NewByteBuffer(config.ReadBufSize * 2),
		writeQueue:   make(chan []byte, 100),
		closeChan:    make(chan struct{}),
		attr:         make(map[string]interface{}),
		frameDecoder: config.FrameDecoder,
		readBufSize:  config.ReadBufSize,
	}

	return fc
}

// GetID 获取 Channel ID
func (fc *FrameChannel) GetID() string {
	return fc.id
}

// GetPipeline 获取 Pipeline
func (fc *FrameChannel) GetPipeline() *Pipeline {
	return fc.pipeline
}

// SetAttr 设置属性
func (fc *FrameChannel) SetAttr(key string, value interface{}) {
	fc.attrLock.Lock()
	defer fc.attrLock.Unlock()
	fc.attr[key] = value
}

// GetAttr 获取属性
func (fc *FrameChannel) GetAttr(key string) interface{} {
	fc.attrLock.RLock()
	defer fc.attrLock.RUnlock()
	return fc.attr[key]
}

// Write 写入数据
func (fc *FrameChannel) Write(data []byte) error {
	if fc.IsClosed() {
		return ErrChannelClosed
	}

	select {
	case fc.writeQueue <- data:
		return nil
	case <-fc.closeChan:
		return ErrChannelClosed
	}
}

// Close 关闭 Channel
func (fc *FrameChannel) Close() error {
	if !atomic.CompareAndSwapInt32(&fc.closed, 0, 1) {
		return nil
	}

	close(fc.closeChan)
	fc.conn.Close()

	return nil
}

// IsClosed 检查是否关闭
func (fc *FrameChannel) IsClosed() bool {
	return atomic.LoadInt32(&fc.closed) == 1
}

// Start 启动 Channel
func (fc *FrameChannel) Start() {
	// 创建 FrameChannel 专用上下文
	ctx := NewFrameChannelContext(fc)

	// 触发激活事件
	fc.pipeline.fireChannelActive(ctx)

	go fc.readLoop(ctx)
	go fc.writeLoop()
}

func (fc *FrameChannel) readLoop(ctx ChannelContext) {
	defer func() {
		fc.Close()
		fc.pipeline.fireChannelInactive(ctx)
	}()

	buf := make([]byte, fc.readBufSize)

	for {
		if fc.IsClosed() {
			return
		}

		n, err := fc.conn.Read(buf)
		if err != nil {
			return
		}

		if n > 0 {
			// 将数据写入缓冲区
			if err := fc.readBuf.Write(buf[:n]); err != nil {
				return
			}

			// 尝试解码帧
			data := fc.readBuf.Bytes()
			frames, consumed, err := fc.frameDecoder.Decode(data)

			if err != nil {
				// 帧解析错误
				return
			}

			// 处理解码出的帧
			if len(frames) > 0 {
				// 消费已处理的字节
				fc.readBuf.Skip(consumed)

				// 触发事件
				for _, frame := range frames {
					frameCopy := make([]byte, len(frame))
					copy(frameCopy, frame)
					fc.pipeline.fireChannelRead(ctx, frameCopy)
				}
			}
		}
	}
}

func (fc *FrameChannel) writeLoop() {
	defer fc.Close()

	for {
		select {
		case data, ok := <-fc.writeQueue:
			if !ok {
				return
			}
			_, err := fc.conn.Write(data)
			if err != nil {
				return
			}
		case <-fc.closeChan:
			return
		}
	}
}
