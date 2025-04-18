### alpine:glibc

* **制作**  
1. 运行基础的alpine镜像: podman run --name alpine --rm -itd alpine:3.19.1 sh  
2. 进入基础的alpine容器: podman exec -it alpine sh  
3. [参考](https://github.com/sgerrand/alpine-pkg-glibc)安装glibc:   
   a. wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub  
   b. apk add glibc-2.35-r1.apk  
4. 建立库的软连接: mkdir /lib64 && ln -s /usr/glibc-compat/lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2  
5. 将安装glibc是产生的文件进行清理(rm glibc-2.35-r1.apk)并退出容器  
6. 打包镜像: podman export alpine > alpine-glibc.tar  
7. 使用镜像: cat alpine-glibc.tar | podman import - alpine:glibc-2.35.r1  

* **说明**
1. 打包镜像并压缩: podman export alpine |gzip >alpine-python-3.11.9.tar.gz
2. 导入镜像并解压: gzip -d alpine-python-3.11.9.tar.gz |podman import - alpine-python-gz:3.11.9
