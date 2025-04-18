trait Perimeter {
    type Item;
    fn perimeter(&self) -> Self::Item;
}

trait Extend {
    type Item;
    fn extend(&self) -> Self::Item;
}

#[derive(Clone)]
struct Circle {
    radius: f64,
}

impl Perimeter for Circle {
    type Item = f64;
    fn perimeter(&self) -> Self::Item {
        2.0 * 3.14 * self.radius
    }
}

impl Extend for Circle {
    type Item = f64;
    fn extend(&self) -> Self::Item {
        3.14 * self.radius * self.radius
    }
}

#[derive(Clone)]
struct Square {
    side: u64,
}

impl Perimeter for Square {
    type Item = u64;
    fn perimeter(&self) -> Self::Item {
        4 * self.side
    }
}

impl Extend for Square {
    type Item = u64;
    fn extend(&self) -> Self::Item {
        self.side * self.side
    }
}

#[derive(Clone)]
struct Rectangle {
    width: u64,
    height: u64,
}

impl Perimeter for Rectangle {
    type Item = u64;
    fn perimeter(&self) -> Self::Item {
        2 * (self.width + self.height)
    }
}

impl Extend for Rectangle {
    type Item = u64;
    fn extend(&self) -> Self::Item {
        self.width * self.height
    }
}

fn calculate_perimeter<T: Perimeter>(shape: &T) -> T::Item {
    shape.perimeter()
}

fn calculate_extend<T: Extend>(shape: &T) -> T::Item {
    shape.extend()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let circle = Circle { radius: 2.5 };
        let square = Square { side: 4 };
        let rectangle = Rectangle{width: 3, height: 4 };
        let circle_perimeter = calculate_perimeter(&circle);
        let square_perimeter = calculate_perimeter(&square);
        let rectangle_perimeter = calculate_perimeter(&rectangle);
        let circle_extend = calculate_extend(&circle);
        let square_extend = calculate_extend(&square);
        let rectangle_extend = calculate_extend(&rectangle);

        assert_eq!(format!("{:.1}", circle_perimeter), "15.7");
        assert_eq!(square_perimeter, 16);
        assert_eq!(format!("{:.1}", circle_extend), "19.6");
        assert_eq!(square_extend, 16);
        assert_eq!(rectangle_perimeter, 14);
        assert_eq!(rectangle_extend, 12);
    }
}
