package bootstrap

import (
    "log"
    "net"

    "gnetty/channel"
)

// ClientBootstrap 客户端启动器
type ClientBootstrap struct {
    addr    string
    handler ChannelInitializer
    channel *channel.Channel
}

// NewClientBootstrap 创建新的 ClientBootstrap
func NewClientBootstrap() *ClientBootstrap {
    return &ClientBootstrap{}
}

// SetHandler 设置 Channel 处理器
func (cb *ClientBootstrap) SetHandler(handler ChannelInitializer) *ClientBootstrap {
    cb.handler = handler
    return cb
}

// Connect 连接到服务器
func (cb *ClientBootstrap) Connect(addr string) error {
    cb.addr = addr

    conn, err := net.Dial("tcp", addr)
    if err != nil {
        return err
    }

    ch := channel.NewChannel(conn)
    cb.channel = ch

    log.Printf("[GNetty] Connected to %s\n", addr)

    if cb.handler != nil {
        cb.handler(ch)
    }

    ch.Start()

    return nil
}

// Close 关闭客户端连接
func (cb *ClientBootstrap) Close() error {
    if cb.channel != nil {
        return cb.channel.Close()
    }
    return nil
}

// GetChannel 获取 Channel
func (cb *ClientBootstrap) GetChannel() *channel.Channel {
    return cb.channel
}

// Write 写入数据
func (cb *ClientBootstrap) Write(data []byte) error {
    if cb.channel == nil {
        return ErrChannelNotFound
    }
    return cb.channel.Write(data)
}