package channel

import (
	"log"
)

// Pipeline 事件处理管道
type Pipeline struct {
	handlers []ChannelHandler
}

// NewPipeline 创建新的管道
func NewPipeline() *Pipeline {
	return &Pipeline{
		handlers: make([]ChannelHandler, 0),
	}
}

// AddLast 在管道末尾添加处理器
func (p *Pipeline) AddLast(handler ChannelHandler) *Pipeline {
	if handler != nil {
		p.handlers = append(p.handlers, handler)
	}
	return p
}

// AddFirst 在管道开头添加处理器
func (p *Pipeline) AddFirst(handler ChannelHandler) *Pipeline {
	if handler != nil {
		p.handlers = append([]ChannelHandler{handler}, p.handlers...)
	}
	return p
}

// Remove 移除指定的处理器
func (p *Pipeline) Remove(handler ChannelHandler) *Pipeline {
	for i, h := range p.handlers {
		if h == handler {
			p.handlers = append(p.handlers[:i], p.handlers[i+1:]...)
			break
		}
	}
	return p
}

// RemoveAll 移除所有处理器
func (p *Pipeline) RemoveAll() *Pipeline {
	p.handlers = make([]ChannelHandler, 0)
	return p
}

// fireChannelActive 触发 Channel 激活事件
func (p *Pipeline) fireChannelActive(ctx ChannelContext) {
	for _, handler := range p.handlers {
		handler.ChannelActive(ctx)
	}
}

// fireChannelInactive 触发 Channel 非激活事件
func (p *Pipeline) fireChannelInactive(ctx ChannelContext) {
	for _, handler := range p.handlers {
		handler.ChannelInactive(ctx)
	}
}

// fireChannelRead 触发读取事件
func (p *Pipeline) fireChannelRead(ctx ChannelContext, msg interface{}) {
	if len(p.handlers) == 0 {
		log.Printf("[Pipeline] No handlers to process message")
		return
	}

	// 只调用第一个处理器，让它通过 Next() 来传递
	wrappedCtx := &wrappedContext{
		ctx:      ctx,
		index:    -1,
		pipeline: p,
	}
	wrappedCtx.Next(msg)
}

// wrappedContext 包装的上下文，用于在管道中传递
type wrappedContext struct {
	ctx      ChannelContext
	index    int
	pipeline *Pipeline
}

// Channel 获取原始 Channel
func (wc *wrappedContext) Channel() *Channel {
	return wc.ctx.Channel()
}

// Next 传递给下一个处理器
func (wc *wrappedContext) Next(msg interface{}) {
	nextIndex := wc.index + 1
	if nextIndex < len(wc.pipeline.handlers) {
		handler := wc.pipeline.handlers[nextIndex]
		nextWrappedCtx := &wrappedContext{
			ctx:      wc.ctx,
			index:    nextIndex,
			pipeline: wc.pipeline,
		}
		handler.ChannelRead(nextWrappedCtx, msg)
	}
}

// Write 写入数据
func (wc *wrappedContext) Write(msg interface{}) error {
	return wc.ctx.Write(msg)
}

// Close 关闭连接
func (wc *wrappedContext) Close() error {
	return wc.ctx.Close()
}

// GetID 获取 ID
func (wc *wrappedContext) GetID() string {
	return wc.ctx.GetID()
}
