// 函数&&方法

fn main() {
    let c = add_one(1, 2);
    println!("c = {}", c);
    let d = add_tow(3, 4);
    println!("d = {}", d);

    // 结构体方法
    let mut student: Student = Student::new("zhangsan", 20);
    println!("name: {}", student.get_name());
    student.set_name("wangwu");
    println!("name: {}", student.get_name());
 
    // 高阶函数
    let ph: fn() = print_hello;
    println!("高阶函数: {:p}", ph);
    ph();
    let add_res = match_add(add, 1, 2);
    println!("{}", add_res);
    let ret_add = add_ret("add");
    println!("ret_add {}", ret_add(1, 2))
}

fn add_one(a: u8, b: u8) -> u8 {
    return a + b;
}

fn add_tow(a: u8, b: u8) -> u8 {
    a + b
}


#[derive(Debug, PartialEq)]
struct Student {
    name: &'static str,
    age: u8,
}

// 对象方法
impl Student {
    // 创建实例对象
    pub fn new(name: &'static str, age: u8) -> Self {
        Student{ name, age }
    }
    // 获取实例名字
    pub fn get_name(&self) -> &str {
        self.name
    }
    // 更改实例名字
    pub fn set_name(&mut self, name: &'static str) {
        self.name = name;
    }
}

// 高级函数:以函数为参数或者返回函数
fn print_hello() {
    println!("hello");
}

// 函数定义
type Add = fn(u8, u8) -> u8;
// 函数作为参数
fn match_add(add: Add, a: u8, b: u8) -> u8 {
    add(a, b)
}
// 函数原型
fn add(a: u8, b: u8) -> u8 {
    a + b
}
// 函数作为返回值
fn add_ret(op: &str) -> Add {
    match op {
        "add" => add,
        _ => add_one,
    }
}
