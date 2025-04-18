use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

const HEADER_LEN: usize = 4;

fn handle_client(mut stream: TcpStream) {
    loop {
        let mut header = [0u8; HEADER_LEN];
        match stream.read_exact(&mut header) {
            Ok(_) => {
                let len = u32::from_be_bytes(header) as usize;
                let mut buffer = vec![0u8; len];
                match stream.read_exact(&mut buffer) {
                    Ok(_) => {
                        let message = String::from_utf8(buffer).unwrap();
                        println!("Received From Client: {}", message);
                        // let response = format!("ACK: {}", message);
                        let response = "你好server, 我是client..............................................................................";
                        let response_len = response.len() as u32;
                        let response_header = response_len.to_be_bytes();
                        stream.write_all(&response_header).unwrap();
                        stream.write_all(response.as_bytes()).unwrap();
                    }
                    Err(_e) => {
                        // println!("Error reading message: {}", e);
                        break;
                    }
                }
            }
            Err(_e) => {
                //println!("Error reading header: {}", e);
                break;
            }
        }
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New client connected: {}", stream.peer_addr().unwrap());
                std::thread::spawn(move || {
                    handle_client(stream);
                });
            }
            Err(e) => {
                println!("Error accepting client: {}", e);
            }
        }
    }
}
