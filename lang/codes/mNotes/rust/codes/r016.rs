// 结构体

#[derive(Debug)]
#[allow(dead_code)]
struct User {
    name: String,
    age: u64,
}

// 使用没有名字字段的元组创建结构体
#[derive(Debug)]
struct Color(i32, i32, i32);

// 没有任何字段的单元结构体
#[derive(Debug)]
struct AlwaysEqual;

fn main() {
    let user1 = User {
        name: String::from("张三"),
        age: 18,
    };
    println!("user1 = {:?}", user1);

    let user2 = User {
        name: String::from("李四"),
        ..user1
    };
    println!("user2 = {:#?}", user2);
    // 上面代码运行结果
    // user1 = User { name: "张三", age: 18 }
    // user2 = User {
    //    name: "李四",
    //    age: 18,
    // }

    let color = Color(1, 1, 1);
    println!("color = {:?}", color);
    // 上面代码运行结果
    // color = Color(1, 1, 1)
    
    let obj = AlwaysEqual;
    println!("obj = {:?}", obj);
    // 上面代码运行结果
    // obj = AlwaysEqual
}

