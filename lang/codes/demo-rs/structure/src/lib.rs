pub struct User {
    pub name: String,
    pub address: String,
}

pub struct Animal<'a> {
    pub variety: &'a str,
}

pub struct Circle {
    pub radius: f64,
}

impl Circle {
    // 方法第一个参数:
    //   &self => self: &Self
    //   &mut self => self: &mut Self
    pub fn show_eare(&self) -> f64 {
        return self.radius * self.radius * 3.14;
    }

    pub fn modify_radius(self: &mut Self, radius: f64) {
        self.radius = radius;
    }
}
