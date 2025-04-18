#!/bin/bash

## 清空链
iptables -F
## 清空子链
iptables -X
#iptables -t nat -F
## 清空规则链中的数据包
iptables -Z
## 设置默认策略
iptables -P INPUT DROP

iptables -A INPUT -i lo -p all -j ACCEPT
iptables -A INPUT -p tcp -m multiport --dports 22,8888,8880 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 5000:5010 -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables-save > /etc/sysconfig/iptables-config
