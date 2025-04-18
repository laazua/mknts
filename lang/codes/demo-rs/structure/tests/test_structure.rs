#[cfg(test)]
mod tests {
    use structure;

    #[test]
    fn test_user() {
        let user = structure::User {
            name: String::from("zhangsan"),
            address: String::from("beijing"),
        };
        println!("name: {}, address: {}", user.name, user.address);
    }

    #[test]
    fn test_animal() {
        let animal = structure::Animal { variety: "cat" };
        println!("variety: {}", animal.variety);
    }

    #[test]
    fn test_show_circle() {
        let circle = structure::Circle { radius: 3.0 };
        println!("eare: {}", circle.show_eare());
    }

    #[test]
    fn test_modify_radius() {
        let mut circle = structure::Circle { radius: 3.0 };
        println!("eare: {}", circle.show_eare());
        circle.modify_radius(4.0);
        println!("eare: {}", circle.show_eare());
    }
}
