//! Prometheus 指标收集模块
//! 仅在启用 metrics feature 时编译

use lazy_static::lazy_static;
use prometheus::{IntCounter, IntGauge, register_counter, register_gauge};

lazy_static! {
    pub static ref ACTIVE_CONNECTIONS: IntGauge = register_gauge!(
        "stask_active_connections",
        "当前活跃连接数"
    ).unwrap();
    
    pub static ref TOTAL_MESSAGES: IntCounter = register_counter!(
        "stask_total_messages",
        "总消息数"
    ).unwrap();
    
    pub static ref MESSAGE_BYTES: IntCounter = register_counter!(
        "stask_message_bytes",
        "消息总字节数"
    ).unwrap();
    
    pub static ref PROTOCOL_ERRORS: IntCounter = register_counter!(
        "stask_protocol_errors",
        "协议错误次数"
    ).unwrap();
    
    pub static ref CLIENT_MESSAGES_SENT: IntCounter = register_counter!(
        "stask_client_messages_sent",
        "客户端发送消息总数"
    ).unwrap();
    
    pub static ref CLIENT_RECONNECTS: IntCounter = register_counter!(
        "stask_client_reconnects",
        "客户端重连次数"
    ).unwrap();
}

// 提供无操作的指标收集器（当metrics feature未启用时）
#[cfg(not(feature = "metrics"))]
pub mod noop {
    pub struct NoopMetrics;
    
    impl NoopMetrics {
        pub fn inc(&self) {}
        pub fn inc_by(&self, _n: u64) {}
        pub fn set(&self, _n: i64) {}
        pub fn dec(&self) {}
    }
    
    pub static ACTIVE_CONNECTIONS: NoopMetrics = NoopMetrics;
    pub static TOTAL_MESSAGES: NoopMetrics = NoopMetrics;
    pub static MESSAGE_BYTES: NoopMetrics = NoopMetrics;
    pub static PROTOCOL_ERRORS: NoopMetrics = NoopMetrics;
    pub static CLIENT_MESSAGES_SENT: NoopMetrics = NoopMetrics;
    pub static CLIENT_RECONNECTS: NoopMetrics = NoopMetrics;
}