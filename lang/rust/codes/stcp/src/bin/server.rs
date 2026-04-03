use std::net::{TcpListener, TcpStream};
use std::thread;
use stcp::{read_packet, send_packet, MAX_BODY_SIZE};

/// 处理单个客户端连接
fn handle_client(mut stream: TcpStream) {
    let peer_addr = stream.peer_addr().unwrap();
    println!("新客户端连接: {}", peer_addr);
    
    let mut message_count = 0;
    
    loop {
        // 使用协议读取一个完整的数据包
        match read_packet(&mut stream) {
            Ok(Some(data)) => {
                message_count += 1;
                // 成功接收到消息
                let message = String::from_utf8_lossy(&data);
                println!("[{}] 收到消息 #{} ({} 字节): {}", 
                         peer_addr, message_count, data.len(), message);
                
                // Echo 回客户端
                if let Err(e) = send_packet(&mut stream, &data) {
                    eprintln!("[{}] 发送响应失败: {}", peer_addr, e);
                    break;
                }
                println!("[{}] 已回显消息 #{}", peer_addr, message_count);
            }
            Ok(None) => {
                // 连接已关闭
                println!("[{}] 客户端已断开连接，共处理 {} 条消息", 
                         peer_addr, message_count);
                break;
            }
            Err(e) => {
                eprintln!("[{}] 读取数据包失败: {}", peer_addr, e);
                break;
            }
        }
    }
}

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:7878")?;
    println!("========================================");
    println!("TCP 协议服务器已启动");
    println!("监听地址: 127.0.0.1:7878");
    println!("协议格式: 消息头(4字节长度) + 消息体");
    println!("最大消息体: {} MB", MAX_BODY_SIZE / 1024 / 1024);
    println!("========================================\n");
    
    let mut connection_count = 0;
    
    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                connection_count += 1;
                println!("收到新的连接请求 (#{})", connection_count);
                thread::spawn(|| handle_client(stream));
            }
            Err(e) => eprintln!("连接失败: {}", e),
        }
    }
    
    Ok(())
}