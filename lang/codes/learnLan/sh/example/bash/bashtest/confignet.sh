#!/bin/bash
# this script used to config vmware host of centos7
# the value how to set reference the env of local area network
#### vmware network adapter select Bridge mode.

echo "BOOTPROTO=static" > /etc/sysconfig/network-scripts/ifcfg-ens33
echo "DEVICE=ens33" >> /etc/sysconfig/network-scripts/ifcfg-ens33
echo "ONBOOT=yes" >> /etc/sysconfig/network-scripts/ifcfg-ens33
echo "IPADDR=192.168.5.131" >> /etc/sysconfig/network-scripts/ifcfg-ens33
echo "GATEWAY=192.168.5.254" >> /etc/sysconfig/network-scripts/ifcfg-ens33
echo "NETMASK=255.255.255.0" >> /etc/sysconfig/network-scripts/ifcfg-ens33 
echo "DNS=192.168.5.149" >> /etc/sysconfig/network-scripts/ifcfg-ens33

echo "nameserver 192.168.5.149" > /etc/resolv.conf

systemctl restart network

ping baidu.com -c 1

if [ $? -eq 0 ];then
    yum install -y yum-fastestmirror
    yum install -y vim
    yum install -y net-tools.x86_64
    exit
else
    echo "config network failed."
    exit 
fi
