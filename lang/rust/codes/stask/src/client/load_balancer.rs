use crate::error::{StaskError, Result};
use async_trait::async_trait;
use std::sync::atomic::{AtomicUsize, Ordering};

#[async_trait]
pub trait LoadBalancer: Send + Sync {
    async fn next_addr(&self) -> Result<String>;
}

pub struct RoundRobinBalancer {
    addresses: Vec<String>,
    counter: AtomicUsize,
}

impl RoundRobinBalancer {
    pub fn new(addresses: Vec<String>) -> Self {
        Self {
            addresses,
            counter: AtomicUsize::new(0),
        }
    }
}

#[async_trait]
impl LoadBalancer for RoundRobinBalancer {
    async fn next_addr(&self) -> Result<String> {
        if self.addresses.is_empty() {
            return Err(StaskError::ServiceUnavailable);
        }
        
        let idx = self.counter.fetch_add(1, Ordering::SeqCst) % self.addresses.len();
        Ok(self.addresses[idx].clone())
    }
}

impl Clone for RoundRobinBalancer {
    fn clone(&self) -> Self {
        Self {
            addresses: self.addresses.clone(),
            counter: AtomicUsize::new(0),
        }
    }
}