# 知识点

1. Option 枚举
   用于处理可能为空的情况，以避免使用空指针或其他类似的错误

   ```
   fn find_element_index(arr: &[i32], target: i32) -> Option<usize> {
       for (index, &value) in arr.iter().enumerate() {
           if value == target {
               return Some(index); // 找到目标值，返回Some包装的索引
           }
       }
       None // 没有找到目标值，返回None
   }

   fn main() {
       let numbers = vec![10, 20, 30, 40, 50];
       let target = 30;
       match find_element_index(&numbers, target) {
           Some(index) => println!("Found {} at index {}", target, index),
           None => println!("{} not found", target),
       }

       let target = 60;
       match find_element_index(&numbers, target) {
           Some(index) => println!("Found {} at index {}", target, index),
           None => println!("{} not found", target),
       }
   }

   ```

2. Result 枚举
   用于处理潜在的错误情况，以避免使用异常或其他类似的错误处理机制

```
fn divide(x: i32, y: i32) -> Result<i32, String> {
    if y == 0 {
        Err("Cannot divide by zero".to_string()) // 返回包含错误消息的Err
    } else {
        Ok(x / y) // 返回包含商的Ok
    }
}

fn main() {
    let dividend = 10;
    let divisor = 2;

    match divide(dividend, divisor) {
        Ok(result) => println!("Result: {}", result),
        Err(err) => println!("Error: {}", err),
    }

    let dividend = 5;
    let divisor = 0;

    match divide(dividend, divisor) {
        Ok(result) => println!("Result: {}", result),
        Err(err) => println!("Error: {}", err),
    }
}
```

3. 多线程

```
use std::thread;

fn main() {
    let t1 = thread::spawn(|| func("xxx"));
    let t2 = thread::spawn(|| func("yyy"));
    println!("main thread!");
    t1.join().unwrap();
    t2.join().unwrap();
}

fn func(name: &str) {
    let id = thread::current().id();
    println!("child thread: {name:?}, current id: {id:?}");
}
```
