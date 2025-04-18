/// rust代码的结构控制

//! 条件判断
// if expr1 {} else {}
// if expr1 {} else if {} else {}

// rust的判断条件是表达式,而不是语句
let x = 100;
 let y = if x == 100 {
    200
 } else {
    250
 };

 // if let(match语法的简化形式)
 let x = Some(100);
 if let Some(y) = x {
    println!("{}", y);   // 输出100
 }

 let z = if let Some(y) = x {
    y
 } else {
     0
 };
 // z值为100

 //上面的代码等价于
 let x = Some(100)
 match x {
     Some(y) => println!("{}", y),
     None => ()
 }

 let z = match x {
     Some(y) => y,
     None => 0
 };

 //! 循环
 // for
 // for value in iterator {
 //   code
 // }
 for i in 0..10 {
     println!("{}", i)
 }

 for (index, value) in (10, 20).enumerate() {
     println!("index={}, value={}", index, value)
 }

 let lines = "Content of line one
Content of line two
Content of line three
Content of line four".lines();
for (linenumber, line) in lines.enumerate() {
    println!("{}: {}", linenumber, line);
}

// while
// while expr {
//    code
// }
let mut x = 5; // mut x: i32
let mut done = false; // mut done: bool

while !done {
    x += x - 3;

    println!("{}", x);

    if x % 5 == 0 {
        done = true;
    }
}

// loop,无限循环
// loop { code }

// break, continue
let mut x = 5;

loop {
    x += x - 3;

    println!("{}", x);

    if x % 5 == 0 { break; }
}

for x in 0..10 {
    if x % 2 == 0 { continue; }

    println!("{}", x);
}

// label
'outer: for x in 0..10 {
    'inner: for y in 0..10 {
        if x % 2 == 0 { continue 'outer; } // continues the loop over x
        if y % 2 == 0 { continue 'inner; } // continues the loop over y
        println!("x: {}, y: {}", x, y);
    }
}