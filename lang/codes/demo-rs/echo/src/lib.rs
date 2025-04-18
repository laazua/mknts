use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::thread;

pub fn start_server() {
    let listener = TcpListener::bind("127.0.0.1:5000").expect("bind address failure!");
    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(move || handle_client(stream));
            }
            Err(e) => {
                eprintln!("connection error: {}", e);
            }
        }
    }
}

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0];
    loop {
        match stream.read(&mut buffer) {
            Ok(size) if size > 0 => {
                stream.write_all(&buffer[..size]).unwrap();
            }
            _ => break,
        }
    }
}
