use serde::{Serialize, Deserialize};

// 删除未使用的 Duration 导入
// use std::time::Duration;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum LoadBalancingStrategy {
    RoundRobin,
    Random,
    LeastConnections,
    Sticky,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ConnectionConfig {
    pub connect_timeout_secs: u64,
    pub read_timeout_secs: u64,
    pub write_timeout_secs: u64,
    pub heartbeat_interval_secs: u64,
    pub max_message_size: usize,
    pub enable_heartbeat: bool,
    pub enable_auto_reconnect: bool,
    pub max_reconnect_attempts: u32,
    pub reconnect_base_delay_ms: u64,
    pub max_reconnect_delay_secs: u64,
}

impl Default for ConnectionConfig {
    fn default() -> Self {
        Self {
            connect_timeout_secs: 10,
            read_timeout_secs: 30,
            write_timeout_secs: 30,
            heartbeat_interval_secs: 30,
            max_message_size: 10 * 1024 * 1024,
            enable_heartbeat: true,
            enable_auto_reconnect: true,
            max_reconnect_attempts: 5,
            reconnect_base_delay_ms: 100,
            max_reconnect_delay_secs: 30,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ServerConfig {
    pub bind_addr: String,
    pub connection: ConnectionConfig,
    pub max_connections: usize,
    pub worker_threads: usize,
    pub enable_metrics: bool,
    pub request_timeout_secs: u64,
    pub max_queue_size: usize,
}

impl Default for ServerConfig {
    fn default() -> Self {
        // 获取 CPU 核心数
        let cpu_count = std::thread::available_parallelism()
            .map(|n| n.get())
            .unwrap_or(1);
        
        Self {
            bind_addr: "0.0.0.0:7878".to_string(),
            connection: ConnectionConfig::default(),
            max_connections: 10000,
            worker_threads: cpu_count,
            enable_metrics: true,
            request_timeout_secs: 30,
            max_queue_size: 10000,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClientConfig {
    pub servers: Vec<String>,
    pub connection: ConnectionConfig,
    pub load_balancing: LoadBalancingStrategy,
    pub max_pool_size: usize,
    pub send_queue_size: usize,
    pub enable_metrics: bool,
    pub request_timeout_secs: u64,
    pub enable_auto_reconnect: bool,
}

impl Default for ClientConfig {
    fn default() -> Self {
        Self {
            servers: vec!["127.0.0.1:7878".to_string()],
            connection: ConnectionConfig::default(),
            load_balancing: LoadBalancingStrategy::RoundRobin,
            max_pool_size: 10,
            send_queue_size: 1000,
            enable_metrics: true,
            request_timeout_secs: 30,
            enable_auto_reconnect: true,
        }
    }
}

impl ClientConfig {
    pub fn from_file(path: &str) -> Result<Self, config::ConfigError> {
        let settings = config::Config::builder()
            .add_source(config::File::with_name(path))
            .build()?;
        settings.try_deserialize()
    }
}

impl ServerConfig {
    pub fn from_file(path: &str) -> Result<Self, config::ConfigError> {
        let settings = config::Config::builder()
            .add_source(config::File::with_name(path))
            .build()?;
        settings.try_deserialize()
    }
}