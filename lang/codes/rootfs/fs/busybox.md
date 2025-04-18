### busybox

**[制作步骤]**
1. wget https://busybox.net/downloads/busybox-1.35.0.tar.bz2
2. tar -xf busybox-1.35.0.tar.bz2 
3. cd busybox-1.35.0/
4. make menuconfig     // 选择: Build BusyBox as a static binary
5. make && make install
6. cd _install/
7. rm linuxrc
8. tar -cf /dev/stdout *|podman import - busybox:1.35.0
9. podman images
10. podman  run --name busybox --rm -itd busybox:1.35.0 sh
11. podman ps -a
12. podman exec -it busybox sh

**[另外说明]**
1. 如果是程序是go文件,则需要是静态编译的go二进制文件
2. 如果程序是python包,则需要在上面的基础镜像的制作过程中将python编译到镜像中去,即在步骤7之后进行如下操作:  
   a. wget https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz && cd Python-3.11.6  
   b. ./configure --prefix=/python --enable-optimizations && make -j$(nproc) && make install DESTDIR=../busybox-1.35.0/_install  
3. 如果需要让busybox可以运行非静态编译的程序,则需要在上面步骤6(cd _install)后执行一下操作:  
   a. mkdir -p lib/x86_64-linux-gnu/ && cp -r /lib/x86_64-linux-gnu/libc.so* lib/x86_64-linux-gnu/ && mkdir lib64 && cp /lib64/ld-linux-x86-64.so.2 lib64/  
   b. 新建: etc/ld.so.conf 文件并写入:   
      /lib  
      /lib64  
      /lib/x86_64-linux-gnu  
