use std::io::Write;
use std::net::TcpStream;

fn send_message(stream: &mut TcpStream, message: &str) -> std::io::Result<()> {
    // 将消息转换为字节流
    let message_bytes = message.as_bytes();
    let message_len = message_bytes.len();

    // 将消息长度作为前缀写入连接
    // message_len as u32 与server.rs中的MESSAGE_SIZE对应
    let len_prefix = (message_len as u32).to_be_bytes();
    stream.write_all(&len_prefix)?;

    // 写入消息体
    stream.write_all(message_bytes)?;

    Ok(())
}

pub fn run_client() {
    // 建立到服务器的连接
    let mut stream = TcpStream::connect("127.0.0.1:8080").expect("Failed to connect to server");

    // 向服务器发送消息
    let message = "Hello, TCP Server!";
    match send_message(&mut stream, message) {
        Ok(()) => println!("Message sent successfully"),
        Err(e) => eprintln!("Failed to send message: {}", e),
    }
}

