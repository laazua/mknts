// 控制流

fn main() {
    // if 控制流
    let x: i8 = 100;
    if x > 0 {
       println!("x > 0");
    }

    if x > 0 {
       println!("x > 0");
    } else {
       println!("x < 0");
    }

    if x > 0 {
       println!("x > 0");
    } else if x < 0 {
        println! ("x < 0");
    } else {
        println!("x == 0");
    }

    // let-if: 每个if后的块类型必须一致
    let y = if true {
        200
    } else {
        300
    };
    println!("y = {}", y);

    // loop 控制流
    let mut i: i8 = 0;
    loop {
        println!("{}", i);
        if i == 5 {
            break;
        }
        i += 1; 
    }
    // let-loop
    let x = loop {
        i += 1;
        if i == 10 {
            break i;
        }
    };
    println!("{}", x);

    // while 控制流
    let mut i: i8 = 0;
    while i != 10 {
        i += 1
    }

    // for 控制流
    let arra: [u8; 5] = [1, 2, 3, 4, 5];
    for v in &arra {
        println!("{}", v);
    }

    // match条件匹配
    let x = 10;
    match x {
        0 => println!("get x == 0"),
        1..=5 => println!("in 1-5"),
        6..=9 => println!("in 6-9"),
        10 => println!("get x == 10"),
        _ => (),
    }
}

