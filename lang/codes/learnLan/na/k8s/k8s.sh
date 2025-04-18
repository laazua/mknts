#!/bin/bash

echo "
    centos7初始化(2G RAM 2core 30G)
    1. 关闭防火墙
    systemctl stop firewall
    systemctl disable firewall

    2. 关闭selinux
    sed -i 's/enforcing/disabled/' /etc/selinux/config
    setenforce 0

    # 关闭swap
    swappoff -a
    sed -ri 's/.*swap.*/#&/' /etc/fstab

    # 根据规划设置主机名
    hostnamectl set-hostname <hostname>

    # 安装docker

    # 根据实际情况部署k8s的各个组件
"