//! stask - 高性能TCP网络框架
//!
//! 提供生产级的TCP客户端和服务端实现，支持：
//! - 异步非阻塞IO
//! - 连接池管理
//! - 自动重连和心跳保活
//! - 负载均衡
//! - 优雅关闭
//! - Prometheus指标集成

pub mod config;
pub mod error;
pub mod protocol;
pub mod server;
pub mod client;

// 重新导出常用类型
pub use config::{ServerConfig, ClientConfig, LoadBalancingStrategy};
pub use error::{StaskError, Result};
pub use protocol::{FramedConnection, Message};
pub use server::StaskServer;
pub use client::StaskClient;

#[cfg(feature = "metrics")]
pub mod metrics;

/// 预导入模块
pub mod prelude {
    pub use crate::{
        StaskServer, StaskClient,
        ServerConfig, ClientConfig,
        StaskError, Result,
        LoadBalancingStrategy,
    };
}

// 版本信息
pub const VERSION: &str = env!("CARGO_PKG_VERSION");
pub const NAME: &str = env!("CARGO_PKG_NAME");