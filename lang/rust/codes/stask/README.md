### stask


##### 编译
```bash
# 清理编译
cargo clean

# 自动修复一些警告
cargo fix --lib --allow-dirty
cargo fix --bin stask-server --allow-dirty
cargo fix --bin stask-client --allow-dirty

# 然后重新编译
cargo build --release
```