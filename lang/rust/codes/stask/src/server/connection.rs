use crate::config::ServerConfig;
use crate::error::Result;
use crate::error::{StaskError};
use crate::protocol::FramedConnection;
use tokio::net::TcpStream;
use bytes::BytesMut;
use std::sync::Arc;
use tokio::sync::Mutex;

#[derive(Debug, Clone)]
pub struct ServerConnection {
    inner: Arc<Mutex<FramedConnection>>,
}

impl ServerConnection {
    pub async fn new(stream: TcpStream, config: &ServerConfig) -> Self {
        let conn = FramedConnection::accept(stream, &config.connection).await;
        Self {
            inner: Arc::new(Mutex::new(conn)),
        }
    }
    
    pub async fn send(&self, data: &[u8]) -> Result<()> {
        let mut conn = self.inner.lock().await;
        conn.send(data).await
    }
    
    pub async fn recv(&self) -> Result<Option<BytesMut>> {
        let mut conn = self.inner.lock().await;
        conn.recv().await
    }
    
    pub async fn shutdown(&self) -> Result<()> {
        let conn = self.inner.lock().await;
        // Clone the connection to take ownership
        let conn_clone = (*conn).try_clone()?;
        conn_clone.shutdown().await
    }
    
    pub fn peer_addr(&self) -> String {
        // 简化实现
        "unknown".to_string()
    }
}

// Add try_clone method to FramedConnection
impl FramedConnection {
    pub fn try_clone(&self) -> Result<Self> {
        // This is a simplified implementation
        // In production, you'd need proper cloning
        Err(StaskError::Protocol("Clone not supported".to_string()))
    }
}