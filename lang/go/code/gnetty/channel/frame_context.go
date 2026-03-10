package channel

// FrameChannelContext FrameChannel 的上下文实现
type FrameChannelContext struct {
	frameChannel *FrameChannel
	pipeline     *Pipeline
	index        int
}

// NewFrameChannelContext 创建 FrameChannel 上下文
func NewFrameChannelContext(fc *FrameChannel) *FrameChannelContext {
	return &FrameChannelContext{
		frameChannel: fc,
		pipeline:     fc.pipeline,
		index:        -1,
	}
}

// Channel 获取 Channel (FrameChannel 不适用，返回 nil)
func (fcc *FrameChannelContext) Channel() *Channel {
	return nil
}

// Next 传递给下一个处理器
func (fcc *FrameChannelContext) Next(msg interface{}) {
	fcc.index++
	if fcc.index < len(fcc.pipeline.handlers) {
		handler := fcc.pipeline.handlers[fcc.index]
		handler.ChannelRead(fcc, msg)
	}
}

// Write 写入数据
func (fcc *FrameChannelContext) Write(msg interface{}) error {
	if data, ok := msg.([]byte); ok {
		return fcc.frameChannel.Write(data)
	}
	return nil
}

// Close 关闭连接
func (fcc *FrameChannelContext) Close() error {
	return fcc.frameChannel.Close()
}

// GetID 获取 ID
func (fcc *FrameChannelContext) GetID() string {
	return fcc.frameChannel.GetID()
}
