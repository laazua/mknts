// PartialOrd+Copy对泛型进行约束
fn largest<T: PartialOrd+Copy>(list: &[T]) -> T {
    let mut largest = list[0];
    for &item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

#[derive(Debug)]
struct Point<T1, T2> {
    x: T1,
    y: T2
}

fn main(){
    let numbers = vec![34, 50, 25, 100, 65];
    let result = largest(&numbers);
    println!("this largest number is {}", result);

    let p = Point{x: 5, y: 6.3};
    println!("p = {:?}", p);
}