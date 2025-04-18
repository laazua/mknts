//! 函数
//! 尽管rust是一门多范式的编程语言，但rust的编程风格是更偏向于函数式的，
//! 函数在rust中是“一等公民”——first-class type。
//! 这意味着，函数是可以作为数据在程序中进行传递，
//! 如：作为函数的参数。跟C、C++一样，rust程序也有一个唯一的程序入口-main函数。
//! rust的main函数形式如下：
//! fn main() {
//!     statements
//! }
//! rust使用snake_case风格来命名函数
//! 如果函数有返回值，则在括号后面加上箭头 -> ，在箭头后加上返回值的类型。
//! fn foo_bar(args: type) -> type{
//!     statements
//! }

/*
将函数作为参数:
fn main() {
  let xm = "xiaoming";
  let xh = "xiaohong";
  say_what(xm, hi);
  say_what(xh, hello);
}

fn hi(name: &str) {
  println!("Hi, {}.", name);
}

fn hello(name: &str) {
  println!("Hello, {}.", name);
}

fn say_what(name: &str, func: fn(&str)) {
  func(name)
}

模式匹配:
fn main() {
  let xm = ("xiaoming", 54);
  let xh = ("xiaohong", 66);
  print_id(xm);
  print_id(xh);
  print_name(xm);
  print_age(xh);
  print_name(xm);
  print_age(xh);
}

fn print_id((name, age): (&str, i32)) {
  println!("I'm {},age {}.", name, age);
}

fn print_age((_, age): (&str, i32)) {
  println!("My age is  {}", age);
}

fn print_name((name,_): (&str, i32)) {
  println!("I am  {}", name);
}

返回值: () == void
fn main() {
    let a = 3;
    println!("{}", inc(a));
}

fn inc(n: i32) -> i32 {
    n + 1
}
return关键字: 提前返回
fn main() {
  let a = [1,3,2,5,9,8];
  println!("There is 7 in the array: {}", find(7, &a));
  println!("There is 8 in the array: {}", find(8, &a));
}

fn find(n: i32, a: &[i32]) -> bool {
  for i in a {
    if *i == n {
      return true;
    }
  }
  false
}
返回多个值:
fn main() {
  let (p2,p3) = pow_2_3(789);
  println!("pow 2 of 789 is {}.", p2);
  println!("pow 3 of 789 is {}.", p3);
}

fn pow_2_3(n: i32) -> (i32, i32) {
  (n*n, n*n*n)
}

发散函数: !作为返回类型
fn main() {
  println!("hello");
  diverging();
  println!("world");
}

fn diverging() -> ! {
  panic!("This function will never return");
}

语句和表达式:
    rust是一个基于表达式的语言，不过它也有语句。
    rust只有两种语句：声明语句和表达式语句，其他的都是表达式。
    基于表达式是函数式语言的一个重要特征，表达式总是返回值

高阶函数:
    使用一个或多个函数作为参数，可以将函数作为返回值
fn inc(n: i32) -> i32 {//函数定义
  n + 1
}

type IncType = fn(i32) -> i32;//函数类型

fn main() {
  let func: IncType = inc;
  println!("3 + 1 = {}", func(3));
}
函数作为参数
fn main() {
  println!("3 + 1 = {}", process(3, inc));
  println!("3 - 1 = {}", process(3, dec));
}

fn inc(n: i32) -> i32 {
  n + 1
}

fn dec(n: i32) -> i32 {
  n - 1
}

fn process(n: i32, func: fn(i32) -> i32) -> i32 {
  func(n)
}
函数作为返回值:
fn main() {
   let a = [1,2,3,4,5,6,7];
   let mut b = Vec::<i32>::new();
   for i in &a {
       b.push(get_func(*i)(*i));
   }
   println!("{:?}", b);
}

fn get_func(n: i32) -> fn(i32) -> i32 {
    fn inc(n: i32) -> i32 {
        n + 1
    }
    fn dec(n: i32) -> i32 {
        n - 1
    }
    if n % 2 == 0 {
        inc
    } else {
        dec
    }
}
*/