//! 模式匹配

// match关键字
/*
enum Direction {
    East,
    West,
    North,
    South,
}

fn main() {
    let dire = Direction::South;
    match dire {
        Direction::East => println!("East"),
        Direction::North | Direction::South => {
            println!("South or North");
        },
        _ => println!("West"),
    };
}
//////////////////////
enum Direction {
    East,
    West,
    North,
    South,
}

fn main() {
    // let d_panic = Direction::South;
    let d_west = Direction::West;
    let d_str = match d_west {
        Direction::East => "East",
        Direction::North | Direction::South => {
            panic!("South or North");
        },
        _ => "West",
    };

    println!("{}", d_str);
}
////////解构/////////
enum Action {
    Say(String),
    MoveTo(i32, i32),
    ChangeColorRGB(u16, u16, u16),
}

fn main() {
    let action = Action::Say("Hello Rust".to_string());
    match action {
        Action::Say(s) => {
            println!("{}", s);
        },
        Action::MoveTo(x, y) => {
            println!("point from (0, 0) move to ({}, {})", x, y);
        },
        Action::ChangeColorRGB(r, g, _) => {
            println!("change color into '(r:{}, g:{}, b:0)', 'b' has been ignored",
                r, g,
            );
        }
    }
}
*/

// 模式: 是Rust另一个强大的特性。它可以被用在let和match表达式里面
/*
let x = 1;
let c = 'c';

match c {
    x => println!("x: {} c: {}", x, c),
}

println!("x: {}", x);
/////////////////////////
struct Point {
    x: i64,
    y: i64,
}
let point = Point { x: 0, y: 0 };
match point {
    Point { x, y } => println!("({},{})", x, y),
}
////////////////////////
struct Point {
    x: i64,
    y: i64,
}
let point = Point { x: 0, y: 0 };
match point {
    Point { x: x1, y: y1} => println!("({},{})", x1, y1),
}
////////////////////////
struct Point {
    x: i64,
    y: i64,
}

let point = Point { x: 0, y: 0 };

match point {
    Point { y, .. } => println!("y is {}", y),
}
///////////////////////
let tuple: (u32, String) = (5, String::from("five"));

let (x, s) = tuple;

// 以下行将导致编译错误，因为String类型并未实现Copy, 所以tuple被整体move掉了。
// println!("Tuple is: {:?}", tuple);

let tuple = (5, String::from("five"));

// 忽略String类型，而u32实现了Copy，则tuple不会被move
let (x, _) = tuple;

println!("Tuple is: {:?}", tuple);
//////////////////////
let x = 1;

match x {
    1 ... 10 => println!("一到十"),
    _ => println!("其它"),
}

let c = 'w';

match c {
    'a' ... 'z' => println!("小写字母"),
    'A' ... 'Z' => println!("大写字母"),
    _ => println!("其他字符"),
}
//////////////////////
let x = 1;

match x {
    1 | 2 => println!("一或二"),
    _ => println!("其他"),
}
/////////////////////
let mut x = 5;

match x {
    ref mut mr => println!("mut ref :{}", mr),
}
// 当然了……在let表达式里也能用
let ref mut mrx = x;
/////////////////////
let x = 1u32;
match x {
    e @ 1 ... 5 | e @ 10 ... 15 => println!("get:{}", e),
    _ => (),
}
/////////////////////
#[derive(Debug)]
struct Person {
    name: Option<String>,
}

let name = "Steve".to_string();
let x: Option<Person> = Some(Person { name: Some(name) });
match x {
    Some(Person { name: ref a @ Some(_), .. }) => println!("{:?}", a),
    _ => {}
}
////////////////////
let x = 4;
let y = false;

match x {
    4 | 5 if y => println!("yes"),
    _ => println!("no"),
}
*/