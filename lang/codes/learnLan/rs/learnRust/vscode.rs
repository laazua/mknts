/*
vscode 远程开发配置

-- 官方下载rust并并配置国内源
    vim $HOME/.cargo/config
    [source.crates-io]
    registry = "https://github.com/rust-lang/crates.io-index"
    replace-with = 'sjtu'
    [source.tuna]
    registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
    [source.sjtu]
    registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index"
    [target.x86_64-apple-darwin]
    rustflags = [
    "-C", "link-arg=-undefined",
    "-C", "link-arg=dynamic_lookup",
    ]

    source $HOME/.cargo/env

-- vscode配置
   安装：rust-analyzer, CodeLLDB

-- glibc安装
   wget wget http://mirrors.ustc.edu.cn/gnu/libc/glibc-2.18.tar.gz
   tar -zxvf glibc-2.18.tar.gz && cd glibc-2.18 && mkdir build && ../configure --prefix=/usr && make -j4 && make install

-- rust-analyzer安装
   github下载: rust-analyzer-x86_64-unknown-linux-gnu
   mv rust-analyzer-x86_64-unknown-linux-gnu /home/gamecpp/.vscode-server/data/User/globalStorage/matklad.rust-analyzer/
*/