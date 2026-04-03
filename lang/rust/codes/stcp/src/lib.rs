use std::io::{Read, Write, Error, ErrorKind};

/// 最大消息体大小（防止恶意超大包，设为1MB）
pub const MAX_BODY_SIZE: usize = 1024 * 1024;

/// 封装数据包：将消息体打包成 [长度+数据] 格式
pub fn pack_message(data: &[u8]) -> Vec<u8> {
    let len = data.len() as u32;
    let mut packed = Vec::with_capacity(4 + len as usize);
    
    // 写入长度（大端字节序，网络标准）
    packed.extend_from_slice(&len.to_be_bytes());
    packed.extend_from_slice(data);
    
    packed
}

/// 从流中解析一个完整的数据包
/// 返回: Ok(Some(data)) 表示成功读取一个包
///       Ok(None) 表示连接已关闭
///       Err(e) 表示读取错误或协议错误
pub fn read_packet(stream: &mut impl Read) -> std::io::Result<Option<Vec<u8>>> {
    // 1. 读取消息头（4字节长度）
    let mut len_buf = [0u8; 4];
    match stream.read_exact(&mut len_buf) {
        Ok(_) => {},
        Err(e) if e.kind() == ErrorKind::UnexpectedEof => return Ok(None),
        Err(e) => return Err(e),
    }
    
    // 解析消息体长度
    let body_len = u32::from_be_bytes(len_buf) as usize;
    
    // 检查长度是否合法
    if body_len == 0 {
        return Ok(Some(Vec::new())); // 空消息体
    }
    
    if body_len > MAX_BODY_SIZE {
        return Err(Error::new(
            ErrorKind::InvalidData,
            format!("消息体过大: {} 字节 (最大允许: {})", body_len, MAX_BODY_SIZE)
        ));
    }
    
    // 2. 读取消息体
    let mut body = vec![0u8; body_len];
    stream.read_exact(&mut body)?;
    
    Ok(Some(body))
}

/// 便捷方法：发送一个打包好的消息
pub fn send_packet(stream: &mut impl Write, data: &[u8]) -> std::io::Result<()> {
    let packet = pack_message(data);
    stream.write_all(&packet)?;
    stream.flush()?; // 确保数据立即发送
    Ok(())
}

/// 测试辅助函数：创建一个简单的测试服务器
#[cfg(test)]
pub mod test_utils {
    use super::*;
    use std::net::{TcpListener};
    use std::thread;
    use std::sync::mpsc;
    
    /// 启动一个测试服务器，返回地址和关闭信号的发送端
    pub fn start_test_server() -> (String, mpsc::Sender<()>) {
        let listener = TcpListener::bind("127.0.0.1:0").unwrap();
        let addr = listener.local_addr().unwrap().to_string();
        let (tx, _rx) = mpsc::channel();
        
        thread::spawn(move || {
            for stream in listener.incoming() {
                match stream {
                    Ok(mut stream) => {
                        // 简单的echo服务
                        thread::spawn(move || {
                            while let Ok(Some(data)) = read_packet(&mut stream) {
                                let _ = send_packet(&mut stream, &data);
                            }
                        });
                    }
                    Err(_) => break,
                }
            }
        });
        
        // 当rx被drop时，listener会被关闭
        (addr, tx)
    }
}