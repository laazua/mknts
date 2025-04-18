/// 关键字示例
pub mod rtrait;

// 模块mod
pub mod m_module {
    // 对外不可见
    fn example_a() {
        println!("a: hello world");
    }

    // 对外可以见
    pub fn example_b() {
        example_a();
        println!("b: hello world");
    }

    // crate之内可见,crate之外不可见
    pub(crate) fn _example_c() {
        println!("c: hello world");
    }

    // 只能在当前模块的父模块可见
    pub(super) fn _example_d() {
        println!("d: hello world");
    }
}

pub mod outer {
    // 外部都可以访问
    pub fn example() { println!("hello world"); inner::example() }
    // crate内部可以访问
    pub(crate) fn _example_x() { println!("hello world");  }
    pub mod inner {
        // 当前模块的父模块可以访问
        pub(super) fn example() { println!("hello world"); }
    }
}