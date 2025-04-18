# 工具链

* 更新rust工具    
$ rustup set profile minimal    
$ export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup    
$ export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup     
$ rustup update    

* 国内源配置(vim ~/.cargo/config)    
[source.crates-io]    
replace-with = 'ustc'    
[source.ustc]    
registry = "https://mirrors.ustc.edu.cn/crates.io-index"    