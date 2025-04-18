// trait: 类似于接口

// 定义trait
trait P {
    fn say_name(&self, name: &str); 
}

struct Person<'a> {
    name: &'a str,
}

// 实现trait
impl<'a> P for Person<'_> {
    fn say_name(&self, name: &str) {
        println!("my name is {}", name);
    }
}

fn main() {
    let p = Person {
        name: "zhangsan",
    };
    p.say_name(p.name);
}
