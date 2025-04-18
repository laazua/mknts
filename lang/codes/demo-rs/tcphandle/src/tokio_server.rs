// 服务器端代码
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::{TcpListener, TcpStream};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;
    println!("Server running on 127.0.0.1:8080");

    loop {
        let (mut socket, _) = listener.accept().await?;

        // 处理每个客户端的连接
        tokio::spawn(async move {
            let mut buf = [0; 4]; // 消息头长度为4字节，存储消息体长度
            loop {
                // 读取消息头
                match socket.read_exact(&mut buf).await {
                    Ok(_) => {
                        let length = u32::from_be_bytes(buf) as usize; // 解析消息体长度
                        let mut data = vec![0; length];

                        // 读取消息体
                        match socket.read_exact(&mut data).await {
                            Ok(_) => {
                                println!("Received data: {:?}", data);

                                // 这里可以对消息进行处理，例如发送回复
                                socket.write_all(&data).await.unwrap();
                            }
                            Err(e) => {
                                eprintln!("Error reading message body: {}", e);
                                break;
                            }
                        }
                    }
                    Err(e) => {
                        eprintln!("Error reading message length: {}", e);
                        break;
                    }
                }
            }
        });
    }
}
