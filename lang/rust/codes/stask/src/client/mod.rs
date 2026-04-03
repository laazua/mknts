mod connection;
mod load_balancer;

pub use connection::ClientConnection;
pub use load_balancer::{LoadBalancer, RoundRobinBalancer};

use crate::config::ClientConfig;
use crate::error::{StaskError, Result};
use crate::protocol::Message;
use tokio::sync::{mpsc, RwLock};
use tracing::{info, error, debug};
use std::sync::Arc;
use std::time::Duration;

pub struct StaskClient {
    config: Arc<ClientConfig>,
    load_balancer: Arc<RoundRobinBalancer>,
    send_tx: mpsc::Sender<Message>,
    stats: Arc<RwLock<ClientStats>>,
}

#[derive(Debug, Clone, Default)]
pub struct ClientStats {
    pub total_messages_sent: u64,
    pub total_messages_received: u64,
    pub active_connections: usize,
    pub reconnect_attempts: u64,
    pub last_heartbeat: Option<chrono::DateTime<chrono::Utc>>,
}

impl StaskClient {
    pub async fn new(config: ClientConfig) -> Result<Self> {
        let config = Arc::new(config);
        let load_balancer = Arc::new(RoundRobinBalancer::new(config.servers.clone()));
        
        let (send_tx, send_rx) = mpsc::channel(config.send_queue_size);  // 移除 mut
        
        let client = Self {
            config: config.clone(),
            load_balancer,
            send_tx,
            stats: Arc::new(RwLock::new(ClientStats::default())),
        };
        
        // 启动消息发送器
        let client_clone = client.clone();
        tokio::spawn(async move {
            client_clone.message_sender_loop(send_rx).await;
        });
        
        Ok(client)
    }
    
    async fn message_sender_loop(&self, mut rx: mpsc::Receiver<Message>) {
        info!("消息发送器已启动");
        
        while let Some(msg) = rx.recv().await {
            if let Err(e) = self.send_message_internal(msg).await {
                error!("发送消息失败: {}", e);
            }
        }
        
        info!("消息发送器已停止");
    }
    
    async fn send_message_internal(&self, msg: Message) -> Result<()> {
        let addr = self.load_balancer.next_addr().await?;
        let mut conn = ClientConnection::connect(&addr, &self.config.connection).await?;
        
        conn.send(&msg.data).await?;
        
        let mut stats = self.stats.write().await;
        stats.total_messages_sent += 1;
        
        debug!("消息已发送: id={}, 大小={}", msg.id, msg.len());
        
        Ok(())
    }
    
    pub async fn send(&self, data: Vec<u8>) -> Result<u64> {
        let msg = Message::new(data);
        let msg_id = msg.id;
        
        self.send_tx
            .send(msg)
            .await
            .map_err(|_| StaskError::Unknown("发送通道已关闭".to_string()))?;
        
        Ok(msg_id)
    }
    
    pub async fn send_and_wait(
        &self,
        data: Vec<u8>,
        timeout_secs: Option<u64>,
    ) -> Result<Vec<u8>> {
        let timeout = timeout_secs.unwrap_or(self.config.request_timeout_secs);
        let addr = self.load_balancer.next_addr().await?;
        let mut conn = ClientConnection::connect(&addr, &self.config.connection).await?;
        
        conn.send(&data).await?;
        
        let response = tokio::time::timeout(
            Duration::from_secs(timeout),
            conn.recv(),
        )
        .await
        .map_err(|_| StaskError::Timeout("请求超时".to_string()))?
        .map_err(|e| StaskError::Protocol(e.to_string()))?;
        
        match response {
            Some(data) => Ok(data.to_vec()),
            None => Err(StaskError::ConnectionClosed),
        }
    }
    
    pub async fn get_stats(&self) -> ClientStats {
        self.stats.read().await.clone()
    }
    
    pub async fn shutdown(&self) -> Result<()> {
        info!("正在关闭客户端...");
        // 等待队列中的消息发送完成
        tokio::time::sleep(Duration::from_secs(1)).await;
        info!("客户端已关闭");
        Ok(())
    }
}

impl Clone for StaskClient {
    fn clone(&self) -> Self {
        Self {
            config: self.config.clone(),
            load_balancer: self.load_balancer.clone(),
            send_tx: self.send_tx.clone(),
            stats: self.stats.clone(),
        }
    }
}