use std::fmt::Debug;
use std::ops::{Add, Mul, Sub, Div};

pub enum Arithmetic {
    Add,
    Sub,
    Mul,
    Div,
}

pub fn arithmetic<T>(num: T, ops: Arithmetic) -> T
where
    T: Copy + 
       Debug + 
       Add<Output=T> + 
       Mul<Output=T> + 
       Sub<Output=T> + 
       Div<Output=T> ,
{
    let add = |item: T| -> T { num + item };
    let sub = |item: T| -> T { num - item };
    let mul = |item: T| -> T { num * item };
    let div = |item: T| -> T { num / item };

    let option = |x: u32, y: u32| -> u32 { x + y };
    println!("Option: {:?}", option(3u32, 5u32));

    match ops {
        Arithmetic::Add => return add(num),
        Arithmetic::Sub => return sub(num),
        Arithmetic::Mul => return mul(num),
        Arithmetic::Div => return div(num),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_arithmetic() {
       assert_eq!(arithmetic(5u32, Arithmetic::Add), 10);
       assert_eq!(arithmetic(5u32, Arithmetic::Sub), 0);
       assert_eq!(arithmetic(5u32, Arithmetic::Mul), 25);
       assert_eq!(arithmetic(5u32, Arithmetic::Div), 1);
    }
}
