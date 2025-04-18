// - 简单的示例
// 声明接口
pub trait Behavior {
    fn run(&self);
    fn swim(&self);
}

pub struct Dog<'a> {
    pub name: &'a str, // 使用 &str 类型，要求指定生命周期
}

impl<'a> Dog<'a> {
    // 创建一个新的 Dog 实例
    pub fn new(name: &'a str) -> Self {
        Dog { name }
    }
}

// 实现Behavior接口
impl<'a> Behavior for Dog<'a> {
    fn run(&self) {
        println!("{} running ...", self.name);
    }

    fn swim(&self) {
        println!("{} swimming ...", self.name);
    }
}

// - trait中关联type类型占位符
pub trait Sing {
    type Person;
    fn speak(&self);
}

pub struct Chinese {
    pub name: String,
}

impl Sing for Chinese {
    type Person = String;

    fn speak(&self) {
        println!("i am chinese.");
    }
}

pub struct American {
    pub name: String,
}

impl Sing for American {
    type Person = String;

    fn speak(&self) {
        println!("i am american.")
    }
}

impl Chinese {
    pub fn new() -> Self {
        Chinese{name: "张三".parse().unwrap() }
    }
}

impl American {
    pub fn new() -> Self {
        American{name: "卢卡斯".parse().unwrap() }
    }
}

#[cfg(test)]
mod test {
    #[test]
    fn test_mod() {
        crate::m_module::example_c();
        crate::m_module::example_d();
    }
}