pub trait Animal {
    fn make_sound(&self);
}

pub struct Cat;
pub struct Dog;

impl Animal for Cat {
    fn make_sound(&self) {
        println!("Meow ...");
    }
}

impl Animal for Dog {
    fn make_sound(&self) {
        println!("Woof ...");
    }
}

// trait bound 的语法糖
// &impl Animal | &dyn Animal
pub fn sound_wawa(animal: &impl Animal) {
    animal.make_sound();
}

// trait bound 语法
pub fn sound_meme<T: Animal>(animal: &T) {
    animal.make_sound();
}

// sound_wawa函数签名等价于sound_meme函数签名
