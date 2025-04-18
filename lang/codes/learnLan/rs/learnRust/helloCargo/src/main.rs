/// cargo
fn main() {
    println!("Hello, cargo!");

    let a = true;
    let b = if a {
        2
    } else {
        3
    };
    println!("{}", b);
}

