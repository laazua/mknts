### 安装keepalived

- **环境依赖**
1. 系统：debian 12
2. 依赖: sudo apt install -y build-essential pkg-config libipset-dev libnl-3-dev libnl-genl-3-dev libssl-dev automake autoconf

- **源码安装**
1. 下载源码：wget https://github.com/acassen/keepalived/archive/refs/tags/v2.3.2.tar.gz
2. 编译源码: tar -xf v2.3.2.tar.gz && cd keepalived-2.3.2 && ./autogen.sh && ./configure --prefix=/usr/local/keepalived-2.3.2
3. sudo make -j $(nproc) && sudo make install
4. 具体编译细节参考仓库的 INSTALL 文件