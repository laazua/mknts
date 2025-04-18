## learn runs

```
  - 参考: 
    https://www.rust-lang.org/zh-CN/learn
    https://doc.rust-lang.org/std/
  - rust基本语法
  - rust常用包
```

```
  - rust代码组织(模块系统)
    1 package(包): cargo的特性,可以构建,测试,共享crate
    2 crate(单元包): 一个模块树,可产生一个library或可执行文件
    3 module(模块,use): 控制代码的组织,作用域,私有路径
    4 path(路径): 为struct, function或module等项的命名方式
  
  - package和crate
    crate类型:
      - binary
      - library
    crate root:
      - 是源代码文件
      - rust编译器从这里开始,组成crate的根module
    一个package:
      - 包含1个Cargo.toml, 描述了如何构建crates
      - 只能包含0-1个library crate
      - 可以包含任意数量的binary crate
      - 但必须至少包含一个crate(library或binary)
  - 例子
    src/main.rs:
      - binary crate的crate root
      - crate名与package名相同
    src/lib.rs:
      - package包含一个library crate
      - library crate的crate root
      - crate名与package名相同
    cargo把crate root文件交给rustc来构建library或binary
```