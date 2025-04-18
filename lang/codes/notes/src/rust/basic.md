# 基础
---
* **变量**    
在rust中使用let关键字声明一个变量:   
let age: u8 = 18;    
变量默认不可变,要声明可变变量使用mut关键字:    
let mut age: u8 = 20;    
在同一个作用域内同时声明两个同名变量,后一个会遮蔽前面的变量:    
let number: u8 = 100;    
let number: u8 = 200;    


* **常量**    
1. 在rust中常量一旦声明就不可更改    
2. 常量声明使用const关键字且不能与mut一起使用,声明时必须标明类型:    
  const max_seconds: u8 = 60 * 60;  


* **基础数据类型**    
1. 有符号整型: i8, i16, i32, i64, i128, isize    
2. 无符号整型: u8, u16, u32, u64, u128, usize    
3. 浮点数类型: f32, f64
4. 布尔类型: bool (true, false)    
5. 字符类型: char


* **原始复合类型**    
复合类型是包含多个类型的一个分组,rust自带两个原始复合类型:
1. 元组: (u8, i8)    
2. 没有任何元素的元组, 叫做unit类型
3. 数组: [type, size] => [u8, 5]    


* **函数签名**    
fn func_name(param_name: type) -> type {}    
其中参数和返回值都可以有多个    
函数体内由多个语句或表达式组成    
以分号结尾的是语句: let x: i8 = 9;    
没有分号结尾的是表达式: x + y    
表达式有返回值    


* **流程控制**    
1. if, else if, else    // let number = if condition { 5 } else { "six" };    
2. loop    // let result = loop {};    
3. while    
4. for .. in ..    
5. math    