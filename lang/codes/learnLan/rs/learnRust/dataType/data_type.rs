//! rust数据类型


// 基础类型(原生类型)
// bool
let is_done = true;

// char(字符型),表示一个unicode字符
let c = 'c';

// 数值类型
// i8, i16, i32, i64, isize
// u8, u16, u32, u64, usize
// f32, f64

// 数组表示为: [T;N]
let arr_o = [1, 2, 3];
let arr_t: [u8;3] = [3, 4, 5];

// slice: &[T], &mut [T], 对数组的切片,slice是动态的,范围不能超过数组的大小
let arra = [1, 2, 3, 4, 5, 6];
let slice_o = &arra[..];  //获取全部元素
let slice_t = &arra[2..4];  // 左闭右开原则, [3, 4]
let slice_e = &arra[2..];
let slice_f = &arra[..5];

// Vec动态数组
// 在Rust里,Vec被表示为 Vec<T>,其中T是一个泛型
let mut v1: Vec<i32> = vec![1, 2, 3]; // 通过vec!宏来声明
let v2 = vec![0; 10]; // 声明一个初始长度为10的值全为0的动态数组
println!("{}", v1[0]); // 通过下标来访问数组元素

for i in &v1 {
    print!("{}", i); // &Vec<i32> 可以通过 Deref 转换成 &[i32]
}

println!("");

for i in &mut v1 {
    *i = *i+1;
    print!("{}", i); // 可变访问
}

// 原生字符串类型: str, 双引号""包裹的内容都可以称为&str

// 函数类型
fn foo(x: i32) -> i32 { x+1 }

let x: fn(i32) -> i32 = foo;

assert_eq!(11, x(10));


// 复合类型
// 元组: tuple
let y = (2, "hello world");
let x: (i32, &str) = (3, "world hello");

// 然后呢，你能用很简单的方式去访问他们：

// 用 let 表达式
let (w, z) = y; // w=2, z="hello world"

// 用下标
let f = x.0; // f = 3
let e = x.1; // e = "world hello"

// 结构体
//具名结构体
struct A {
    attr1: i32,
    atrr2: String,
}

//元组类型结构体
struct B(i32, u16, bool);

//空结构体
struct D;

// 实现结构体(impl)
// Rust没有继承，它和Golang不约而同的选择了trait(Golang叫Interface)作为其实现多态的基础
/*
struct Person {
    name: String,
}

impl Person {
    fn new(n: &str) -> Person {
        Person {
            name: n.to_string(),
        }
    }

    fn greeting(&self) {
        println!("{} say hello .", self.name);
    }
}

fn main() {
    let peter = Person::new("Peter");
    peter.greeting();
}
上面的impl中，new 被 Person 这个结构体自身所调用，其特征是 :: 的调用

#[derive(Copy, Clone)]
struct A {
    a: i32,
}
impl A {
    pub fn show(&self) {
        println!("{}", self.a);
        // compile error: cannot borrow immutable borrowed content `*self` as mutable
        // self.add_one();
    }
    pub fn add_two(&mut self) {
        self.add_one();
        self.add_one();
        self.show();
    }
    pub fn add_one(&mut self) {
        self.a += 1;
    }
}

fn main() {
    let mut ast = A{a: 12i32};
    ast.show();
    ast.add_two();
}
*/

// 枚举类型: enum
enum Direction {
    West,
    North,
    South,
    East,
}

enum SpecialPoint {
    Point(i32, i32),
    Special(String),
}

enum SpecialPoint {
    Point {
        x: i32,
        y: i32,
    },
    Special(String),
}

// 枚举使用
/*
enum SpecialPoint {
    Point(i32, i32),
    Special(String),
}

fn main() {
    let sp = SpecialPoint::Point(0, 0);
    match sp {
        SpecialPoint::Point(x, y) => {
            println!("I'am SpecialPoint(x={}, y={})", x, y);
        }
        SpecialPoint::Special(why) => {
            println!("I'am Special because I am {}", why);
        }
    }
}
*/

// 字符串类: String
