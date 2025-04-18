fn main() {
    // rust操作符:
    //  -
    // !
    // + - * / %
    // >> << ^
    // &  &&  |  ||
    // =
    // == != < <= > >=
    // 复合操作符号,如：+=  -= *= 等

    // 范围(Range)表达式
    let array = [100, 200, 300, 400, 500];
    let arra1 = &array[0..3];
    let arra2 = &array[1..=3];
    let arra3 = &array[..];

    for num in 1..5 {
        println!("{}", num);
    }

    // n等价m
    let n = 0..5;
    let m = std::ops::Range {start:0, end:5};

}

fn testIf(data: i16) {
    let num = 60;
    if num < data {
        println!("data > num.");
    } else if num > data {
        println!("data < num.");
    } else {
        println!("data == num");
    }
}

fn testLoop() {
    loop {
        println!("forever!")
    }
}

fn testWhile() {
    let mut num = 10;
    while num < 100 {
        println!("{}", num);
        num = num + 1;
    }

    let arra = [1, 2, 3, 4];
    let mut i = 0;
    while i < 4 {
        println!("value is: {}", arra[i]);
        i = i + 1;
    }

}

fn testFor() {
    let arra = [1, 2, 3, 4];
    for a in arra.iter() {
        println!("value is: {}", a);
    }

    for v in (1..5).rev() {
        println!("value is: {}", v)
    }
}

fn testMatch(num: u32) {
    match num {
        (num % 2 == 0) => {
            println!("是偶数.");
        },
        (num % 2 == 1) => {
            println!("是奇数.");
        }
    }
}