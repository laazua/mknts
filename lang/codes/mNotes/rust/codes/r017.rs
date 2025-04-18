// 结构体绑定方法

// 声明一个长方形结构体类型
#[derive(Debug)]
struct Rect {
    width: u32,
    height: u32,
}

// 给长方形结构类型绑定方法和关联函数
impl Rect {
    // area是Rect结构体的一个方法
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    // 关联函数
    fn print_width(width: u32) {
        println!("rect width = {}", width);
    }
}

// 同一个结构体可以有多个impl块
impl Rect {
    fn print_height(height: u32) {
        println!("rect height = {}", height);
    }
}

fn main() {
    let rect = Rect {
        width: 2,
        height: 4,
    };
    // 调用结构体方法
    println!("rect area = {}", rect.area());
    // 调用结构体关联函数
    Rect::print_width(rect.width);
    
    // 多个通一个结构体多个impl测试
    Rect::print_height(rect.height);
}
