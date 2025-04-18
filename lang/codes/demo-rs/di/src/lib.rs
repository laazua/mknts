trait Logger {
    fn log(&self, msg: &str);
}

struct ConsoleLog;

impl Logger for ConsoleLog {
    fn log(&self, msg: &str) {
        println!("console log: {}", msg);
    }
}

struct FileLog {
    file_path: String,
}

impl Logger for FileLog {
    fn log(&self, msg: &str) {
        println!("file log: {} {}", self.file_path, msg);
    }
}

// 一个应用程序组件，需要注入一个 Logger
struct Application<T: Logger> {
    logger: T,
}

impl<T: Logger> Application<T> {
    fn new(logger: T) -> Self {
        Application { logger }
    }

    fn run(&self) {
        self.logger.log("Application is running");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        // 使用控制台日志记录器
        let console_logger = ConsoleLog;
        let app_with_console_logger = Application::new(console_logger);
        app_with_console_logger.run();

        // 使用文件日志记录器
        let file_logger = FileLog {
            file_path: String::from("/path/to/log.txt"),
        };
        let app_with_file_logger = Application::new(file_logger);
        app_with_file_logger.run();
    }
}
