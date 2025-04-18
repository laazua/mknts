#[cfg(test)]
mod tests {
    use macros;
    #[test]
    fn test_range() {
        // assert_eq!(macros::range!(5), 120);
        macros::range!(5)
    }
}
