# GNetty - Go Network Framework

GNetty 是一个受 Java Netty 框架启发的高性能网络应用框架，使用 Go 语言实现。它提供了异步事件驱动的网络通信能力，适用于构建高并发、低延迟的网络应用。

## 核心设计理念

### 1. Channel（通道）
- 代表与网络实体的连接
- 支持读写操作
- 管理连接的生命周期

### 2. EventLoop（事件循环）
- 单线程处理 Channel 中的所有事件
- 基于 Goroutine 实现
- 保证事件处理的顺序性

### 3. ChannelPipeline（管道）
- 由多个 ChannelHandler 组成的处理链
- 支持入站（Inbound）和出站（Outbound）事件传播
- 支持动态添加/移除处理器

### 4. ChannelHandler（事件处理器）
- 处理网络事件的业务逻辑
- InboundHandler：处理入站数据和连接事件
- OutboundHandler：处理出站数据

### 5. Bootstrap（启动器）
- 简化服务器和客户端的配置和启动
- ServerBootstrap：服务器端启动器
- ClientBootstrap：客户端启动器

## 项目结构

```
gnetty/
├── channel/          # Channel 实现
│   ├── channel.go
│   ├── context.go
│   ├── pipeline.go
│   └── errors.go
├── eventloop/        # EventLoop 实现
│   ├── eventloop.go
│   └── errors.go
├── handler/          # ChannelHandler 相关
│   └── simple_handler.go
├── bootstrap/        # Bootstrap 启动器
│   ├── server.go
│   ├── client.go
│   └── errors.go
├── codec/            # 编码解码器
│   ├── encoder.go
│   ├── decoder.go
│   └── errors.go
├── util/             # 工具函数
│   ├── logger.go
│   ├── pool.go
│   ├── time.go
│   ├── string.go
│   └── errors.go
├── examples/         # 使用示例
│   ├── echo_server.go
│   └── echo_client.go
├── go.mod
└── README.md
```

## 快速开始

### 服务器示例

```go
func main() {
    server := bootstrap.NewServerBootstrap()
    server.SetHandler(func(ch *channel.Channel) {
        h := handler.NewSimpleInboundHandler().
            OnRead(func(ctx channel.ChannelContext, msg interface{}) {
                if data, ok := msg.([]byte); ok {
                    ctx.Channel().Write(data)
                }
            })
        ch.GetPipeline().AddLast(h)
    })
    server.Bind(":8080")
    select {}
}
```

### 客户端示例

```go
func main() {
    client := bootstrap.NewClientBootstrap()
    client.Connect("localhost:8080")
    ch := client.GetChannel()
    ch.Write([]byte("Hello Server"))
}
```

## 功能特性

- ✅ 基于事件驱动的异步网络通信
- ✅ 多种编码解码器
- ✅ 灵活的管道处理机制
- ✅ 优雅的连接管理
- ✅ 线程安全的并发处理
- ✅ 完整的工具库

## 主要模块

### Channel
负责网络连接的抽象和管理。

### EventLoop
处理所有网络事件，基于 Go 的 Goroutine 实现。

### Pipeline
事件处理链，支持链式处理。

### Handler
自定义业务逻辑处理。

### Codec
编码解码器模块，支持多种数据格式：
- ByteEncoder/ByteDecoder
- StringEncoder/StringDecoder
- IntEncoder/IntDecoder
- LengthFieldEncoder/LengthFieldDecoder

### Util
工具函数库：
- Logger：日志记录
- BytePool：字节缓冲池
- GoroutinePool：Goroutine 任务池
- Timer：计时工具
- RateLimiter：速率限制器
- String：字符串工具函数

## 许可证

MIT