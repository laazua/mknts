use crate::config::ConnectionConfig;
use crate::error::Result;
use crate::protocol::FramedConnection;
use bytes::BytesMut;

pub struct ClientConnection {
    inner: FramedConnection,
}

impl ClientConnection {
    pub async fn connect(addr: &str, config: &ConnectionConfig) -> Result<Self> {
        let inner = FramedConnection::connect(addr, config).await?;
        Ok(Self { inner })
    }
    
    pub async fn send(&mut self, data: &[u8]) -> Result<()> {
        self.inner.send(data).await
    }
    
    pub async fn recv(&mut self) -> Result<Option<BytesMut>> {
        self.inner.recv().await
    }
    
    pub async fn heartbeat(&mut self) -> Result<()> {
        self.inner.heartbeat().await
    }
    
    pub async fn shutdown(self) -> Result<()> {
        self.inner.shutdown().await
    }
}