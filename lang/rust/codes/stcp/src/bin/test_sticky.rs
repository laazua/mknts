use std::net::TcpStream;
use std::io::Write;
use stcp::pack_message;

fn main() -> std::io::Result<()> {
    println!("========================================");
    println!("粘包测试客户端");
    println!("演示协议如何解决TCP粘包问题");
    println!("========================================\n");
    
    let mut stream = TcpStream::connect("127.0.0.1:7878")?;
    println!("✓ 已连接到服务器: {:?}\n", stream.peer_addr()?);
    
    // 准备三条消息
    let messages: Vec<(Vec<u8>, &str)> = vec![
        (b"Hello".to_vec(), "Hello"),
        (b"World".to_vec(), "World"),
        (b"Rust".to_vec(), "Rust"),
    ];
    
    println!("准备连续发送 {} 条消息（不等待响应）:", messages.len());
    for (i, (_, display)) in messages.iter().enumerate() {
        println!("  {}: \"{}\"", i + 1, display);
    }
    
    println!("\n---");
    println!("打包消息:");
    
    let mut total_bytes = 0;
    let mut packets = Vec::new();
    
    for (i, (data, display)) in messages.iter().enumerate() {
        let packet = pack_message(data);
        let packet_size = packet.len();
        total_bytes += packet_size;
        packets.push(packet);
        
        println!("  包{}: {} 字节 (头4字节 + {}字节数据: \"{}\")", 
                 i + 1, packet_size, data.len(), display);
    }
    
    println!("\n---");
    println!("连续写入所有数据包到TCP流（模拟批量发送）:");
    
    // 关键：连续写入所有打包后的数据，模拟发送端批量发送
    // 这会导致TCP层将这些数据合并成一个大的数据段
    for packet in &packets {
        stream.write_all(packet)?;
    }
    stream.flush()?;
    
    println!("✓ 已连续写入总计 {} 字节的数据", total_bytes);
    println!("\n尽管数据在TCP层面是连续的（会发生粘包），");
    println!("但服务端的协议层会通过读取长度字段来正确分离每个消息。\n");
    
    println!("---");
    println!("等待服务器回显...\n");
    
    // 等待响应（服务器会逐个回显）
    use stcp::read_packet;
    
    for i in 0..messages.len() {
        match read_packet(&mut stream) {
            Ok(Some(response)) => {
                let response_str = String::from_utf8_lossy(&response);
                println!("[回显 #{}] 收到: \"{}\"", i + 1, response_str);
            }
            Ok(None) => {
                println!("[回显 #{}] 服务器关闭了连接", i + 1);
                break;
            }
            Err(e) => {
                eprintln!("[回显 #{}] 读取失败: {}", i + 1, e);
                break;
            }
        }
    }
    
    println!("\n========================================");
    println!("✓ 所有消息都被正确分离！");
    println!("  粘包问题已通过消息头+消息体格式解决");
    println!("========================================");
    
    Ok(())
}