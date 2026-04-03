use thiserror::Error;

#[derive(Error, Debug)]
pub enum StaskError {
    #[error("IO错误: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("协议错误: {0}")]
    Protocol(String),
    
    #[error("消息过大: {0} 字节 (限制: {1})")]
    MessageTooLarge(usize, usize),
    
    #[error("超时: {0}")]
    Timeout(String),
    
    #[error("连接池已满")]
    PoolFull,
    
    #[error("连接已关闭")]
    ConnectionClosed,
    
    #[error("配置错误: {0}")]
    ConfigError(String),
    
    #[error("速率限制")]
    RateLimited,
    
    #[error("重连失败: {0}")]
    ReconnectFailed(String),
    
    #[error("服务不可用")]
    ServiceUnavailable,
    
    #[error("序列化错误: {0}")]
    Serialization(String),
    
    #[error("未知错误: {0}")]
    Unknown(String),
}

pub type Result<T> = std::result::Result<T, StaskError>;