### gcc


- 源码安装

```
1. 下载源码
   gcc-14.2.0.tar.gz
2. 安装依赖
   apt-get install build-essential libgmp-dev libmpfr-dev libmpc-dev flex gcc-multilib
3. 构建源码
   tar -xf gcc-14.2.0.tar.gz && cd gcc-releases-gcc-14.2.0 && mkdir build && cd build
   CFLAGS="-m32 -ansi -D_SVID_SOURCE -DOSS_AUDIO -D'ARCH=\"$host_cpu\"' $CFLAGS" &&
   ../configure --prefix=/usr/local/gcc-14.2.0 --enable-languages=c,c++  --enable-multilib
   make -j$(nproc) && make install
```
