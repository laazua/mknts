// 所有权
// 堆和栈: rust中,数据大小固定且已知,则分配在栈上;否则分配在堆上
// 作用域
// String内存回收
// 移动
// clone
// 栈上数据拷贝与堆上数据拷贝的特征
// 函数和作用域

fn main() {
    // 作用域: 离开作用域后,作用域上的数据会被回收
    let x: u8 = 100;
    {
        let y: u8 = 200;
        println!("x = {}", x);
        println!("y = {}", y);
    }
    // 报错, y的作用域只在14-17行内
    // println!("y = {}", y);

    {
        // String类型在离开作用域时,调用drop()方法释放内存
        let mut s = String:: from("hello");
        s.push_str(" world");
        println!("{}", s);

        // s的所有权move到t, s无效
        let t = s;
        // println!("s = {}", s);
        println!("t = {}", t);

        // clone(), 类似深拷贝
        let u = t.clone();
        println!("t = {}", t);
        println!("u = {}", u);
    }

    {
        // copy trait: 数值型,布尔型,字符型,元组
        // 实现了copy trait的类型进行拷贝后原来的变量仍然可用
        let a: u8 = 100;
        let b = a;
        println!("a = {}", a);
        println!("b = {}", b);
    }

    // 堆上的数据所有权移交情况
    let s = String::from("hello world");
    // s所有权移交到show函数内
    show_heap_data(s);
    // println!(s);

    // 栈上数据所有权移交情况
    let x: u8 = 250;
    show_stack_data(x);
    println!("x = {}", x);
}

fn show_heap_data(s: String) {
    // 在该函数作用域内s有效
    println!("s = {}", s)
}

fn show_stack_data(x: u8) {
    println!("x = {}", x);
}

