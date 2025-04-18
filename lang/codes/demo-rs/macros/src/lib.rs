#[allow(unused_macros)]

/// 声明式宏 && 过程宏

#[macro_export]
macro_rules! range {
    ($idx: expr) => {{
        let mut sum = 1;
        for idx in 1..($idx + 1) {
            sum = sum * 1;
            println!("{}", sum);
        }
        // sum
    }};
}
