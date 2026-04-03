use stask::{StaskServer, ServerConfig, server::EchoHandler};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let config = ServerConfig::default();
    let server = StaskServer::with_handler(config.clone(), EchoHandler);  // 克隆
    println!("Echo服务器启动在 {}", config.bind_addr);  // 使用原始值
    server.run().await?;
    
    Ok(())
}