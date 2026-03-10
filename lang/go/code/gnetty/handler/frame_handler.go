package handler

import (
	"gnetty/channel"
)

// FrameInboundHandler 帧入站处理器
type FrameInboundHandler interface {
	ChannelActive(ctx channel.ChannelContext)
	ChannelInactive(ctx channel.ChannelContext)
	ChannelRead(ctx channel.ChannelContext, msg interface{})
	ExceptionCaught(ctx channel.ChannelContext, err error)
}

// FrameSimpleInboundHandler 简单的帧入站处理器
type FrameSimpleInboundHandler struct {
	onActive   func(ctx channel.ChannelContext)
	onInactive func(ctx channel.ChannelContext)
	onRead     func(ctx channel.ChannelContext, msg interface{})
	onError    func(ctx channel.ChannelContext, err error)
}

// NewFrameSimpleInboundHandler 创建新的简单帧处理器
func NewFrameSimpleInboundHandler() *FrameSimpleInboundHandler {
	return &FrameSimpleInboundHandler{}
}

// OnActive 设置激活事件处理
func (f *FrameSimpleInboundHandler) OnActive(fn func(ctx channel.ChannelContext)) *FrameSimpleInboundHandler {
	f.onActive = fn
	return f
}

// OnInactive 设置非激活事件处理
func (f *FrameSimpleInboundHandler) OnInactive(fn func(ctx channel.ChannelContext)) *FrameSimpleInboundHandler {
	f.onInactive = fn
	return f
}

// OnRead 设置读取事件处理
func (f *FrameSimpleInboundHandler) OnRead(fn func(ctx channel.ChannelContext, msg interface{})) *FrameSimpleInboundHandler {
	f.onRead = fn
	return f
}

// OnError 设置错误处理
func (f *FrameSimpleInboundHandler) OnError(fn func(ctx channel.ChannelContext, err error)) *FrameSimpleInboundHandler {
	f.onError = fn
	return f
}

// HandlerAdded 处理器添加时调用
func (f *FrameSimpleInboundHandler) HandlerAdded(ctx channel.ChannelContext) {
}

// HandlerRemoved 处理器移除时调用
func (f *FrameSimpleInboundHandler) HandlerRemoved(ctx channel.ChannelContext) {
}

// ChannelActive 连接激活时调用
func (f *FrameSimpleInboundHandler) ChannelActive(ctx channel.ChannelContext) {
	if f.onActive != nil {
		f.onActive(ctx)
	}
}

// ChannelInactive 连接非激活时调用
func (f *FrameSimpleInboundHandler) ChannelInactive(ctx channel.ChannelContext) {
	if f.onInactive != nil {
		f.onInactive(ctx)
	}
}

// ChannelRead 读取数据时调用
func (f *FrameSimpleInboundHandler) ChannelRead(ctx channel.ChannelContext, msg interface{}) {
	if f.onRead != nil {
		f.onRead(ctx, msg)
	}
}

// ExceptionCaught 异常捕获
func (f *FrameSimpleInboundHandler) ExceptionCaught(ctx channel.ChannelContext, err error) {
	if f.onError != nil {
		f.onError(ctx, err)
	}
}
