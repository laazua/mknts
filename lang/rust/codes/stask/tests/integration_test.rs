use stask::{StaskServer, StaskClient, ServerConfig, ClientConfig};
use tokio::time::{timeout, Duration};

#[tokio::test]
async fn test_echo_server() {
    let server_config = ServerConfig {
        bind_addr: "127.0.0.1:0".to_string(),
        ..Default::default()
    };
    
    let server = StaskServer::new(server_config);
    let server_handle = tokio::spawn(async move {
        let _ = server.run().await;
    });
    
    tokio::time::sleep(Duration::from_millis(100)).await;
    
    let client_config = ClientConfig {
        servers: vec!["127.0.0.1:7878".to_string()],
        ..Default::default()
    };
    
    let client = StaskClient::new(client_config).await.unwrap();
    
    let test_msg = b"Hello, Stask!".to_vec();
    let response = timeout(
        Duration::from_secs(5),
        client.send_and_wait(test_msg, Some(5))
    ).await.unwrap().unwrap();
    
    assert_eq!(&response, b"Hello, Stask!");
    
    server_handle.abort();
}