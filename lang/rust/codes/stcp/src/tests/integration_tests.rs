use std::net::TcpStream;
use std::io::{Write, Read};
use std::thread;
use std::time::Duration;


/// 测试基本的打包和解包功能
#[test]
fn test_pack_and_unpack() {
    let test_data = b"Hello, World!";
    let packed = pack_message(test_data);
    
    // 验证打包后的长度：4字节头 + 数据长度
    assert_eq!(packed.len(), 4 + test_data.len());
    
    // 验证头部包含正确的长度
    let len_bytes = &packed[0..4];
    let len = u32::from_be_bytes(len_bytes.try_into().unwrap());
    assert_eq!(len as usize, test_data.len());
    
    // 验证数据部分正确
    assert_eq!(&packed[4..], test_data);
}

/// 测试空消息的打包和解包
#[test]
fn test_empty_message() {
    let test_data: &[u8] = &[];
    let packed = pack_message(test_data);
    
    // 空消息：只有4字节头，值为0
    assert_eq!(packed.len(), 4);
    let len = u32::from_be_bytes(packed[0..4].try_into().unwrap());
    assert_eq!(len, 0);
}

/// 测试多消息的连续打包
#[test]
fn test_multiple_packets() {
    let messages = vec![
        b"First",
        b"Second message",
        b"Third",
    ];
    
    let mut all_packed = Vec::new();
    for msg in &messages {
        all_packed.extend_from_slice(&pack_message(msg));
    }
    
    // 模拟从流中读取
    let mut cursor = std::io::Cursor::new(all_packed);
    let mut received = Vec::new();
    
    while let Ok(Some(data)) = read_packet(&mut cursor) {
        received.push(data);
    }
    
    assert_eq!(received.len(), messages.len());
    for (expected, actual) in messages.iter().zip(received.iter()) {
        assert_eq!(expected.to_vec(), *actual);
    }
}

/// 测试协议边界情况：部分读取
#[test]
fn test_partial_read() {
    let test_data = b"Test message";
    let packed = pack_message(test_data);
    
    // 模拟分两次读取：先读一半
    let half = packed.len() / 2;
    let first_half = &packed[0..half];
    let second_half = &packed[half..];
    
    let mut combined = Vec::new();
    combined.extend_from_slice(first_half);
    
    // 创建一个流，先给一半数据
    let mut cursor = std::io::Cursor::new(combined);
    
    // 第一次读取应该返回None（数据不完整）
    let result = read_packet(&mut cursor);
    assert!(matches!(result, Err(e) if e.kind() == std::io::ErrorKind::UnexpectedEof));
    
    // 添加剩余数据
    cursor.get_mut().extend_from_slice(second_half);
    cursor.set_position(0);
    
    // 现在应该能完整读取
    let result = read_packet(&mut cursor);
    assert!(matches!(result, Ok(Some(data)) if data == test_data));
}

/// 测试无效数据：长度字段过大
#[test]
fn test_invalid_length() {
    // 构造一个长度字段过大的数据包
    let invalid_len = (MAX_BODY_SIZE + 1) as u32;
    let mut packet = Vec::new();
    packet.extend_from_slice(&invalid_len.to_be_bytes());
    packet.extend_from_slice(b"Some data");
    
    let mut cursor = std::io::Cursor::new(packet);
    let result = read_packet(&mut cursor);
    
    assert!(result.is_err());
    let err = result.unwrap_err();
    assert_eq!(err.kind(), std::io::ErrorKind::InvalidData);
}

/// 集成测试：实际的TCP连接（需要服务器在运行）
#[test]
#[ignore] // 默认忽略，需要先手动启动服务器
fn test_real_tcp_connection() {
    let mut stream = TcpStream::connect("127.0.0.1:7878").unwrap();
    
    let test_msg = b"Integration test message";
    send_packet(&mut stream, test_msg).unwrap();
    
    let response = read_packet(&mut stream).unwrap().unwrap();
    assert_eq!(test_msg.to_vec(), response);
}

/// 压力测试：大量消息
#[test]
fn test_many_messages() {
    let messages: Vec<Vec<u8>> = (0..100)
        .map(|i| format!("Message {}", i).into_bytes())
        .collect();
    
    // 打包所有消息
    let mut all_packed = Vec::new();
    for msg in &messages {
        all_packed.extend_from_slice(&pack_message(msg));
    }
    
    // 解包
    let mut cursor = std::io::Cursor::new(all_packed);
    let mut received = Vec::new();
    
    while let Ok(Some(data)) = read_packet(&mut cursor) {
        received.push(data);
    }
    
    assert_eq!(received.len(), messages.len());
    for (expected, actual) in messages.iter().zip(received.iter()) {
        assert_eq!(expected, actual);
    }
}

/// 测试send_packet和read_packet配合使用
#[test]
fn test_send_and_receive() {
    // 使用内存流模拟网络连接
    let mut server_read = Vec::new();
    let mut client_write = Vec::new();
    
    // 模拟客户端发送
    let test_data = b"Test data for round trip";
    send_packet(&mut client_write, test_data).unwrap();
    
    // 模拟服务器接收
    let mut cursor = std::io::Cursor::new(client_write);
    let received = read_packet(&mut cursor).unwrap().unwrap();
    assert_eq!(test_data.to_vec(), received);
    
    // 模拟服务器响应
    send_packet(&mut server_read, &received).unwrap();
    
    // 模拟客户端接收响应
    let mut cursor2 = std::io::Cursor::new(server_read);
    let response = read_packet(&mut cursor2).unwrap().unwrap();
    assert_eq!(test_data.to_vec(), response);
}

/// 测试非UTF-8数据（二进制数据）
#[test]
fn test_binary_data() {
    let binary_data: Vec<u8> = vec![0xFF, 0x00, 0xAA, 0x55, 0x12, 0x34];
    let packed = pack_message(&binary_data);
    
    let mut cursor = std::io::Cursor::new(packed);
    let result = read_packet(&mut cursor).unwrap().unwrap();
    
    assert_eq!(binary_data, result);
}