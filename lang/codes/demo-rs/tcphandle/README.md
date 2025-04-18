### TCP粘包处理

*) 消息边界  
*) 在消息中使用特殊字符或字节序列作为分隔符，比如换行符 \n 或者特定的结束符号  
*) 接收端根据分隔符来拆分消息，每次读取一行或者一段完整的数据  
[server]  
```
use std::io::{Read, BufReader};

fn handle_connection(stream: TcpStream) {
    let mut reader = BufReader::new(stream);
    loop {
        let mut buffer = String::new();
        match reader.read_line(&mut buffer) {
            Ok(0) => break, // EOF
            Ok(_) => {
                // 处理消息
                println!("Received: {}", buffer);
            },
            Err(e) => {
                eprintln!("Error reading from socket: {}", e);
                break;
            }
        }
    }
}
```

[client]  
```
use std::io::{Write};
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:8080").expect("Could not connect to server");
    let message = "Hello\n";
    stream.write_all(message.as_bytes()).expect("Failed to send message");
}
```

*) 固定长度消息  
*) 在消息中预先定义消息的长度，然后在接收端读取指定长度的字节  
*) 可以使用 std::io::Read::read_exact() 方法来确保读取到足够长度的数据  
[server]  
```
use std::io::{Read, BufReader};

const MSG_SIZE: usize = 8;

fn handle_connection(stream: TcpStream) {
    let mut reader = BufReader::new(stream);
    loop {
        let mut buffer = [0; MSG_SIZE];
        match reader.read_exact(&mut buffer) {
            Ok(_) => {
                // 处理消息
                println!("Received: {:?}", buffer);
            },
            Err(e) => {
                eprintln!("Error reading from socket: {}", e);
                break;
            }
        }
    }
}
```

[client]  
```
use std::io::{Write};
use std::net::TcpStream;

const MSG_SIZE: usize = 8;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:8080").expect("Could not connect to server");
    let message = "Hello!!!";
    let mut buffer = [0; MSG_SIZE];
    buffer[..message.len()].copy_from_slice(message.as_bytes());
    stream.write_all(&buffer).expect("Failed to send message");
}
```

*) 长度前缀法  
*) 在消息开头加上一个表示消息长度的前缀，通常使用固定长度的整数来表示消息的长度  
*) 接收端先读取前缀以确定消息长度，然后再读取相应长度的消息内容  
[server]
```
use std::io::{Read, BufReader, Error};

const PREFIX_SIZE: usize = 4;

fn handle_connection(stream: TcpStream) -> Result<(), Error> {
    let mut reader = BufReader::new(stream);
    loop {
        let mut prefix_buffer = [0; PREFIX_SIZE];
        reader.read_exact(&mut prefix_buffer)?;

        let msg_size = u32::from_be_bytes(prefix_buffer) as usize;

        let mut message = vec![0; msg_size];
        reader.read_exact(&mut message)?;

        // 处理消息
        println!("Received: {:?}", message);
    }
}
```

[client]  
```
use std::io::{Write};
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("127.0.0.1:8080").expect("Could not connect to server");
    let message = "Hello!!!";
    let msg_size = message.len() as u32;
    let mut buffer = [0; 4];
    buffer.copy_from_slice(&msg_size.to_be_bytes());
    stream.write_all(&buffer).expect("Failed to send message size");
    stream.write_all(message.as_bytes()).expect("Failed to send message");
}
```
