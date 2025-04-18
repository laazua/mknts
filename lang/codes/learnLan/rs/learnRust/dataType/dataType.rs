fn main() {
    // rust数据类型
}

// 函数
// fn funcName(arg1: type1, arg2: type2, arg3: type3) -> type {
//     // code statment
// }

fn numType() {
    // 整数型(i8, i16, i32, i64, isize, u8, u16, u32, u64, usize)
    let intNum: i8 = 100;    // let intNum = 100;
    // 浮点型(f32, f64)
    let floatNum: f32 = 3.14;
}

fn boolType() {
    // 布尔型(true, false)
    let isDone: bool = true;
}

fn charType() {
    // 字符型(单引号引起的单个字符)
    let cc: char = 'a';
}

fn stringType() {
    // 字符串字面量类型(s1与s2的声明并赋值等价,在栈上分配内存)
    let s1 = "hello world."
    let s2: &str = "hello world."

    // String类型的字符串(在堆上分配内存)
    let s3 = String::from("hello world.")
}

fn tupleType() {
    // tuple类型
    let tup: (i8, f32) = (200, 5.20);
    let (a, b) = tup;    // 解构
    // tup.0 == a    true
    // tup.1 == b    true

    // unit类型(空tuple)
    let u: () = ();
}

fn arrayType() {
    // 数组类型[T; N], 数组的引用类型&[T; N]
    let array1 = [1, 2, 3];    // 每个元素类型必须一致
    // array[0] == 1; array[1] == 2; array[2] == 3;
    let array2 = [&str; 3] = ["aa", "bb", "cc"];
}

fn referenceType() {
    // 引用类型
    let n: &i32 = &33_i32

    let mut m = 200;
    let m_ref = &mut m;
    m = *m_ref + 200;
}

fn sliceType() {
    // Slice类型[T], Slice的引用类型&[T] 
    // rust编译器不允许在编译期间使用大小不固定的数据类型,因此rust
    // 几乎总是使用切片数据的引用 &[T]或者&mut [T]
    // String类型,Array类型,Vec类型,Slice类型支持切片操作
    // s[n..m]
    // s[n..]
    // s[..m]
    // s[..]
    // s[n..=m]
}

fn structType() {
    // 结构体
    struct User {
        name: String,
        age: u8,
        score: f32,
    };
    struct Color(i8, i16, i32);
   
    struct Rectangle {
        width: u32,
        height: u32,
    };
    // 结构体上定义方法
    impl Rectangle {
        fn area(&self) -> u32 {
            self.width * self.height
        }
    }
    // 结构体上定义关联函数
    impl Rectangle {
        fn square(size: u32) -> Rectangle {
            Rectangle {width: size, height: size}
        }
    }

    let s = Rectangle{width: 100, height: 200};
    println!(s.area());
}

fn enumType() {
    // 枚举
    enum country {
        China,
        USA,
    };
}