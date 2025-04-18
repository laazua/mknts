//! 操作符和格式化字符串

// 操作符
/*
一元操作符
顾名思义，一元操作符是专门对一个Rust元素进行操纵的操作符，主要包括以下几个:
    -: 取负，专门用于数值类型
    *: 解引用。这是一个很有用的符号，和Deref（DerefMut）这个trait关联密切
    !: 取反。取反操作相信大家都比较熟悉了，不多说了。有意思的是，当这个操作符对数字类型使用的时候，会将其每一位都置反！也就是说，你对一个1u8进行!的话你将会得到一个254u8
    &和&mut: 租借，borrow。向一个owner租借其使用权，分别是租借一个只读使用权和读写使用权

二元操作符
算数操作符
算数运算符都有对应的trait的，他们都在std::ops下：
    +: 加法。实现了std::ops::Add
    -: 减法。实现了std::ops::Sub
    *: 乘法。实现了std::ops::Mul
    /: 除法。实现了std::ops::Div
    %: 取余。实现了std::ops::Rem

位运算符
和算数运算符差不多的是，位运算也有对应的trait。
    &: 与操作。实现了std::ops::BitAnd
    |: 或操作。实现了std::ops::BitOr
    ^: 异或。实现了std::ops::BitXor
    <<: 左移运算符。实现了std::ops::Shl
    >>: 右移运算符。实现了std::ops::Shr

惰性boolean运算符
逻辑运算符有三个，分别是:
    &&
    ||
    !
    其中前两个叫做惰性boolean运算符，之所以叫这个名字。
    是因为在Rust里也会出现其他类C语言的逻辑短路问题。
    所以取了这么一个高大上然并卵的名字。 
    Rust里这个运算符只能用在bool类型变量上

比较运算符
比较运算符其实也是某些trait的语法糖啦，不同的是比较运算符所实现的trait只有两个:
    std::cmp::PartialEq
    std::cmp::PartialOrd
    ==和!=实现的是PartialEq
    <、>、>=、<=实现的是PartialOrd

类型转换运算符
    as
fn avg(vals: &[f64]) -> f64 {
    let sum: f64 = sum(vals);
    let num: f64 = len(vals) as f64;
    sum / num
}

运算符重载
use std::ops::{Add, Sub};

#[derive(Copy, Clone)]
struct A(i32);

impl Add for A {
    type Output = A;
    fn add(self, rhs: A) -> A {
        A(self.0 + rhs.0)
    }
}

impl Sub for A {
    type Output = A;
    fn sub(self, rhs: A) -> A{
        A(self.0 - rhs.0)
    }
}

fn main() {
    let a1 = A(10i32);
    let a2 = A(5i32);
    let a3 = a1 + a2;
    println!("{}", (a3).0);
    let a4 = a1 - a2;
    println!("{}", (a4).0);
}
*/

// 格式化字符串
/*
Rust采取了一种类似Python里面format的用法，其核心组成是五个宏和两个trait:
    format!
    format_arg!
    print!
    println!
    write!
    Debug
    Display
*/