use axum::{Router, routing::get};

pub async fn create_route() -> Router {
    Router::new().route("/hello", get(hello))
}

async fn hello() -> &'static str {
    "hello world"
}