// 导入测试框架
#[cfg(test)]
mod tests {
    // 导入要测试的lib
    use ownership;

    // 编写测试函数
    #[test]
    fn test_display_heap_data() {
        let text = String::from("hello world"); // text 进入作用域

        ownership::display_heap_data(text); // text 的值移动到函数里 ...
                                            // ... 所以到这里不再有效
        println!("{:?}", text); // 这里会报错, text已经无效
    }

    #[test]
    fn test_display_stack_data() {
        let num = 5; // num 进入作用域

        ownership::display_stack_data(num); // num 应该移动函数里，
                                            // 但 i32 是 Copy 的，
                                            // 所以在后面可继续使用 num
        println!("{}", num); // 这里不会报错
    }
}
