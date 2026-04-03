use stask::{StaskClient, ClientConfig};

// 只在启用 tracing feature 时导入
#[cfg(feature = "tracing")]
use tracing_subscriber;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // 条件编译日志初始化
    #[cfg(feature = "tracing")]
    tracing_subscriber::fmt()
        .with_env_filter("info")
        .init();
    
    #[cfg(not(feature = "tracing"))]
    println!("Stask 客户端启动 (无日志feature)");
    
    let config = ClientConfig {
        servers: vec![
            "127.0.0.1:7878".to_string(),
        ],
        load_balancing: stask::LoadBalancingStrategy::RoundRobin,
        max_pool_size: 10,
        ..Default::default()
    };
    
    let client = StaskClient::new(config).await?;
    
    println!("Stask客户端已启动");
    
    // 发送测试消息
    for i in 0..10 {
        let msg = serde_json::json!({
            "message": format!("Hello from client {}", i),
            "timestamp": chrono::Utc::now().to_rfc3339(),
        }).to_string();
        
        match client.send_and_wait(msg.into_bytes(), Some(5)).await {
            Ok(response) => {
                let response_str = String::from_utf8_lossy(&response);
                println!("收到响应: {}", response_str);
            }
            Err(e) => {
                eprintln!("发送失败: {}", e);
            }
        }
        
        tokio::time::sleep(tokio::time::Duration::from_secs(1)).await;
    }
    
    client.shutdown().await?;
    
    Ok(())
}