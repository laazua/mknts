#!/bin/bash


## mysql单机多实例安装

## 添加mysql用户和组
# groupadd mysql
# useradd mysql -g mysql

## 下载mysql安装包

## 创建多实例数据目录
# mkdir -p /data/{mysql1,mysql2,mysql3,mysql4}
# chown -R mysql:mysql /data/{mysql1,mysql2,mysql3,mysql4}
# chmod -R 755 /data/mysql

## 初始化不成功安装以下依赖
# yum install -y libaio
# yum install -y numactl

## 初始化实例(--initialize-insecure)
# /usr/local/mysql/bin/mysqld --defaults-file=my.cnf --initialize --user=mysql --basedir=/usr/local/mysql/ --basedir=/data/mysql1
# /usr/local/mysql/bin/mysqld --defaults-file=my.cnf --initialize --user=mysql --basedir=/usr/local/mysql/ --basedir=/data/mysql2
# /usr/local/mysql/bin/mysqld --defaults-file=my.cnf --initialize --user=mysql --basedir=/usr/local/mysql/ --basedir=/data/mysql3
# /usr/local/mysql/bin/mysqld --defaults-file=my.cnf --initialize --user=mysql --basedir=/usr/local/mysql/ --basedir=/data/mysql4

## 启动多实例
# /usr/local/mysql/bin/mysqld_multi --defaults-extra-file=my.cnf --user=mysql start 3306,3307,3308,3309

## 验证
# mysqld_multi --defaults-extra-file=my.cnf report
