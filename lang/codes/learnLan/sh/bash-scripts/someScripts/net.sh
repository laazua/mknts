#!/bin/bash

# 标准网络接口缺省的MTU(最大传输单元): 1500字节, 是最大帧1518减去源宿的MAC, FCS后最大的IP packet大小
#    MTU - 20字节IP包头

# linux系统tcp断开连接后，会以TIME_WAIT状态保留一段时间，然后才释放端口。当并发请求过多时，会产生大量TIME_WAIT状态的连接，不及时断开会占用端口和服务器资源。
# netstat -n|awk '/^tcp/ {++S[$NF]} END{for(a in S) print a, S[a]}'，输出如下结果:
# LAST_ACK    16
# SYN_RECV    348
# ESTABLISHED 70
# FIN_WAIT1   229
# FIN_WAIT2   30
# CLOSEING    33
# TIME_WAIT   18000

# 解决方法:
#    vim /etc/sysctl.conf,加入如下内容
#    net.ipv4.tcp_syncookies = 1         #开启YSN Cookies,当出现SYN等待队列溢出时,启用cookies来处理,可防范少量SYN攻击
#    net.ipv4.tcp_tw_reuse = 1           #允许TIME_WAIT sockets重新用于新的tcp连接
#    net.ipv4_tcp_tw_recycle = 1         #开启tcp连接中TIME_WAIT sockets的快速回收
#    net.ipv4.tcp_fin_timeout = 30       #修改系统默认的TIMEOUT时间
# sysctl -p 使内核参数生效

# 如果连接数本身很多，可以优化一下tcp可使用的端口范围，提高并发能力(流量比较大的服务器上可以添加一下参数，小流量没必要添加):
#    net.ipv4.tcp_keepalive_time = 1200              #当keepalive启用时，tcp发送keepalive消息的频度,缺省是2小时，改为20分钟
#    net.ipv4.ip_local_port_range = 10000 65000      #用于向外连接的端口范围，缺省情况下很小：32768-61000，改为10000-65000
#    net.ipv4.tcp_max_syn_backlog = 8192             #SYN队列的长度,默认1024，加大队列长度到8192，可以容纳更多等待连接的网络连接数
#    net.ipv4.tcp_max_tw_buckets = 5000              #系统保持TIME_WAIT的最大数量，超过这个数量TIME_WAIT将立即被清除默认180000，改为5000；对于apache,nginx等服务器，以上参数可以很好的减少TIME_WAIT套接字数量，但是对于squid效果不

## 主机网络配置
# TYPE=Ethernet
# BOOTPROTO=static
# NAME=ens33
# DEVICE=ens33
# ONBOOT=yes
# IPADDR=192.168.7.21
# NETMASK=255.255.255.0
# GATEWAY=192.168.7.254
# DNS1=192.168.5.149
## 桥接模式