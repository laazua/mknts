use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::io::Error as IoError;

// 定义一个错误类型
#[derive(Debug)]
pub enum FileOptionError {
    FileOpenError,
    FileReadError(IoError),
    FileWriteError,
}

pub fn read_from_file(filename: &str) -> Result<String, FileOptionError> {
    // 尝试打开文件
    let file = match File::open(filename) {
        Ok(file) => file,
        Err(_) => return Err(FileOptionError::FileOpenError), // 文件打开失败，返回错误
    };

    // 使用 BufReader 包装文件，以便逐行读取
    let reader = BufReader::new(file);

    // 逐行读取文件内容并将其连接成一个字符串
    let mut content = String::new();
    for line in reader.lines() {
        match line {
            Ok(line) => content.push_str(&line),
            Err(err) => return Err(FileOptionError::FileReadError(err)), // 读取行时发生错误，返回错误
        }
    }

    Ok(content)
}

pub fn write_to_file(data: &str) -> Result<(), FileOptionError> {
    let mut file = match File::create("../test.txt") {
        Ok(file) => file,
        Err(_) => return Err(FileOptionError::FileOpenError),
    };

    match file.write_all(data.as_bytes()) {
        Ok(_) => Ok(()),
        Err(_) => Err(FileOptionError::FileWriteError),
    }
}
