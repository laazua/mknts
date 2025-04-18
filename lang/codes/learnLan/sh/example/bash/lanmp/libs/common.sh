#!/bin/bash
## 全局变量
USER=$(whoami)
CURDIR=$(pwd)
PKG_DIR="/usr/local/src/"
CORE=$(cat /proc/cpuinfo |grep "cpu cores"|uniq -c|awk '{print $1}')
SRC_URL="http://dl.wdlinux.cn/files/"

## server版本
NGX_VER=("1.2.9" "1.4.7" "1.6.3" "1.8.1" "1.10.3" "1.12.2" "1.14.2" "1.16.1")
MYS_VER=("5.5.62" "5.6.42" "5.7.25" "8.0.14")
PHP_VER=("5.3.29" "5.4.45" "5.5.38" "5.6.38" "7.1.25" "7.2.26" "7.3.13")
APA_VER=("2.2.34" "2.4.41")

PCR_VER=("8.38")

## nginx configure
NUSER="www"
NNUM=$(cat /etc/passwd|grep "www")
## apache configure


## mysql configure
MUSER="mysql"
MNUM=$(cat /etc/passwd|grep "mysql")
