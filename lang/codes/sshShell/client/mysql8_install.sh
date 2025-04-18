#!/usr/bin/bash

# mysql init

# 下载mysql二进制安装包mysql-8.0.26-el7-x86_64.tar.gz
# 配置/etc/my.cnf

groupadd mysql
useradd mysql -g mysql
mkdir -p /data/mysql
chown -R mysql:mysql /data/mysql
chmod -R 755 /data/mysql
yum install -y libaio
yum install -y numactl
/usr/local/mysql/bin/mysqld --user=mysql --basedir=/usr/local/mysql/ --datadir=/data/mysql --initialize-insecure

cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld

/etc/init.d/mysql start
