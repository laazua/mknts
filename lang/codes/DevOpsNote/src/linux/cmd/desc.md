# Cmd

- [网络诊断工具](https://github.com/OpenCloudOS/nettrace)

- **隐藏痕迹**
  - 在终端敲命令时,先空一格,再输入命令

- **top**
  - 查看指定服务的资源使用情况: top -c -p $(pgrep -d ',' -f nginx)

- **awk**
  - 按照指定的列去重: awk '!arr[$9]++'   # 按照第9列去重
  - 使用数组数据统计: awk '{a[$1]++}END{for(v in a) print a[v], v}' /var/log/nginx/access.log

- **归档打包**
  - tar -cf - test/ |xz -9ze -T1 >test.tar.xz

- **防止文件被重定向**
  - set -o noclobber # 可以写入.bashrc文件中
  - 如果确实要重定向: echo "xadf" >| test.txt

- **linux端口是否监听**  
  - echo >/dev/tcp/ip/port  # 没有输出在监听,否则没有监听
