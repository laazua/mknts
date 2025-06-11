package server

import (
	"bufio"
	"encoding/binary"
	"io"
	"net"
	"sync"
	"time"

	"sksrv/pkg/codec"
	"sksrv/pkg/comm"
)

type Conn struct {
	conn         net.Conn
	codec        codec.Codec
	reader       *bufio.Reader
	writeLock    sync.Mutex
	authenticted bool
	lastActive   time.Time
}

func NewConn(conn net.Conn, codec codec.Codec) *Conn {
	return &Conn{
		conn:       conn,
		codec:      codec,
		reader:     bufio.NewReader(conn),
		lastActive: time.Now(),
	}
}

// 接收消息
func (c *Conn) ReceMessage() (*comm.Message, error) {
	// 设置读取超时时间
	c.conn.SetDeadline(time.Now().Add(comm.ReadTimeout))
	// 读取消息长度
	lenBuffer := make([]byte, comm.MsgLength)
	if _, err := io.ReadFull(c.reader, lenBuffer); err != nil {
		return nil, err
	}
	length := binary.BigEndian.Uint32(lenBuffer)
	// 读取消息内容
	data := make([]byte, length)
	if _, err := io.ReadFull(c.reader, data); err != nil {
		return nil, err
	}
	// 解码消息
	message, err := c.codec.Decode(data)
	if err != nil {
		return nil, err
	}
	c.lastActive = time.Now()
	return message, nil
}

// 发送消息
func (c *Conn) SendMessage(message *comm.Message) error {
	// 加锁
	c.writeLock.Lock()
	defer c.writeLock.Unlock()
	// 编码消息
	data, err := c.codec.Encode(message)
	if err != nil {
		return err
	}
	// 设置超时时间
	c.conn.SetWriteDeadline(time.Now().Add(comm.WriteTimeout))
	// 写入消息长度
	length := make([]byte, comm.MsgLength)
	binary.BigEndian.PutUint32(length, uint32(len(data)))
	if _, err := c.conn.Write(length); err != nil {
		return err
	}
	// 写入消息体内容
	if _, err := c.conn.Write(data); err != nil {
		return err
	}
	return nil
}

// 关闭连接
func (c *Conn) Close() {
	c.conn.Close()
}

// 获取远程地址
func (c *Conn) GetRemoteAddress() net.Addr {
	return c.conn.RemoteAddr()
}

// 设置认证
func (c *Conn) SetAuthenticked(authenticted bool) {
	c.authenticted = authenticted
}

// 获取认证
func (c *Conn) GetAuthenticked() bool {
	return c.authenticted
}

// 获取最后活跃时间
func (c *Conn) GetLastActiveTime() time.Time {
	return c.lastActive
}

// IsAuthenticated 是否已认证
func (c *Conn) IsAuthenticated() bool {
	return c.authenticted
}
