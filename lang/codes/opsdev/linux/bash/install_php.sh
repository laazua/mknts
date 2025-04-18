#!/usr/bin/env bash

## centos7 安装php和php-fpm环境


#### 依赖安装
# sudo yum install -y gcc gcc-c++ make autoconf bison re2c libxml2-devel \
#    libcurl-devel libjpeg-devel libpng-devel freetype-devel \
#    libmcrypt-devel openssl-devel mariadb-devel libicu-devel


####
# curl -o ./php-7.2.0.tar.gz https://www.php.net/distributions/php-7.2.0.tar.gz
# tar zxvf php-7.2.0.tar.gz
# cd php-7.2.0
#
# ./configure --prefix=/usr/local/php7.2.0 \
#   --with-config-file-path=/usr/local/php7.2.0/etc \
#   --with-mysqli \
#   --with-pdo-mysql \
#   --with-openssl \
#   --with-zlib \
#   --with-curl \
#   --with-gd \
#   --with-jpeg-dir \
#   --with-png-dir \
#   --with-freetype-dir \
#   --enable-mbstring \
#   --enable-fpm \
#   --with-fpm-user=www \
#   --with-fpm-group=www \
#   --enable-opcache \
#   --enable-sockets \
#   --with-xmlrpc \
#   --with-xsl
#
# make -j$(nproc) && make install
#
# cp php.ini-production /usr/local/php7.2.0/etc/php.ini
# cp sapi/fpm/php-fpm.conf /usr/local/php7.2.0/etc/php-fpm.conf
#
# cat /lib/systemd/system/php-fpm.service
# [Unit]
# Description=The PHP FastCGI Process Manager
# After=network.target
#
# [Service]
# Type=simple
# ExecStart=/usr/local/php7.2.0/sbin/php-fpm --nodaemonize --fpm-config /usr/local/php7.2.0/etc/php-fpm.conf
# ExecReload=/bin/kill -USR2 $MAINPID
# PIDFile=/usr/local/php7.2.0/var/run/php-fpm.pid
#
# [Install]
# WantedBy=multi-user.target
#
# systemctl daemon-reload && systemctl enable php-fpm.service


#### 扩展安装：redis为例
# curl -o ./redis-4.3.0.tgz  https://pecl.php.net/get/redis-4.3.0.tgz
# tar -xf redis-4.3.0.tgz && cd redis-4.3.0
# /usr/local/php7.2.0/bin/phpize   # 这里要给哪个版本的php安装扩展就使对应php版本路径的phpize
# ./configure --with-php-config=/usr/local/php7.2.0/bin/php-config  # 这里同上
# make && make install
# 
# vim /usr/local/php7.2.0/etc/php.ini 添加extension=redis.so
# ;
# ;   extension=mysqli
# extension=redis.so
# ; When the extension library to load is not located in the default extension
# ; directory, You may specify an absolute path to the library file: