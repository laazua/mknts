// 字符串
//    固定长度: str
//    可变长度: String


fn main() {
    // 固定长度
    let s1 = "hello world!";
    println!("固定长度s1: {}", s1);
    // 使用as_str()方法将字符串对象转换为字符串字面量
    let s2 = String::from("hello world!");
    let s3 = s2.as_str();
    println!("字符串字面量s3: {}", s3);
   
    // 可变长度String: 本质Vec<u8>
    let mut _s4 = String::new();
    // 根据指定的字符串字面量创建字符串对象
    let _s4 = String::from("hello rust!");
    // to_string()将字符串字面值转换为字符对象
    let s5 = _s4.to_string();
    println!("字符串对象_s4: {}", _s4);
    println!("字符串对象s5: {}", s5);
 
    // String字符串修改   
    let mut s6 = String::from("hello, ");
    s6.push('W');
    s6.push_str("orld");
    println!("s6: {}", s6);
    s6.insert(5, ' ');
    s6.insert_str(7, "Rust");
    println!("s6: {}", s6);
    let s7 = " haha";
    let mut s8 = s6 + s7 + &s2 + _s4.as_str();
    println!("s8: {}", s8);
    s8 += "!!!!";
    println!("{}", s8);
    let s9 = format!("{}-{}", s2, _s4);
    println!("{}", s9);
    let mut s9 = s9.replace("rust", "RUST");
    println!("len: {}", s9.len());
    println!("{}", s9);
    s9.pop();
    s9.truncate(8);
    s9.clear();
    println!("{}", s9);

    //let b =  s1.bytes();
    //for v in b {
    //    print!("{} | ", v);
    //}
    //let c = s6.chars();
    //for v in c {
    //    print!("{} | ", c);
    //}
}
