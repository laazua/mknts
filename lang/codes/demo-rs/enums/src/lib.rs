// - 枚举
// Option<T> 表示可能有值,也可能没值
// enum Option<T> {
//     Some(T),
//     None,
// }

// Result<T, E> 表示一个操作可能成功也可能失败的类型
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

// Option示例
pub fn a(option: Option(i32)) {
    match option {
        Some(value) => println!("有值: {}", value),
        None => println!("没有值"),
    }
}

// let some_value = Some(10);
// println!("The value is: {}", some_value.unwrap()); // 输出: The value is: 10
// let no_value: Option<i32> = None;
// println!("The value is: {}", no_value.unwrap()); // 这行代码会导致程序崩溃

// let some_value = Some(10);
// let no_value: Option<i32> = None;
// println!("The value is: {}", some_value.unwrap_or(0)); // 输出: The value is: 10
// println!("The value is: {}", no_value.unwrap_or(0));   // 输出: The value is: 0

// let some_value = Some(10);
// let no_value: Option<i32> = None;
// println!("The value is: {}", some_value.unwrap_or_else(|| 0)); // 输出: The value is: 10
// println!("The value is: {}", no_value.unwrap_or_else(|| 0));   // 输出: The value is: 0

// let some_value = Some(10);
// let no_value: Option<i32> = None;
// println!("some_value is_some: {}", some_value.is_some()); // 输出: true
// println!("no_value is_some: {}", no_value.is_some());     // 输出: false
// println!("some_value is_none: {}", some_value.is_none()); // 输出: false
// println!("no_value is_none: {}", no_value.is_none());     // 输出: true

// let some_value = Some(10);
// let no_value: Option<i32> = None;
// let new_value = some_value.map(|x| x + 1);
// let no_new_value = no_value.map(|x| x + 1);
// println!("{:?}", new_value); // 输出: Some(11)
// println!("{:?}", no_new_value); // 输出: None

// let some_value = Some(10);
// let no_value: Option<i32> = None;
// let new_value = some_value.and_then(|x| Some(x + 1));
// let no_new_value = no_value.and_then(|x| Some(x + 1));
// println!("{:?}", new_value); // 输出: Some(11)
// println!("{:?}", no_new_value); // 输出: None
