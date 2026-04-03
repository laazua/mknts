use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpStream;
use tokio::time::timeout;
use crate::error::{StaskError, Result};
use crate::config::ConnectionConfig;
use tracing::debug;
use bytes::BytesMut;
use chrono::{DateTime, Utc};
use std::sync::atomic::{AtomicU64, Ordering};
use std::time::Duration;

#[derive(Debug, Clone)]
pub struct Message {
    pub id: u64,
    pub data: BytesMut,
    pub timestamp: DateTime<Utc>,
}

impl Message {
    pub fn new(data: Vec<u8>) -> Self {
        static COUNTER: AtomicU64 = AtomicU64::new(0);
        Self {
            id: COUNTER.fetch_add(1, Ordering::SeqCst),
            data: BytesMut::from(&data[..]),
            timestamp: Utc::now(),
        }
    }
    
    pub fn len(&self) -> usize {
        self.data.len()
    }
    
    pub fn is_empty(&self) -> bool {
        self.data.is_empty()
    }
    
    pub fn as_slice(&self) -> &[u8] {
        &self.data
    }
}

#[derive(Debug)]
pub struct FramedConnection {
    stream: TcpStream,
    config: ConnectionConfig,
    peer_addr: String,
    message_counter: u64,
}

impl FramedConnection {
    pub async fn connect(
        addr: &str,
        config: &ConnectionConfig,
    ) -> Result<Self> {
        debug!("正在连接到 {}", addr);
        
        let stream = timeout(
            Duration::from_secs(config.connect_timeout_secs),
            TcpStream::connect(addr),
        )
        .await
        .map_err(|_| StaskError::Timeout("连接超时".to_string()))?
        .map_err(StaskError::Io)?;
        
        let peer_addr = stream.peer_addr()?.to_string();
        debug!("已连接到 {}", peer_addr);
        
        Ok(Self {
            stream,
            config: config.clone(),
            peer_addr,
            message_counter: 0,
        })
    }
    
    pub async fn accept(stream: TcpStream, config: &ConnectionConfig) -> Self {
        let peer_addr = stream.peer_addr()
            .map(|addr| addr.to_string())
            .unwrap_or_else(|_| "unknown".to_string());
        
        Self {
            stream,
            config: config.clone(),
            peer_addr,
            message_counter: 0,
        }
    }
    
    pub async fn send(&mut self, data: &[u8]) -> Result<()> {
        if data.len() > self.config.max_message_size {
            return Err(StaskError::MessageTooLarge(
                data.len(),
                self.config.max_message_size,
            ));
        }
        
        let len = data.len() as u32;
        let mut packet = Vec::with_capacity(4 + data.len());
        packet.extend_from_slice(&len.to_be_bytes());
        packet.extend_from_slice(data);
        
        timeout(
            Duration::from_secs(self.config.write_timeout_secs),
            self.stream.write_all(&packet),
        )
        .await
        .map_err(|_| StaskError::Timeout("写入超时".to_string()))?
        .map_err(StaskError::Io)?;
        
        timeout(
            Duration::from_secs(self.config.write_timeout_secs),
            self.stream.flush(),
        )
        .await
        .map_err(|_| StaskError::Timeout("刷新超时".to_string()))?
        .map_err(StaskError::Io)?;
        
        self.message_counter += 1;
        debug!("发送消息: {} 字节", data.len());
        
        Ok(())
    }
    
    pub async fn recv(&mut self) -> Result<Option<BytesMut>> {
        let mut len_buf = [0u8; 4];
        let read_result = timeout(
            Duration::from_secs(self.config.read_timeout_secs),
            self.stream.read_exact(&mut len_buf),
        ).await;
        
        match read_result {
            Ok(Ok(_)) => {}
            Ok(Err(e)) => {
                if e.kind() == std::io::ErrorKind::UnexpectedEof {
                    return Ok(None);
                }
                return Err(StaskError::Io(e));
            }
            Err(_) => {
                return Err(StaskError::Timeout("读取超时".to_string()));
            }
        }
        
        let body_len = u32::from_be_bytes(len_buf) as usize;
        
        if body_len > self.config.max_message_size {
            return Err(StaskError::MessageTooLarge(
                body_len,
                self.config.max_message_size,
            ));
        }
        
        if body_len == 0 {
            return Ok(Some(BytesMut::new()));
        }
        
        let mut body = vec![0u8; body_len];
        timeout(
            Duration::from_secs(self.config.read_timeout_secs),
            self.stream.read_exact(&mut body),
        )
        .await
        .map_err(|_| StaskError::Timeout("读取超时".to_string()))?
        .map_err(StaskError::Io)?;
        
        debug!("接收消息: {} 字节", body_len);
        
        Ok(Some(BytesMut::from(&body[..])))
    }
    
    pub async fn heartbeat(&mut self) -> Result<()> {
        let heartbeat_data = b"__HEARTBEAT__";
        self.send(heartbeat_data).await?;
        
        match self.recv().await? {
            Some(data) if &data[..] == heartbeat_data => Ok(()),
            Some(_) => Err(StaskError::Protocol("心跳响应错误".to_string())),
            None => Err(StaskError::ConnectionClosed),
        }
    }
    
    pub async fn shutdown(mut self) -> Result<()> {
        debug!("关闭连接: {}", self.peer_addr);
        self.stream.shutdown().await?;
        Ok(())
    }
    
    pub fn peer_addr(&self) -> &str {
        &self.peer_addr
    }
    
    pub fn message_count(&self) -> u64 {
        self.message_counter
    }
}