use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::thread;

fn handle_client(mut client_stream: TcpStream, server_addr: &str) {
    match TcpStream::connect(server_addr) {
        Ok(mut server_stream) => {
            println!("connection server success: {}", server_addr);

            let mut client_stream_clone = client_stream.try_clone().expect("clone client stream failure");
            let mut server_stream_clone = server_stream.try_clone().expect("clone server stream failure");

            let client_to_server = thread::spawn(move || {
                let mut buffer = [0; 1024];
                loop {
                    match client_stream_clone.read(&mut buffer) {
                        Ok(size) if size > 0 => {
                            let _ = server_stream_clone.write_all(&buffer[..size]);
                        }
                        _ => {
                            break;
                        }
                    }
                }
            });

            let server_to_client = thread::spawn(move || {
                let mut buffer = [0; 1024];
                loop {
                    match server_stream.read(&mut buffer) {
                        Ok(size) if size > 0 => {
                            let _ = client_stream.write_all(&buffer[..size]);
                        }
                        _ => {
                            break;
                        }
                    }
                }
            });

            client_to_server.join().expect("cannot join thread");
            server_to_client.join().expect("cannot join thread");
        }
        Err(e) => {
            eprintln!("connection server failure {}: {}", server_addr, e);
        }
    }
}

pub fn start_server() {
    let listener = TcpListener::bind("127.0.0.1:5000").expect("bind address failure");
    println!("proxy server start on: 5000");

    let server_addr = "127.0.0.1:9000"; // 修改为你想代理的目标服务器地址

    for stream in listener.incoming() {
        match stream {
            Ok(client_stream) => {
                println!("get a new connection");
                let server_addr_clone = server_addr.to_string();
                thread::spawn(move || {
                    handle_client(client_stream, &server_addr_clone);
                });
            }
            Err(e) => {
                eprintln!("connection failure: {}", e);
            }
        }
    }
}
