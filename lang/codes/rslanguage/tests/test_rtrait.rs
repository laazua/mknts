#[cfg(test)]
mod tests {
    use keyword;
    use keyword::rtrait::demo::Sing;
    
    #[test]
   fn test_trait() {
        let p1 = keyword::rtrait::demo::Chinese::new();
        p1.speak();
        let p2 = keyword::rtrait::demo::American::new();
        p2.speak();
    }
}