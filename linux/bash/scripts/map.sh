#!/bin/bash
#

## 方式一
ips=(
  "1 10.8.0.1"
  "2 10.8.0.2"  
)

for ip in "${ips[@]}";do
    set -- $ip
    echo key: $1 ++++ value: $2
done

## 方式二
declare -A hosts=(
  ["test"]="10.8.0.1"
  ["prod"]="10.8.0.2"
)
# 获取所有键
#echo "${!hosts[@]}"
# 获取所有值
#echo "${hosts[@]}"
for key in "${!hosts[@]}";do
    echo key: $key ++++ value: ${hosts[$key]}
done
