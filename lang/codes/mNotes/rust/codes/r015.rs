// 所有权
/// rust通过所有权管理内存,编译时会根据一系列规则进行检查
/// 如果违反了任何这些规则,程序都不能编译通过

/// Rust 中的每一个值都有一个被称为其 所有者(owner)的变量.
/// 值在任一时刻有且只有一个所有者
/// 当所有者(变量)离开作用域,这个值将被丢弃.

/// 内存在拥有它的变量离开作用域后就被自动释放(在作用域结束}就调用drop函数)

// 引用
/// 在任意给定时间，要么 只能有一个可变引用，要么 只能有多个不可变引用。
/// 引用必须总是有效的

fn main() {
    // 分配在栈上的不可变变量
    let name = "zhangsan";
    // name字面值,不可变,这里会报错
    // name.push_str(" lisi");
    println!("name = {}", name);
    
    
    // 分配在堆上的可变变量
    let mut address = String::from("chengdu");
    address.push_str(" beijing");
    println!("address = {}", address);

    // 这里的x, y都有各自的副本值(即在内存中x,y指向的时不同的内存地址)
    let x = 10;
    let y = x;
    println!("x = {}, y = {}", x, y);

    // 这里的s1, s2在内存上指向同一个地址(所以当s2指向s1所在地址的值时,s1就不再有效)
    // 在rust中这里称之为s1被移动到了s2上
    // let s1 = String::from("hello");
    // let s2 = s1;
    // println!("s1 = {}, s2 = {}", s1, s2); // 这里编译不通过s1无效

    // 栈上可认为默认调用了clone()函数进行拷贝,所以在栈内存上会有两个副本值
    // 在堆上需要手动调用clone(),在堆内存上才会出现两个副本值
    let s3 = String::from("world");
    let s4 = s3.clone();
    println!("s3 = {}, s4 = {}", s3, s4);

    // 函数的参数在栈上
    let num = 18;
    print_age(18);
    println!("num = {}", num);

    // 函数的参数在堆上
    let s = String::from("s");
    print_name(s);
    // println!("s = {}", s); // 变量s在进入print_name函数时,在此就不在有效,这里编译会报错

    // 函数参数在堆上: 传不可变引用
    let ss = String::from("ss");
    print_addr(&ss);
    println!("ss = {}", ss);

    // 函数参数在堆上: 传可变引用
    let mut sex = String::from("男");
    print_sex(&mut sex);
    println!("sex = {}", sex);
}

// 函数参数在栈上的例子
fn print_age(num: u32) {
    println!("fn num = {}", num);
}

// 函数参数在堆上的例子
fn print_name(s: String) {
    println!("fn s = {}", s);
}

// 函数参数在堆上:传不可变引用类型
fn print_addr(s: &String) {
    // 这里的引用可以使用s指向的值,但不获取其所有权(指向ss变量,但不获取ss的所有权)
    // 所以在此函数作用域结束后ss任然有效,因为其所有权没有被移交到形参变量s上
    // 只能使用形参s只能使用实参ss变量所指向的值,不能修改ss变量的值
    println!("fn s = {}", s);
}

// 函数参数在堆上:传可变引用类型
fn print_sex(sex: &mut String) {
    // 所有权还是在实参上,形参没有获取其所有权,但这里可以改变实参的值
    println!("fn sex = {}", sex);
    sex.push_str(" 女")
}
