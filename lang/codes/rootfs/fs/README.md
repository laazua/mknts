### alpine-golang:3.19.3

**[说明]**  
1. ld-linux-x86-64.so.2 和libc.so.6是运行golang文件所需的库文件  
2. ld-linux-x86-64.so.2 放置在: /lib64/ld-linux-x86-64.so.2 (mkdir /lib64)  
3. libc.so.6 放置在: /usr/lib/x86_64-linux-gnu/libc.so.6 (mkdir /usr/lib/x86_64-linux-gnu/)  

**[制作]**  
1. cat alpine-minirootfs-3.20.0-x86_64.tar.gz | podman import - alpine:3.19.3  
2. podman run --name alpine -itd --rm alpine:3.19.3  
3. podman exec -it alpine sh  
4. mkdir /usr/lib/x86_64-linux-gnu/ && mkdir /lib64 && exit  
5. podman cp ld-linux-x86-64.so.2 alpine:/lib64/  
6. podman cp libc.so.6 alpine:/usr/lib/x86_64-linux-gnu/  
7. podman export alpine > alpine-golang-3-19-3.tar  
8. cat alpine-golang-3-19-3.tar | podman import - alpine-golang:3.19.3  

**[rootfs]**
1. [ubuntu](https://cloud-images.ubuntu.com/)
2. [alpine](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86_64/)


**[推送]**  
1. 说明: U2FsdGVkX18I5851oYAQITcTYY/SH4oMWjPoxRXoo5qCeXdUohQjRPozjY3t4b029d6jLfw838l+bha3gjD3Pg== 该字符串是加密后的字符串  
2. echo U2FsdGVkX18I5851oYAQITcTYY/SH4oMWjPoxRXoo5qCeXdUohQjRPozjY3t4b029d6jLfw838l+bha3gjD3Pg== |podman login ghcr.io -u confucuis --password-stdin  
3. podman tag localhost/alpine-golang:3.19.3 ghcr.io/confucuis/alpine-golang:3.19.3  

**[拉取]**  
1. 说明: U2FsdGVkX18I5851oYAQITcTYY/SH4oMWjPoxRXoo5qCeXdUohQjRPozjY3t4b029d6jLfw838l+bha3gjD3Pg== 该字符串是加密后的字符串  
2. echo U2FsdGVkX18I5851oYAQITcTYY/SH4oMWjPoxRXoo5qCeXdUohQjRPozjY3t4b029d6jLfw838l+bha3gjD3Pg== |podman login ghcr.io -u confucuis --password-stdin  
3. podman pull ghcr.io/confucuis/alpine-golang:3.19.3  

[[阿里云镜像地址](https://developer.aliyun.com/mirror/)]  
[[linux容器镜像地址](https://images.linuxcontainers.org/images/)]
<!-- 
[解密密钥]  
    mypass: 加密时的密码(仓库密码)  
    echo U2FsdGVkX18I5851oYAQITcTYY/SH4oMWjPoxRXoo5qCeXdUohQjRPozjY3t4b029d6jLfw838l+bha3gjD3Pg==|openssl enc -aes-256-cbc -d -a -pbkdf2 -pass pass:mypass  
-->
