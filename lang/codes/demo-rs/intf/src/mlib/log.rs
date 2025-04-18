/// Rust依赖注入
use std::fs::OpenOptions;
use std::io::Write;

pub trait Logger {
    fn log(&self, msg: &str);
}

pub struct FileLog {
    pub path: String
}

impl Logger for FileLog {
    fn log(&self, msg: &str) {
        // 这里只是示例，实际代码应处理文件操作错误
        let mut file = OpenOptions::new()
            .append(true)
            .create(true)
            .open(&self.path)
            .unwrap();
        writeln!(file, "FileLogger: {}", msg).unwrap();
    }
}

pub struct ConsoleLog;

impl Logger for ConsoleLog {
    fn log(&self, msg: &str) {
        println!("ConsoleLogger: {}", msg);
    }
}

pub struct App {
    logger: Box<dyn Logger>
}

impl App {
    pub fn new(logger: Box<dyn Logger>) -> App {
        App { logger }
    }

    pub fn run(&self) {
        self.logger.log("App is running ... ")
    }
}