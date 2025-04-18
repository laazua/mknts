
use axum::Router;

pub fn new() -> Router {
    Router::new()
        .merge(foo::create_route())
        .merge(bar::create_route())
}

mod foo {
    use axum::{Router, routing::get};
    pub(crate) fn create_route() -> Router {
        Router::new()
            .route("/foo", get(foo))
    }

    async fn foo() ->&'static str {
        "this is a foo test"
    }
}

mod bar {
    use serde::{Deserialize, Serialize};
    use axum::{Router, routing::post, http::StatusCode, Json, extract};

    pub(crate) fn create_route() -> Router {
        Router::new()
            .route("/bar", post(bar))
    }

    #[derive(Deserialize)]
    struct CreateBar {
        bar: String,
    }

    // the output to our `create_user` handler
    #[derive(Serialize)]
    struct Bar {
        id: u64,
        bar: String,
    }
    async fn bar(extract::Json(payload): extract::Json<CreateBar>) -> (StatusCode, Json<Bar>) {
        let bar = Bar{id: 1001, bar: payload.bar};

        (StatusCode::CREATED, Json(bar))
    }
}
