package bootstrap

import (
    "log"
    "net"
    "sync"

    "gnetty/channel"
)

// ChannelInitializer Channel 初始化函数
type ChannelInitializer func(*channel.Channel)

// ServerBootstrap 服务器启动器
type ServerBootstrap struct {
    addr        string
    handler     ChannelInitializer
    listener    net.Listener
    connections map[string]*channel.Channel
    connMu      sync.RWMutex
    running     bool
    mu          sync.RWMutex
}

// NewServerBootstrap 创建新的 ServerBootstrap
func NewServerBootstrap() *ServerBootstrap {
    return &ServerBootstrap{
        connections: make(map[string]*channel.Channel),
    }
}

// SetHandler 设置 Channel 处理器
func (sb *ServerBootstrap) SetHandler(handler ChannelInitializer) *ServerBootstrap {
    sb.handler = handler
    return sb
}

// Bind 绑定地址并启动服务器
func (sb *ServerBootstrap) Bind(addr string) error {
    sb.mu.Lock()
    defer sb.mu.Unlock()

    sb.addr = addr

    listener, err := net.Listen("tcp", addr)
    if err != nil {
        return err
    }

    sb.listener = listener
    sb.running = true

    log.Printf("[GNetty] Server listening on %s\n", addr)

    go sb.accept()
    return nil
}

// Close 关闭服务器
func (sb *ServerBootstrap) Close() error {
    sb.mu.Lock()
    defer sb.mu.Unlock()

    if !sb.running {
        return nil
    }

    sb.running = false

    if sb.listener != nil {
        sb.listener.Close()
    }

    sb.connMu.Lock()
    for _, ch := range sb.connections {
        ch.Close()
    }
    sb.connections = make(map[string]*channel.Channel)
    sb.connMu.Unlock()

    return nil
}

// GetConnections 获取所有连接
func (sb *ServerBootstrap) GetConnections() map[string]*channel.Channel {
    sb.connMu.RLock()
    defer sb.connMu.RUnlock()

    result := make(map[string]*channel.Channel)
    for k, v := range sb.connections {
        result[k] = v
    }
    return result
}

// BroadCast 广播消息
func (sb *ServerBootstrap) BroadCast(data []byte) {
    sb.connMu.RLock()
    defer sb.connMu.RUnlock()

    for _, ch := range sb.connections {
        if !ch.IsClosed() {
            ch.Write(data)
        }
    }
}

func (sb *ServerBootstrap) accept() {
    for {
        conn, err := sb.listener.Accept()
        if err != nil {
            return
        }

        ch := channel.NewChannel(conn)

        sb.connMu.Lock()
        sb.connections[ch.GetID()] = ch
        sb.connMu.Unlock()

        log.Printf("[GNetty] Client connected: %s\n", ch.GetID())

        if sb.handler != nil {
            sb.handler(ch)
        }

        ch.Start()
    }
}