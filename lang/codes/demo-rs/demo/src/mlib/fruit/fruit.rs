pub trait Fruit {
    fn show(self);
}
pub struct Apple;

impl Fruit for Apple {
    fn show(self) {
        println!("it is apple ...")
    }
}

pub struct Banana;

impl Fruit for Banana {
    fn show(self) {
        println!("it is banana ...")
    }
}

pub fn show_fruit(fruit: impl Fruit) {
    fruit.show()
}