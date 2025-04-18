#[cfg(test)]
mod tests {
    use errhandle;

    #[test]
    fn test_read_file() {
        match errhandle::read_from_file("../Cargo.toml") {
            Ok(content) => println!("{}", content),
            Err(err) => println!("{:?}", err),
        }
    }

    #[test]
    fn test_wirte_file() {
        match errhandle::write_to_file("hello rust\n") {
            Ok(_) => println!("Write to file successful!"),
            Err(err) => println!("{:?}", err),
        }
    }
}
