/// 原始类型

fn main() {
    // 布尔类型: true, false
    let is_done = true;
    println!("isDone = {}", is_done);

    // 字符型, 在rust中,一个char类型占32位
    let cha:  char = '我';
    println!("cha = {}", cha);

    // 数字类型: integers, unsigned integers, float等
    // i8, i16, i32, i64, 128, u8, u16, u32, u64, u128, f32, f64
    // isize, usize

    // i8是类型注解
    let height = 72i8;
    println!("height = {}", height);

    // 显式给出类型,类型注解省略
    let size: i8 = 12;
    println!("size = {}", size);

    // 自适应类型: isize, usize
    println!("usize_max = {}", usize::max_value());

    // 数组 [type; size]
    let arra: [u32; 3] = [1, 2, 3];
    println!("arra = {}", arra[0]);
    show_arra(arra);

    // 元组 (type1, type2, ...)
    let tup: (i8, u8, f32) = (5, 4, 2.0);
    println!("{}", tup.0);
    println!("{}", tup.1);
    println!("{}", tup.2);
}

fn show_arra(arra: [u32; 3]) {
    for v in &arra {
        println!("{}", v);
    }
}

