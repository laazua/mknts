// 客户端代码
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpStream;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut stream = TcpStream::connect("127.0.0.1:8080").await?;
    println!("Connected to server");

    // 构造消息体
    let message = b"Hello, this is a message from the client.";
    let length = message.len() as u32;
    let length_bytes = length.to_be_bytes();

    // 发送消息头和消息体
    stream.write_all(&length_bytes).await?;
    stream.write_all(message).await?;
    println!("Sent data to server");

    // 接收服务器的响应
    let mut buf = vec![0; message.len()];
    let n = stream.read(&mut buf).await?;
    println!("Received data from server: {:?}", &buf[..n]);

    Ok(())
}
