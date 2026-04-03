use stask::{StaskServer, ServerConfig};

// 只在启用 tracing feature 时导入
#[cfg(feature = "tracing")]
use tracing_subscriber;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // 条件编译日志初始化
    #[cfg(feature = "tracing")]
    tracing_subscriber::fmt()
        .with_env_filter("info")
        .with_target(false)
        .init();
    
    // 如果没有启用 tracing，使用简单的 println
    #[cfg(not(feature = "tracing"))]
    println!("Stask 服务器启动 (无日志feature)");
    
    // 服务器配置
    let config = ServerConfig {
        bind_addr: "0.0.0.0:7878".to_string(),
        max_connections: 10000,
        ..Default::default()
    };
    
    println!("服务器配置: {:?}", config);
    
    // 创建服务器（使用默认的 Echo 处理器）
    let server = StaskServer::new(config);
    
    // 运行服务器
    if let Err(e) = server.run().await {
        eprintln!("服务器错误: {}", e);
    }
    
    Ok(())
}