mod connection;
mod handler;

pub use connection::ServerConnection;
pub use handler::{MessageHandler, EchoHandler, JsonHandler, NoOpHandler, HandlerResult};

use crate::config::ServerConfig;
use crate::error::Result;
use tokio::net::TcpListener;
use tokio::sync::{broadcast, Semaphore};
use tracing::{info, error, warn, debug};
use std::sync::Arc;
use dashmap::DashMap;
use std::time::Duration;

pub struct StaskServer<H: MessageHandler + Send + Sync + 'static = EchoHandler> {
    config: ServerConfig,
    handler: Arc<H>,
    active_connections: Arc<DashMap<String, ServerConnection>>,
    shutdown_tx: broadcast::Sender<()>,
}

impl StaskServer {
    pub fn new(config: ServerConfig) -> Self {
        Self::with_handler(config, EchoHandler)
    }
}

impl<H: MessageHandler + Send + Sync + 'static> StaskServer<H> {
    pub fn with_handler(config: ServerConfig, handler: H) -> Self {
        let (shutdown_tx, _) = broadcast::channel(1);
        
        Self {
            config,
            handler: Arc::new(handler),
            active_connections: Arc::new(DashMap::new()),
            shutdown_tx,
        }
    }
    
    pub async fn run(&self) -> Result<()> {
        let listener = TcpListener::bind(&self.config.bind_addr).await?;
        info!("Stask服务器启动在 {}", self.config.bind_addr);
        info!("最大连接数: {}", self.config.max_connections);
        info!("工作线程数: {}", self.config.worker_threads);
        
        let connection_semaphore = Arc::new(Semaphore::new(self.config.max_connections));
        let mut shutdown_rx = self.shutdown_tx.subscribe();
        
        loop {
            tokio::select! {
                accept_result = listener.accept() => {
                    match accept_result {
                        Ok((stream, addr)) => {
                            let permit = connection_semaphore.clone().acquire_owned().await;
                            if let Ok(permit) = permit {
                                let handler = self.handler.clone();
                                let config = self.config.clone();
                                let active_connections = self.active_connections.clone();
                                let mut shutdown_rx = self.shutdown_tx.subscribe();
                                
                                tokio::spawn(async move {
                                    let conn = ServerConnection::new(stream, &config).await;
                                    let addr_str = addr.to_string();
                                    
                                    active_connections.insert(addr_str.clone(), conn.clone());
                                    info!("新连接: {}", addr_str);
                                    
                                    let result = Self::handle_connection(
                                        conn,
                                        handler,
                                        &mut shutdown_rx,
                                    ).await;
                                    
                                    active_connections.remove(&addr_str);
                                    drop(permit);
                                    
                                    if let Err(e) = result {
                                        error!("连接处理错误 [{}]: {}", addr_str, e);
                                    }
                                });
                            } else {
                                warn!("连接数已达上限，拒绝连接: {}", addr);
                            }
                        }
                        Err(e) => {
                            error!("接受连接失败: {}", e);
                        }
                    }
                }
                _ = shutdown_rx.recv() => {
                    info!("收到关闭信号，开始优雅关闭...");
                    break;
                }
            }
        }
        
        self.shutdown().await?;
        Ok(())
    }
    
    async fn handle_connection(
        conn: ServerConnection,  // 移除 mut
        handler: Arc<H>,
        shutdown_rx: &mut broadcast::Receiver<()>,
    ) -> Result<()> {
        loop {
            tokio::select! {
                recv_result = conn.recv() => {
                    match recv_result {
                        Ok(Some(data)) => {
                            debug!("收到消息: {} 字节", data.len());
                            
                            match handler.handle(&data).await {
                                HandlerResult::Respond(response) => {
                                    if let Err(e) = conn.send(&response).await {
                                        error!("发送响应失败: {}", e);
                                        break;
                                    }
                                }
                                HandlerResult::Ignore => {}
                                HandlerResult::Close => {
                                    info!("处理器要求关闭连接");
                                    break;
                                }
                            }
                        }
                        Ok(None) => {
                            debug!("连接关闭");
                            break;
                        }
                        Err(e) => {
                            error!("接收消息错误: {}", e);
                            break;
                        }
                    }
                }
                _ = shutdown_rx.recv() => {
                    info!("收到关闭信号，关闭连接");
                    break;
                }
            }
        }
        
        conn.shutdown().await?;
        Ok(())
    }
    
    async fn shutdown(&self) -> Result<()> {
        info!("关闭所有连接...");
        
        for entry in self.active_connections.iter() {
            let conn = entry.value();
            if let Err(e) = conn.shutdown().await {
                error!("关闭连接失败: {}", e);
            }
        }
        
        self.active_connections.clear();
        info!("服务器已关闭");
        
        Ok(())
    }
    
    pub async fn graceful_shutdown(&self) -> Result<()> {
        info!("开始优雅关闭...");
        let _ = self.shutdown_tx.send(());
        tokio::time::sleep(Duration::from_secs(5)).await;
        Ok(())
    }
    
    pub fn active_connections_count(&self) -> usize {
        self.active_connections.len()
    }
}