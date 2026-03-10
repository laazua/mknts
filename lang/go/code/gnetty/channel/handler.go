package channel

// ChannelHandler Channel 处理器接口
type ChannelHandler interface {
	// HandlerAdded 处理器添加到 Pipeline 时调用
	HandlerAdded(ctx ChannelContext)

	// HandlerRemoved 处理器从 Pipeline 移除时调用
	HandlerRemoved(ctx ChannelContext)

	// ChannelActive Channel 激活时调用（连接建立）
	ChannelActive(ctx ChannelContext)

	// ChannelInactive Channel 非激活时调用（连接关闭）
	ChannelInactive(ctx ChannelContext)

	// ChannelRead 读取数据时调用
	ChannelRead(ctx ChannelContext, msg interface{})

	// ExceptionCaught 异常捕获时调用
	ExceptionCaught(ctx ChannelContext, err error)
}
