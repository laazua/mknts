use async_trait::async_trait;
use std::fmt::Debug;

#[async_trait]
pub trait MessageHandler: Send + Sync + Debug {
    async fn handle(&self, data: &[u8]) -> HandlerResult;
}

pub enum HandlerResult {
    Respond(Vec<u8>),
    Ignore,
    Close,
}

#[derive(Debug)]
pub struct EchoHandler;

#[async_trait]
impl MessageHandler for EchoHandler {
    async fn handle(&self, data: &[u8]) -> HandlerResult {
        HandlerResult::Respond(data.to_vec())
    }
}

#[derive(Debug)]
pub struct NoOpHandler;

#[async_trait]
impl MessageHandler for NoOpHandler {
    async fn handle(&self, _data: &[u8]) -> HandlerResult {
        HandlerResult::Ignore
    }
}

// JSON消息处理器示例
#[derive(Debug)]
pub struct JsonHandler;

#[async_trait]
impl MessageHandler for JsonHandler {
    async fn handle(&self, data: &[u8]) -> HandlerResult {
        match serde_json::from_slice::<serde_json::Value>(data) {
            Ok(json) => {
                // 处理JSON消息
                let response = serde_json::json!({
                    "status": "ok",
                    "echo": json,
                    "timestamp": chrono::Utc::now().to_rfc3339(),
                });
                HandlerResult::Respond(response.to_string().into_bytes())
            }
            Err(e) => {
                let error_response = serde_json::json!({
                    "status": "error",
                    "message": e.to_string(),
                });
                HandlerResult::Respond(error_response.to_string().into_bytes())
            }
        }
    }
}