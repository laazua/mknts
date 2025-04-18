### cargo 使用方法
```
  -- cargo new helloCargo   新建一个项目: helloCargo/
                                                    ├── Cargo.toml
                                                    ├── readme.md
                                                    └── src
                                                        └── main.rs
  -- cargo build(cargo run) 构建项目: helloCargo/
                                                ├── Cargo.lock
                                                ├── Cargo.toml
                                                ├── readme.md
                                                ├── src
                                                │   └── main.rs
                                                └── target
                                                    ├── CACHEDIR.TAG
                                                    └── debug
                                                        ├── build
                                                        ├── deps
                                                        │   ├── helloCargo-bdd74b26b3a95568
                                                        │   └── helloCargo-bdd74b26b3a95568.d
                                                        ├── examples
                                                        ├── helloCargo
                                                        ├── helloCargo.d
                                                        └── incremental
                                                            └── helloCargo-3231js4pl325s
                                                                ├── s-g1zcatiigz-mla98n-2mj5boyjhefiy
                                                                │   ├── 1npezk5kvpi1o4hs.o
                                                                │   ├── 2kwwqgsx9h4qv0d5.o
                                                                │   ├── 2xinr7pxgm6l19vy.o
                                                                │   ├── 449a02pzd1fwkq3u.o
                                                                │   ├── 4pt752e45gzvd12c.o
                                                                │   ├── 55yfy77z7lxsbwzr.o
                                                                │   ├── 5cr0dw903q3ha3gn.o
                                                                │   ├── dep-graph.bin
                                                                │   ├── query-cache.bin
                                                                │   ├── work-products.bin
                                                                │   └── x5pqzwgdtzr16x5.o
                                                                └── s-g1zcatiigz-mla98n.lock
  -- cargo check 快速检查代码,确保其可以编译
  -- cargo build --release  构建后的代码用于发布
  -- cargo update  忽略Cargo.lock 文件,并计算出所有符合Cargo.toml声明的最新版本.如果成功了,Cargo会把这些版本写入Cargo.lock文件

  --cargo new --lib libtest  创建一个名为libtest的库
```