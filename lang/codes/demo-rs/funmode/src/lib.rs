#[derive(Debug)]
struct ServerConfig {
    address: String,
    port: u16,
    threads: usize,
}

impl ServerConfig {
    // 提供一个默认的构造函数
    fn new() -> Self {
        ServerConfig {
            address: String::from("127.0.0.1"),
            port: 8080,
            threads: 4,
        }
    }

    // 设置地址
    fn address(mut self, address: &str) -> Self {
        self.address = address.to_string();
        self
    }

    // 设置端口
    fn port(mut self, port: u16) -> Self {
        self.port = port;
        self
    }

    // 设置线程数
    fn threads(mut self, threads: usize) -> Self {
        self.threads = threads;
        self
    }
}

// fn main() {
//     // 使用默认值创建配置
//     let config1 = ServerConfig::new();
//     println!("{:?}", config1);

//     // 通过链式调用设置部分配置项
//     let config2 = ServerConfig::new().address("192.168.1.1").port(8081);
//     println!("{:?}", config2);

//     // 通过链式调用设置所有配置项
//     let config3 = ServerConfig::new()
//         .address("10.0.0.1")
//         .port(9090)
//         .threads(8);
//     println!("{:?}", config3);
// }
