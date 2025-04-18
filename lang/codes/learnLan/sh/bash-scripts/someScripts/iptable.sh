#!/bin/bash

# iptables防火墙策略由内核层面的netfilter网络过滤器来处理

## pack进人主机路线
#              nat                             filter
#  pack in ------------> router forward ------------------> in system
#           PREOUTING          |               INPUT            |
#                              |                                |
#                             \|/                              \|/ 
#                       filter FORWARD                      nat OUTPUT
#                             |                                 |
#                            \|/                                |
#                             nat  POSTROUTING <-----------------
#                                      |
#                                      |
#                                     \|/
#                                   pack out    

## 四表:
# raw:
# mangle:
# nat:
# filter

## 五链：
# PREOUTING:
# INPUT:
# OUTPUT
# FORWARD
# POSTROUTING

## note:
# 没有指定规则表则默认指filter表
# 不指定规则链则指表内所有的规则链
# 在规则链中匹配规则时会依次检查，匹配即停止（LOG规则例外），若没匹配项则按链的默认状态处理

## iptables命令中则常见的控制类型有:
# ACCEPT:允许通过.
# LOG:记录日志信息,然后传给下一条规则继续匹配.
# REJECT:拒绝通过,必要时会给出提示.
# DROP:直接丢弃,不给出任何回应

# ipt_cmd="/sbin/iptables"

# $ipt_cmd -F    #清空规则链
# $ipt_cmd -t nat -F    #清空nat表的规则链 
# $ipt_cmd -A INPUT -i lo -j ACCEPT    #filter表INPUT链上添加一条规则

# $ipt_cmd -t 表名 选项 [链名] [条件] [-j 控制类型]
# $ipt_cmd –[A|I 链] [-i|o 网络接口] [-p 协议] [-s 来源ip/网域] [-d 目标ip/网域] –j[ACCEPT|DROP]

# echo 1 > /proc/sys/net/ipv4/ip_forward    #开启端口转发

# $ipt_cmd -P INPUT DROP
# /sbin/iptables-save > /etc/sysconfig/iptables    #centos 6
# man iptables for more help