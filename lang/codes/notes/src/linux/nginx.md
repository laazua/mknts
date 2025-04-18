### nginx

- **nginx 升级**

```
  - 在原来的nginx基础上: 运行 nginx -V获取原来nginx的编译参数
  - 下载新版本的nginx源码使用原来的编译参数进行编译(不要make install)获取nginx二进制对象
  - 备份原来的nginx二进制文件, 使用新的nginx二进制文件替换原来的nginx二进制文件
  - 如果需要编译新的模块需要加上参数: --add-module=模块路径
```

- **日志客户端 IP 统计排名**
  cat access.log|awk '{print $1}'|sort|uniq -c|sort -nr|head -n 20
