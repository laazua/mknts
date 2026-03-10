package handler

import (
	"gnetty/channel"
)

// SimpleInboundHandler 简单的入站处理器
type SimpleInboundHandler struct {
	onActive   func(ctx channel.ChannelContext)
	onInactive func(ctx channel.ChannelContext)
	onRead     func(ctx channel.ChannelContext, msg interface{})
	onError    func(ctx channel.ChannelContext, err error)
}

// NewSimpleInboundHandler 创建新的简单处理器
func NewSimpleInboundHandler() *SimpleInboundHandler {
	return &SimpleInboundHandler{}
}

// OnActive 设置激活事件处理
func (s *SimpleInboundHandler) OnActive(fn func(ctx channel.ChannelContext)) *SimpleInboundHandler {
	s.onActive = fn
	return s
}

// OnInactive 设置非激活事件处理
func (s *SimpleInboundHandler) OnInactive(fn func(ctx channel.ChannelContext)) *SimpleInboundHandler {
	s.onInactive = fn
	return s
}

// OnRead 设置读取事件处理
func (s *SimpleInboundHandler) OnRead(fn func(ctx channel.ChannelContext, msg interface{})) *SimpleInboundHandler {
	s.onRead = fn
	return s
}

// OnError 设置错误处理
func (s *SimpleInboundHandler) OnError(fn func(ctx channel.ChannelContext, err error)) *SimpleInboundHandler {
	s.onError = fn
	return s
}

// HandlerAdded 处理器添加时调用
func (s *SimpleInboundHandler) HandlerAdded(ctx channel.ChannelContext) {
	// 默认空实现
}

// HandlerRemoved 处理器移除时调用
func (s *SimpleInboundHandler) HandlerRemoved(ctx channel.ChannelContext) {
	// 默认空实现
}

// ChannelActive 连接激活时调用
func (s *SimpleInboundHandler) ChannelActive(ctx channel.ChannelContext) {
	if s.onActive != nil {
		s.onActive(ctx)
	}
}

// ChannelInactive 连接非激活时调用
func (s *SimpleInboundHandler) ChannelInactive(ctx channel.ChannelContext) {
	if s.onInactive != nil {
		s.onInactive(ctx)
	}
}

// ChannelRead 读取数据时调用
func (s *SimpleInboundHandler) ChannelRead(ctx channel.ChannelContext, msg interface{}) {
	if s.onRead != nil {
		s.onRead(ctx, msg)
	}
}

// ExceptionCaught 异常捕获
func (s *SimpleInboundHandler) ExceptionCaught(ctx channel.ChannelContext, err error) {
	if s.onError != nil {
		s.onError(ctx, err)
	}
}
