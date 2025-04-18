#!/usr/bin/env bash

## centos7 安装mysql5.7


#### 系统环境初始化
# 关闭selinux和防火墙
# 修改I/O调度模式为deadline
# swap分区设置
# 建议选择xfs文件系统
# 操作系统限制(ulimit -a)


#### 安装mysql
# wget https://cdn.mysql.com/archives/mysql-5.7/mysql-5.7.44-el7-x86_64.tar.gz
# tar -xf mysql-5.7.44-el7-x86_64.tar.gz -C /usr/local/mysql5.7 && ln -s /usr/local/mysql5.7 /usr/local/mysql
# groupadd mysql
# useradd  -g mysql mysql -s /sbin/nologin
# mkdir -p /data/mysql
# chown mysql:mysql -R /data/mysql
# chown mysql:mysql -R /usr/local/mysql
# 初始化: /usr/local/mysql/bin/mysql_install_db --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql --datadir=/data/mysql/ --user=mysql
# 更改密码进入: /usr/local/mysql/bin/mysqld_safe --defaults-file=/etc/my.cnf --skip-grant-tables
# mysql> use mysql;
# mysql> UPDATE user SET authentication_string=PASSWORD('123456') WHERE User='root';


#### 运行
# cat /lib/systemd/system/mysql.service 
# [Unit]
# Description=MySQL Community Server
# Documentation=man:mysqld(8)
# After=network.target

# [Service]
# Type=simple
# User=mysql
# Group=mysql
# ExecStart=/usr/local/mysql/bin/mysqld_safe --defaults-file=/etc/my.cnf
# ExecStop=/usr/local/mysql/bin/mysqladmin shutdown
# LimitNOFILE=5000
# TimeoutSec=600

# [Install]
# WantedBy=multi-user.target

# systemctl daemon-reload && systemctl enable mysql && systemctl start mysql