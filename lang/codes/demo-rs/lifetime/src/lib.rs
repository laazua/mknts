// - 生命周期:
//   Rust程序中每个变量都有一个固定的作用域,
//   当超出变量的作用域以后,变量就会被销毁.
//   变量在作用域中从初始化到销毁的整个过程称之为生命周期.
//
// - 生命周期与借用:
//   Rust中的借用是指对一块内存空间的引用.
//   Rust有一条借用规则是借用方的生命周期不能比出借方的生命周期还要长.
//
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
    data: &'a str,
}

impl<'a> Foo<'a> {
    fn new(data: &'a str) -> Foo<'a> {
        Foo { data }
    }

    fn get_data(&self) -> &'a str {
        self.data
    }
}

// - 静态生命周期变量: 'static
//   所有的字符串字面量都是静态生命周期的: let xx: &'static str = "abc";, &'static可以省略
//   static变量也是静态生命周期的: static num: u32 = 200;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let m = 100;
        let n = 200;
        println!("{}", max(&m, &n));

        {
            let o = 300;
            println!("{}", max(&n, &o));
        }

        let foo = Foo::new("hello world");
        println!("{}", foo.get_data());
    }
}
