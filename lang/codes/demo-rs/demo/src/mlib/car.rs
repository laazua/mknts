
pub trait Car {
    fn run(self);
}

pub struct BenZi {
    pub name: String
}

impl Car for BenZi {
    fn run(self) {
        println!("{} running ..., bz bz", self.name)
    }
}

pub struct BaoMa {
    pub name: String
}

impl Car for BaoMa {
    fn run(self) {
        println!("{} running ..., bm bm", self.name)
    }
}

pub fn run_car(car: impl Car) {
    car.run()
}