use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::thread;
use std::sync::{Arc, Mutex};
use std::collections::HashMap;

type SharedData = Arc<Mutex<HashMap<usize, TcpStream>>>;

fn handle_client(id: usize, mut stream: TcpStream, shared_data: SharedData) {
    let mut buffer = [0; 1024];
    let mut name = String::new();

    let _ = stream.write(b"please input your nick name: ");
    match stream.read(&mut buffer) {
        Ok(size) if size > 0 => {
            name = String::from_utf8_lossy(&buffer[..size]).trim().to_string();
        }
        _ => {}
    }

    let _ = stream.write(format!("welcome {} join this chat!\n", name).as_bytes());

    let mut data = shared_data.lock().unwrap();
    data.insert(id, stream.try_clone().expect("clone stream failure"));

    loop {
        match stream.read(&mut buffer) {
            Ok(size) if size > 0 => {
                let msg = String::from_utf8_lossy(&buffer[..size]);
                let msg_to_send = format!("{}: {}", name, msg);

                for (&client_id, mut client_stream) in data.iter() {
                    if id != client_id {
                        let _ = client_stream.write(msg_to_send.as_bytes());
                    }
                }
            }
            _ => {
                let _ = data.remove(&id);
                break;
            }
        }
    }
}

pub fn start_server() {
    let listener = TcpListener::bind("127.0.0.1:5000").expect("bind address failure");

    let shared_data: SharedData = Arc::new(Mutex::new(HashMap::new()));
    let mut client_id_counter = 0;

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("get a new connector");
                let shared_data_clone = shared_data.clone();
                let id = client_id_counter;
                client_id_counter += 1;
                thread::spawn(move || {
                    handle_client(id, stream, shared_data_clone);
                });
            }
            Err(e) => {
                eprintln!("connect failure: {}", e);
            }
        }
    }
}
