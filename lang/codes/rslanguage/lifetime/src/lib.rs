/// 生命周期

pub fn example() {
    // a变量生命周期开始
    let a = 32;
    {
        // b变量生命周期开始
        let b = a;
        println!("{}, {}", a, b)
    }  // b变量生命周期结束
    // println!("{}", b);
} // a变量生命周期结束

// - 函数中的生命周期
//   下面的函数max中,函数参数是出借方,函数返回值是借用方
//   'b: 'a 标注'a的生命周期不能超过'b
pub fn max<'a, 'b: 'a>(m: &'a u32, n: &'b u32) -> &'a u32 {
    if m > n {
        &m
    } else {
        &n
    }
}

// - 结构体和impl中的生命周期
//   结构体成员是出借方,结构体本身是借用方
//   下面的示例表示Foo结构体和他的方法都一个生命周期参数'a
pub struct Foo<'a> {
    pub data: &'a str,
}

impl<'a> Foo<'a> {
    pub fn new(data: &'a str) -> Foo<'a> {
        Foo { data }
    }

    pub fn get_data(&self) -> &'a str {
        self.data
    }
}

// - 静态生命周期变量: 'static
//   所有的字符串字面量都是静态生命周期的: let xx: &'static str = "abc";, &'static可以省略
//   static变量也是静态生命周期的: static num: u32 = 200;