package channel

import (
	"net"
	"sync"
	"sync/atomic"
)

// Channel 代表一个网络连接
type Channel struct {
	conn      net.Conn
	id        string
	pipeline  *Pipeline
	readChan  chan []byte
	writeChan chan []byte
	closeChan chan struct{}
	once      sync.Once
	closed    int32
	mu        sync.RWMutex
	attr      map[string]interface{}
	attrLock  sync.RWMutex
}

// NewChannel 创建新的 Channel
func NewChannel(conn net.Conn) *Channel {
	return &Channel{
		conn:      conn,
		id:        conn.RemoteAddr().String(),
		pipeline:  NewPipeline(),
		readChan:  make(chan []byte, 100),
		writeChan: make(chan []byte, 100),
		closeChan: make(chan struct{}),
		attr:      make(map[string]interface{}),
	}
}

// GetID 获取 Channel ID
func (c *Channel) GetID() string {
	return c.id
}

// GetPipeline 获取 Pipeline
func (c *Channel) GetPipeline() *Pipeline {
	return c.pipeline
}

// SetAttr 设置属性
func (c *Channel) SetAttr(key string, value interface{}) {
	c.attrLock.Lock()
	defer c.attrLock.Unlock()
	c.attr[key] = value
}

// GetAttr 获取属性
func (c *Channel) GetAttr(key string) interface{} {
	c.attrLock.RLock()
	defer c.attrLock.RUnlock()
	return c.attr[key]
}

// Write 写入数据
func (c *Channel) Write(data []byte) error {
	if c.IsClosed() {
		return ErrChannelClosed
	}

	select {
	case c.writeChan <- data:
		return nil
	case <-c.closeChan:
		return ErrChannelClosed
	}
}

// Close 关闭 Channel
func (c *Channel) Close() error {
	if !atomic.CompareAndSwapInt32(&c.closed, 0, 1) {
		return nil
	}

	c.once.Do(func() {
		close(c.closeChan)
		c.conn.Close()
	})
	return nil
}

// IsClosed 检查 Channel 是否关闭
func (c *Channel) IsClosed() bool {
	return atomic.LoadInt32(&c.closed) == 1
}

// Start 启动 Channel 读写循环
func (c *Channel) Start() {
	ctx := newChannelContext(c)
	c.pipeline.fireChannelActive(ctx)

	go c.readLoop()
	go c.writeLoop()
}

func (c *Channel) readLoop() {
	defer func() {
		c.Close()
		ctx := newChannelContext(c)
		c.pipeline.fireChannelInactive(ctx)
	}()

	buf := make([]byte, 4096)
	ctx := newChannelContext(c)

	for {
		n, err := c.conn.Read(buf)
		if err != nil {
			return
		}

		data := make([]byte, n)
		copy(data, buf[:n])

		c.pipeline.fireChannelRead(ctx, data)
	}
}

func (c *Channel) writeLoop() {
	defer c.Close()

	for {
		select {
		case data := <-c.writeChan:
			_, err := c.conn.Write(data)
			if err != nil {
				return
			}
		case <-c.closeChan:
			return
		}
	}
}
