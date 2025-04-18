### 安装haproxy

- **环境依赖**
1. 系统：debian 12
2. 依赖：apt install -y build-essential libssl-dev liblua5.4-dev libpcre2-dev

- **源码安装**
1. 下载源码：wget https://github.com/haproxy/haproxy/archive/refs/tags/v3.1.0.tar.gz
2. 编译源码: tar -xf v3.1.0.tar.gz && cd haproxy-3.1.0 && sudo make -j $(nproc) TARGET=linux-glibc USE_OPENSSL=1 USE_QUIC=1 USE_QUIC_OPENSSL_COMPAT=1 USE_LUA=1 USE_PCRE2=1 && sudo make install
3. 执行上面编译步骤会在当前目录生成 haproxy 二进制文件.
4. 具体编译细节参考仓库的 INSTALL 文件
