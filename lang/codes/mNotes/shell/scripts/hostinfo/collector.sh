#!/bin/bash

## 主机资源采集

current_path=$(cd "$(dirname $0)";pwd)
collect_file="$current_path/col.txt"

## 业务进程数量
col_zone_num() {
    local num=$(pgrep -l gameserv|wc -l)
    echo "num:${num}" >> ${collect_file}
}

## 内存剩余
col_host_mem() {
    local mem=$(free -h|awk 'NR==2'|awk '{print $7}'|cut -d 'M' -f1)
    echo "mem:${mem}" >> ${collect_file}
}

## 磁盘剩余 
col_host_dsk() {
    local dsk=$(df -h|grep '/data'|awk '{print $4}')
    echo "dsk:${dsk}" >> ${collect_file}
}

## cpu使用情况
col_host_cpu() {
    local us=$(top -bn 1 -i -c|awk 'NR==3'|awk '{print $2}')
    local sy=$(top -bn 1 -i -c|awk 'NR==3'|awk '{print $4}')
    local sum=$(echo "${us} + ${sy}"|bc|cut -d '.' -f1)
    echo "cpu:${sum}" >> ${collect_file}
}

## 网络连接数量
col_host_con() {
    local con=$(netstat -na|grep ESTABLISHED|wc -l)
    echo "con:${con}" >> ${collect_file}
}

## 主机负载
col_host_lod() {
    local lod=$(w|grep load|awk '{print $12}')
    echo "lod:${lod}" >> ${collect_file}
}

## 清空收集文件
>${collect_file}
echo "ip:10.0.0.16" >> ${collect_file}
col_zone_num
col_host_mem
col_host_dsk
col_host_cpu
col_host_con
col_host_lod
