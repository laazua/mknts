#!/bin/bash

# firewalld由内核层面的nftables包过滤框架来处理

## 常用的区名称及策略规则
# trusted
# home
# internal
# work
# public
# external
# dmz
# block
# drop

## 常用参数
# --get-default-zone	查访默认的区域名称
# --set-default-zone=<区域名称>	设置默认的区域，使其永久生效
# --get-zones	显示可用的区域
# --get-services	显示预定义的服务
# --get-active-zones	显示当前正在使用的区域、来源地址和网卡名称
# --add-source=	将源自此IP或子网的流量导向指定的区域
# --remove-source=	不再将源自此IP或子网的流量导向这个区域
# --add-interface=<网卡名称>	将源自该网卡的所有流量都导向某个指定区域
# --change-interface=<网卡名称>	将某个网卡与区域进行关联
# --list-all	显示当前区域的网卡配置参数、资源、端口以及服务等信息
# --list-all-zones	显示所有区域的网卡配置参数、资源、端口以及服务等信息
# --add-service=<服务名>	设置默认区域允许该服务的流量
# --add-port=<端口号/协议>	设置默认区域允许该端口的流量
# --remove-service=<服务名>	设置默认区域不再允许该服务的流量
# --remove-port=<端口号/协议>	设置默认区域不再允许该端口的流量
# --reload	让“永久生效”的配置规则立即生效，并覆盖当前的配置规则
# --panic-on	开启应急状况模式,拒绝所有流量，远程连接会立即断开，只有本地能登陆
# --panic-off	关闭应急状况模式,取消应急模式，但需要重启firewalld后才可以远程ssh
# 注意：启动关闭firewalld防火墙服务的应急状况模式，远程连接服务器时请慎用
# firewall-cmd --query-panic  # 查看是否为应急模式

## 示例， 注：不指定--zone参数的话，将会对默认区域进行设置
# firewall-cmd --zone=drop --add-service=https, 在drop区域开放https服务
# firewall-cmd --zone=drop --remove-service=https, 取消开放https服务，即禁止https服务
# firewall-cmd --zone=drop --add-port=22/tcp, 开放22端口
# firewall-cmd --zone=drop --remove-port=22/tcp, 取消开放22端口
# firewall-cmd --zone=drop --add-port=8080-8081/tcp, 开放8080和8081端口
# firewall-cmd --zone=drop --list-ports, 查询drop区域开放了哪些端口
# firewall-cmd --zone=drop --add-protocol=icmp, 允许icmp协议流量，即允许ping
# firewall-cmd --zone=drop --remove-protocol=icmp, 取消允许icmp协议的流量，即禁ping
# firewall-cmd --zone=drop --list-protocols, 查询drop区域开放了哪些协议
# firewall-cmd --zone=drop --add-forward-port=port=888:proto=tcp:toport=22, 将原本访问本机888端口的流量转发到本机22端口
# firewall-cmd --zone=drop --add-masquerade && firewall-cmd --zone=drop --add-forward-port=port=888:proto=tcp:toport=22:toaddr=192.168.2.208将原本访问本机888端口的流量转发到ip为192.168.2.208的主机的22端口，需要开启masquerade


## 富规则的设置
# firewall-cmd --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.208" accept", 允许192.168.2.208主机的所有流量
# firewall-cmd --add-rich-rule="rule family="ipv4" source address="192.168.2.208" protocol value="icmp" accept", 允许192.168.2.208主机的icmp协议，即允许192.168.2.208主机ping
# firewall-cmd --zone=drop --remove-rich-rule="rule family="ipv4" source address="192.168.2.208" accept", 取消允许192.168.2.208主机的所有流量
# firewall-cmd --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.208" service name="ssh" accept", 允许192.168.2.208主机访问ssh服务
# firewall-cmd --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.208" service name="https" reject", 禁止192.168.2.208访问https服务，并返回错误信息
# 注：如果是drop的话是直接丢弃，会返回timeout（连接超时）
# firewall-cmd --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.0/24" port protocol="tcp" port="22" accept", 允许192.168.2.0/24网段的主机访问22端口
# firewall-cmd --add-rich-rule="rule service name=ftp limit value=2/m accept", 每分钟允许2个新连接访问ftp服务
# firewall-cmd --add-rich-rule="rule service name=ftp log limit value="1/m" audit accept", 允许新的ipv4和ipv6连接ftp，并使用日志和审核，每分钟允许访问一次
# firewall-cmd --add-rich-rule="rule family=ipv4 source address=192.168.2.0/24 reject" --timeout=10, 拒绝来自192.168.2.0/24网段的连接，10秒后自动取消
# firewall-cmd --add-rich-rule="rule family=ipv6 source address="2001:db8::/64" service name="dns" audit limit value="1/h" reject" --timeout=300,允许ipv6地址为2001:db8::/64子网的主机访问dns服务，并且每小时审核一次，300秒后自动取消
# firewall-cmd --zone=drop --add-rich-rule="rule family=ipv4 source address=192.168.2.0/24 forward-port port=80 protocol=tcp to-port=22", 将来自192.168.2.0/24网段访问本机80端口的流量转发到本机的22端口
# firewall-cmd --zone=drop --add-rich-rule="rule family=ipv4 source address=192.168.2.0/24 forward-port port=80 protocol=tcp to-port=22 to-addr=192.168.2.208", 将来自192.168.2.0/24网段访问本地80端口的流量转发到192.168.2.208主机的22端口
# firewall-cmd --zone=drop --add-masquerade && firewall-cmd --zone=drop --add-rich-rule="rule family=ipv4 source address=192.168.2.0/24 masquerade"伪装，将来自局域网192.168.2.0/24网段访问外网的流量映射为网络出口公网IP，即修改源IP地址

## 脚本
# systemctl stop firewalld
# cp -p /usr/lib/firewalld/zones/drop.xml /etc/firewalld/zones/
# systemctl start firewalld
# firewall-cmd --set-default-zone=drop
# firewall-cmd --permanent --zone=drop --change-interface=ens32
# firewall-cmd --permanent --zone=drop --add-service=https
# firewall-cmd --permanent --zone=drop --add-protocol=icmp
# firewall-cmd --permanent --zone=drop --add-masquerade
# firewall-cmd --permanent --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.208" port protocol="tcp" port="5210" accept"
# firewall-cmd --permanent --zone=drop --add-rich-rule="rule family="ipv4" source address="192.168.2.206" port protocol="tcp" port="5210" accept"
# firewall-cmd --permanent --zone=drop --add-rich-rule="rule family="ipv4" source address="116.226.230.115" port protocol="tcp" port="8023" accept"
# firewall-cmd --reload
