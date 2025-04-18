
//- 泛型函数
pub fn print_t<T: std::fmt::Display>(arg: T) {
    println!("{}", arg)
}

//- 泛型结构体: 默认T类型为i32
pub struct Point<T = i32> {
    x: T,
    y: T,
}

// 实现泛型结构体
impl<T> Point<T> {
    fn new(x: T, y: T) -> Self {
        Point {x, y}
    }
}

//- 内置泛型枚举: Option<T>, Result<T, E>

//- trait泛型约束
// 参数a, b必须实现PartialOrd trait
pub fn max<'a, T: std::cmp::PartialOrd>(a: &'a T, b: &'a T) -> &'a T {
    if a>b {
        a
    } else {
        b
    }
}

// where关键字进行多个trait约束
pub fn add_or_sub<T>(a: T, b: T) -> T
where
    T: std::ops::Add<Output = T> +
       std::ops::Sub<Output = T>
{
    if a > b {
        a - b
    } else {
        a + b
    }
}

