#!/bin/bash

# centos 7 docker安装，主机初始化

# 备份yum源
cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
# 更换yum源
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
#刷新yum源缓存
yum makecache
# 更新系统
yum update -y --exclud=kernel*
# 安装所需的基础软件
yum install -y yum-utils device-mapper-persistent-data lvm2
# 安装yum源
cd /etc/yum.repos.d/ && yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 安装docker-ce
yum makecache fast
yum install -y docker-ce
# 设置开机启动
systemctl enable --now docker
systemctl start docker
docker info