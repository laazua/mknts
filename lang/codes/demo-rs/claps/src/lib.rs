use clap::{App, Arg};

pub fn greet(name: &str) {
    println!("Hello, {}!", name);
}

pub fn parse_args() {
    let matches = App::new("clap_lib_example")
        .version("1.0")
        .author("confucuis")
        .about("一个示例库, 使用clap处理命令行参数")
        .arg(
            Arg::new("name")
                .short('n')
                .long("name")
                .value_name("NAME")
                .takes_value(true),
        )
        .get_matches();

    if let Some(name) = matches.value_of("name") {
        greet(name);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        assert_eq!(greet("Alice"), ());
    }

    #[test]
    fn test_parse_args_with_name() {
        parse_args();
    }

    #[test]
    fn test_parse_args_without_name() {
        parse_args();
    }
}
