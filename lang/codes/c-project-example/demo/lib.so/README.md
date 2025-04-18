## 动态库


* *编译动态链接库*
```
  - 参数
    -fPIC      产生位置无关的代码
    -shared    共享
    -l         指定动态库
    -I         指定头文件目录(默认当前目录)
    -L         指定动态库文件搜索目录, 默认只链接共享目录

  - 生成共享库文件(一定要以lib开头: libsoExample.so)
    gcc -shared -fPIC -o libsoExample.so soExample.c

  - 编译程序时使用共享库
    gcc -L./ -lsoExample main.c -o main

  - 配置动态链接库路径(/etc/ld.so.conf, /etc/ld.so.conf.d/*.conf)
  - 将动态库libsoExample.so添加到动态库配置文件指定的路径中去才能运行程序main
  - 例如将软连接文件放在/lib64路径下
```
