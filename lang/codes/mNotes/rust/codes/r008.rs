// 符合数据类型

fn main() {
    // 元组
    let tup: (i8, u8, f32) = (-10, 10, 10.0);
    println!("{:?}", tup);
    println!("tup[0]: {}, tup[1]: {}, tup[2]: {}", tup.0, tup.1, tup.2);
    // 元组解构
    let (x, y, z) = tup;
    println!("x: {}, y: {}, z: {}", x, y, z);

    // 数组
    let arra: [u8; 3] = [1, 2, 4];
    println!("{:?}", arra);

    // 结构体
    let mut student = Student {
        name: "张三",
        height: 17.2,
    };
    println!("name: {}, height: {}", student.name, student.height);

    // 元组结构体
    struct Color(i32, i32, i32);
    let black = Color(0, 0, 0);
    println!("{}", black.0);

    // 单元结构体
    // struct Solution;

    // 枚举
     let color = ColorE::Red;
     match color {
        ColorE::Red => println!("{:?}", ColorE::Red),
        ColorE::Yellow => println!("{:?}", ColorE::Yellow),
        ColorE::Blue => println!("{:?}", ColorE::Blue),
     }
   
}

struct Student {
    name: &'static str,
    height: f32,
}

#[derive(Debug)]
enum ColorE { 
    Red,
    Yellow,
    Blue,
}
