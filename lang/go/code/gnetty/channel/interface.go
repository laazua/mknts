package channel

// 确保类型实现了接口
var (
	_ ChannelContext = (*channelContext)(nil)
	_ ChannelContext = (*FrameChannelContext)(nil)
)
