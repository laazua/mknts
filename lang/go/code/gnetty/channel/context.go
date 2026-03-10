package channel

// ChannelContext Channel 上下文接口
type ChannelContext interface {
	// Channel 获取 Channel
	Channel() *Channel

	// Next 传递给下一个处理器
	Next(msg interface{})

	// Write 写入数据
	Write(msg interface{}) error

	// Close 关闭连接
	Close() error

	// GetID 获取 Channel ID
	GetID() string
}

// channelContext 标准 Channel 的上下文实现
type channelContext struct {
	channel  *Channel
	pipeline *Pipeline
	index    int
}

// newChannelContext 创建新的 Channel 上下文
func newChannelContext(ch *Channel) *channelContext {
	return &channelContext{
		channel:  ch,
		pipeline: ch.pipeline,
		index:    -1,
	}
}

// Channel 获取 Channel
func (cc *channelContext) Channel() *Channel {
	return cc.channel
}

// Next 传递给下一个处理器
func (cc *channelContext) Next(msg interface{}) {
	cc.index++
	if cc.index < len(cc.pipeline.handlers) {
		handler := cc.pipeline.handlers[cc.index]
		handler.ChannelRead(cc, msg)
	}
}

// Write 写入数据
func (cc *channelContext) Write(msg interface{}) error {
	if data, ok := msg.([]byte); ok {
		return cc.channel.Write(data)
	}
	return nil
}

// Close 关闭连接
func (cc *channelContext) Close() error {
	return cc.channel.Close()
}

// GetID 获取 ID
func (cc *channelContext) GetID() string {
	return cc.channel.GetID()
}
