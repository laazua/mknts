use std::borrow::Cow;
use std::env;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::process::exit;
use std::thread;

fn handle_client(mut tcp_stream: TcpStream) {
    let mut buffer = [0; 512];

    // 读取客户端发送的数据
    tcp_stream.read(&mut buffer).unwrap();

    // 处理数据
    let request = String::from_utf8_lossy(&buffer);
    println!("Received data: {}", request);

    // 发送响应给目标服务器
    handle_target(request);
}

fn handle_target(request: Cow<'_, str>) {
    // 命令行参数
    let args: Vec<String> = env::args().collect();
    let address = format!("{}:{}", &args[3], &args[4]);
    let mut target_stream = TcpStream::connect(address).expect("target error");
    target_stream.write(request.as_bytes()).unwrap();
}

fn main() {
    // 命令行参数
    let args: Vec<String> = env::args().collect();
    if args.len() != 5 {
        let useage = format!(
            "useage {} <server_ip> <server_port> <target_ip> <target_port>",
            &args[0]
        );
        println!("{}", useage);
        exit(0);
    }
    let address = format!("{}:{}", &args[1], &args[2]);

    // 创建 TCP 监听器，监听在 address
    let listener = TcpListener::bind(address.clone()).unwrap();
    println!("Server Listen On: [{}]", address);

    // 处理传入的连接请求
    for tcp_stream in listener.incoming() {
        match tcp_stream {
            Ok(tcp_stream) => {
                // 创建新线程处理连接
                thread::spawn(|| {
                    handle_client(tcp_stream);
                });
            }
            Err(e) => {
                println!("Error: {}", e);
            }
        }
    }
}
