use std::io::{Read, Write};
use std::net::TcpStream;
use std::time::Duration;
use std::thread;


const HEADER_LEN: usize = 4;

fn send_message(mut stream: &TcpStream, message: &str) -> String {
    let message_len = message.len() as u32;
    let message_header = message_len.to_be_bytes();
    let message_bytes = message.as_bytes();
    let mut request = Vec::with_capacity(HEADER_LEN + message_bytes.len());
    request.extend_from_slice(&message_header);
    request.extend_from_slice(message_bytes);
    stream.write_all(&request).unwrap();

    let mut header = [0u8; HEADER_LEN];
    match stream.read_exact(&mut header) {
        Ok(stream) => stream,
        Err(_e) => {
            println!("server端关闭!");
        }
    };
    let len = u32::from_be_bytes(header) as usize;
    let mut buffer = vec![0u8; len];
    stream.read_exact(&mut buffer).unwrap();
    let response =  String::from_utf8(buffer).unwrap();
    response
}

fn main() {
    let stream =TcpStream::connect("127.0.0.1:8080").unwrap();

    // let messages = vec!["hello", "world", "how", "are", "you"];
    // for message in messages {
    //    let response = send_message(&stream, message);
    //    println!("Received response: {}", response);
    // }
    loop {
        let response = send_message(&stream, "你好server, 我是client..............................................................................");
        println!("Received From Server: {}", response);
        // 睡眠5秒
        thread::sleep(Duration::from_secs(5));
    }
}
