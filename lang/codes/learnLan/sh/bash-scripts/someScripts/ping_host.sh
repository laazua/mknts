#!/bin/bash

if [ "$#" != "2" ];then
    echo "Usage: ./ping_host.sh 127.0.0.1"
    exit 1
fi

# ping主机状态
for((i=1;i<=3;i++));do
    if ping -c 1 $1 &>/dev/null;then
        export ping_count"$i"=1
    else
        export ping_count"$i"=0
    fi

    sleep 3
done

# 分析结果
if [ $ping_count1 -eq $ping_count2 ] && [ $ping_count2 -eq $ping_count3] && [ $ping_count3 -eq 0 ];then
    echo "$1 挂掉"
elif [ $ping_count1 -eq $ping_count2 ] && [ $ping_count2 -eq $ping_count3] && [ $ping_count3 -eq 1 ];then
    echo "$1 正常"
else
    echo "$1 网络延迟"
fi

# 释放export 变量
unset ping_count1
unset ping_count2
unset ping_count3