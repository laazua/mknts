use std::net::TcpStream;
use std::time::Duration;
use stcp::{send_packet, read_packet};

fn main() -> std::io::Result<()> {
    println!("========================================");
    println!("TCP 协议客户端");
    println!("========================================\n");
    
    let mut stream = TcpStream::connect("127.0.0.1:7878")?;
    println!("✓ 已连接到服务器: {:?}\n", stream.peer_addr()?);
    
    // 准备测试消息
    let messages = vec![
        "第一条消息: Hello, Rust!",
        "第二条消息: 这是一条比较长的消息，用来测试协议的正确性",
        "第三条消息: World!",
        "第四条消息: 测试空消息",
        "",  // 空消息
        "第五条消息: 测试多条连续消息",
    ];
    
    println!("开始发送 {} 条消息...\n", messages.len());
    println!("---");
    
    for (i, msg) in messages.iter().enumerate() {
        println!("[发送 #{}] 准备发送: \"{}\"", i + 1, msg);
        
        // 发送打包好的消息
        match send_packet(&mut stream, msg.as_bytes()) {
            Ok(_) => println!("[发送 #{}] ✓ 已发送 ({} 字节)", i + 1, msg.len()),
            Err(e) => {
                eprintln!("[发送 #{}] ✗ 发送失败: {}", i + 1, e);
                break;
            }
        }
        
        // 接收响应
        match read_packet(&mut stream) {
            Ok(Some(response)) => {
                let response_str = String::from_utf8_lossy(&response);
                println!("[接收 #{}] ✓ 收到回显: \"{}\"", i + 1, response_str);
                
                // 验证响应是否匹配
                if msg.as_bytes() == response.as_slice() {
                    println!("[验证 #{}] ✓ 数据一致", i + 1);
                } else {
                    println!("[验证 #{}] ✗ 数据不一致!", i + 1);
                }
            }
            Ok(None) => {
                println!("[接收 #{}] 服务器关闭了连接", i + 1);
                break;
            }
            Err(e) => {
                eprintln!("[接收 #{}] ✗ 接收失败: {}", i + 1, e);
                break;
            }
        }
        
        println!("---");
        
        // 模拟间隔发送
        if i < messages.len() - 1 {
            std::thread::sleep(Duration::from_millis(500));
        }
    }
    
    println!("\n========================================");
    println!("所有消息发送完毕！");
    println!("========================================");
    
    Ok(())
}