package bootstrap

import (
	"log"
	"net"
	"sync"

	"gnetty/channel"
	"gnetty/codec"
)

// FrameChannelInitializer 帧 Channel 初始化函数
type FrameChannelInitializer func(*channel.FrameChannel)

// FrameServerBootstrap 支持帧处理的服务器启动器
type FrameServerBootstrap struct {
	addr        string
	handler     FrameChannelInitializer
	listener    net.Listener
	connections map[string]*channel.FrameChannel
	connMu      sync.RWMutex
	running     bool
	mu          sync.RWMutex
	frameConfig *channel.FrameChannelConfig
}

// NewFrameServerBootstrap 创建新的框架服务器启动器
func NewFrameServerBootstrap() *FrameServerBootstrap {
	return &FrameServerBootstrap{
		connections: make(map[string]*channel.FrameChannel),
		frameConfig: &channel.FrameChannelConfig{
			FrameDecoder: codec.NewLengthFieldFrameDecoder(4, 1024*1024),
			ReadBufSize:  4096,
		},
	}
}

// SetFrameDecoder 设置帧解码器
func (fsb *FrameServerBootstrap) SetFrameDecoder(decoder codec.FrameDecoder) *FrameServerBootstrap {
	fsb.frameConfig.FrameDecoder = decoder
	return fsb
}

// SetHandler 设置处理器
func (fsb *FrameServerBootstrap) SetHandler(handler FrameChannelInitializer) *FrameServerBootstrap {
	fsb.handler = handler
	return fsb
}

// Bind 绑定并启动
func (fsb *FrameServerBootstrap) Bind(addr string) error {
	fsb.mu.Lock()
	defer fsb.mu.Unlock()

	fsb.addr = addr

	listener, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}

	fsb.listener = listener
	fsb.running = true

	log.Printf("[GNetty] Frame Server listening on %s\n", addr)

	go fsb.accept()
	return nil
}

// Close 关闭服务器
func (fsb *FrameServerBootstrap) Close() error {
	fsb.mu.Lock()
	defer fsb.mu.Unlock()

	if !fsb.running {
		return nil
	}

	fsb.running = false

	if fsb.listener != nil {
		fsb.listener.Close()
	}

	fsb.connMu.Lock()
	for _, ch := range fsb.connections {
		ch.Close()
	}
	fsb.connections = make(map[string]*channel.FrameChannel)
	fsb.connMu.Unlock()

	return nil
}

// GetConnections 获取所有连接
func (fsb *FrameServerBootstrap) GetConnections() map[string]*channel.FrameChannel {
	fsb.connMu.RLock()
	defer fsb.connMu.RUnlock()

	result := make(map[string]*channel.FrameChannel)
	for k, v := range fsb.connections {
		result[k] = v
	}
	return result
}

// BroadCast 广播消息
func (fsb *FrameServerBootstrap) BroadCast(data []byte) {
	fsb.connMu.RLock()
	defer fsb.connMu.RUnlock()

	for _, ch := range fsb.connections {
		if !ch.IsClosed() {
			ch.Write(data)
		}
	}
}

func (fsb *FrameServerBootstrap) accept() {
	for {
		conn, err := fsb.listener.Accept()
		if err != nil {
			return
		}

		ch := channel.NewFrameChannel(conn, fsb.frameConfig)

		fsb.connMu.Lock()
		fsb.connections[ch.GetID()] = ch
		fsb.connMu.Unlock()

		log.Printf("[GNetty] Client connected: %s\n", ch.GetID())

		if fsb.handler != nil {
			fsb.handler(ch)
		}

		ch.Start()
	}
}
