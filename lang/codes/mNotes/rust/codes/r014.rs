// 变量的可变性

fn main() {
    // 声明不可变变量并绑定一个值
    let num = 15;
    // 重新绑定一个值(编译报错)
    // num = 20;
    println!("num = {}", num);

    // 声明一个可变变量并绑定一个值
    let mut name = "zhangsan";
    println!("name = {}", name);
    // 重新绑定一个值
    name = "lisi";
    println!("name = {}", name);
}
