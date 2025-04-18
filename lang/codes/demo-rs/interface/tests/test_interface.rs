// 导入测试框架
#[cfg(test)]
mod tests {
    use interface;

    #[test]
    fn test_sound_wawa() {
        let dog = interface::Dog;
        interface::sound_wawa(&dog);
    }

    #[test]
    fn test_sound_meme() {
        let cat = interface::Cat;
        interface::sound_meme(&cat);
    }
}
