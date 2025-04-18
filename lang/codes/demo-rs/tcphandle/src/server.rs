use std::io::Read;
use std::net::{TcpListener, TcpStream};

const MESSAGE_SIZE: usize = 4; // 消息长度前缀的大小

fn handle_client(mut stream: TcpStream) {
    // 读取消息长度前缀
    let mut len_prefix = [0; MESSAGE_SIZE];
    match stream.read_exact(&mut len_prefix) {
        Ok(_) => {
            let message_len = u32::from_be_bytes(len_prefix) as usize;

            // 读取消息体
            let mut buffer = vec![0; message_len];
            match stream.read_exact(&mut buffer) {
                Ok(_) => {
                    let message = String::from_utf8_lossy(&buffer);
                    println!("Received message: {}", message);
                }
                Err(e) => {
                    eprintln!("Failed to read message: {}", e);
                }
            }
        }
        Err(e) => {
            eprintln!("Failed to read message length prefix: {}", e);
        }
    }
}

pub fn run_server() {
    let listener = TcpListener::bind("127.0.0.1:8080").expect("Failed to bind");
    println!("Server listening on port 8080...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New client connected: {:?}", stream.peer_addr());
                std::thread::spawn(move || {
                    handle_client(stream);
                });
            }
            Err(e) => {
                eprintln!("Error accepting connection: {}", e);
            }
        }
    }
}

