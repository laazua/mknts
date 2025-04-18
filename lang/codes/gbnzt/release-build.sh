#!/bin/bash

if [ ! -x /usr/bin/upx ];then
    echo "upx工具不存在,正在安装..."
    yum install -y upx >/dev/null 2>&1
    if [ $? -ne 0 ];then
        echo "upx安装失败"
        exit 
    fi

fi

# 打包版本
go build -ldflags="-s -w" -o bnzt && upx -9 bnzt && \
echo -e '\033[32mbnzt\033[0m success' || echo 'packed failed'
