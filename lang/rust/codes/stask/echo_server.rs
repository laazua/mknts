use stask::{StaskServer, ServerConfig, server::EchoHandler};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let config = ServerConfig::default();
    let server = StaskServer::with_handler(config, EchoHandler);
    
    println!("Echo服务器启动在 {}", config.bind_addr);
    server.run().await?;
    
    Ok(())
}