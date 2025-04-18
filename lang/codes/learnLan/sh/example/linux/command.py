#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""
linux操作
"""
from __future__ import print_function

print("""
# 删除0字节文件
  find ./ -type f -size 0 -exec rm -rf {} \;

# 查看进程,按内存从达到小排列
  ps -e -o "%C : %p : %z : %a" | sort -k5 -nr |head -n 10

# 查看进程,按cpu利用率从大到小排列
  ps -e -o "%C : %p : %z : %a" | sort -nr |head -n 10

# 查看http的并发请求数及其TCP连接状态
  netstat -n | awk "/^tcp/{++S[$NF]} END {for(a in S) print a, S[a]}"

# 如何杀掉mysql进程
  ps aux | grep mysql | grep -v grep | awk "{print $2}" | xargs kill
  killall -TERM mysqld

# 显示运行3级别开启的服务
  ls /etc/rc3.d/S* | cut -c 15-

# 编写shell显示多个信息(EOF)
  cat << EOF
  +-----------------------------+
  |    === WELCOME TO ===       |
  +-----------------------------+

# for的巧用(如给mysql建软链接)
  cd /usr/local/mysql/bin
  for i in *; do
      ln /usr/local/mysql/bin/$i /usr/bin/$i
  done

# 获取内网地址
  ifconfig eth0 | grep "inet addr:" | awk "{print $2}" | cut -c 6-  或者
  ifconfig | grep "inet addr:" | grep -v grep "127.0.0.1" | cut -d: -f2 | awk "{print $1}"

# cpu核数
  cat /proc/cpuinfo |grep -c processor

# cpu负载
  cat /proc/loadavg    检查前三个输出值是否是系统逻辑cpu数量的4倍
  mpstat 1 1           检查%idle是否过低(小于5%)
	
# 查看某个目录下文件占用空间情况
  du -cks * | sort -rn |head -n 10

# 磁盘I/O负载
  iostat -x 1 2        检查I/O使用率(%util)是否超过100%

# 网络负载
  sar -n DEV	       检查网络流量(rxbyt/s, txbyt/s)是否过高

# 网络错误
  netstat -i           检查是否有网络错误(drop fifo colls carrier), 也可以用命令: cat /proc/net/dev

# 网络连接数目
  netstat -an | grep -E "^(tcp)" | cut -c 68- | sort |uniq -c | sort -n

#=================================================================================================
# 严禁酒后操作线上服务器
# 严禁情绪激动操作线上服务器
# 严禁长时间加班操作线上服务器
# 严禁线上实验不熟悉的命令
# 重要系统先做备份

# 常用ip addr(ifconfig) && pwd 确认当前光标位置

# rm -rf 将递归强制删除文件,执行该命令一定要慢,并多次确认
# rm -rf ./*  => rm -rf /
# rm -rf abc/ => rm -rf abc /
# 脚本中执行rm -rf, 如: rm -rf ${variable}/*   一定要判断variable变量是否为空

# chmod 命令更改文件多个权限,要先备份文件权限,否则会和rm有一样的后果
备份: getfacl -R / > chmod.txt
恢复: setfacl --restore=chmod.txt

# cat命令
cat somefile >> file   注意是追加少写一个箭头会覆盖file, echo也一样

# cp命令, alias cp='cp -i' 在拷贝时生成一个备份文件（mv类似）

# tar命令解压时,如果当前目录存在同名文件,则会覆盖同名文件.

# vim命令,不要用此命令来阅读文件(用more,less代替,或者view只读打开文件)

## mysql操作
1.使用 mysql -U
     --safe-updates, --i-am-a-dummy, -U  (别名设置alias mysql='mysql -U')
     使用mysql -U 防止delete,update执行没带where条件操作,当发出没有WHERE或LIMIT关键字的UPDATE或DELETE时，mysql程序拒绝执行

2.使用事务
     start transaction
     执行
     确认
     commit

3.DML误操作回滚,可以使用binlog2sql

4.小心DDL操作(尽量在业务低峰执行,而且尽量采用inplace方式操作)

""")
