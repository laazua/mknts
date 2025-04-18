#!/bin/bash

## 登录远程机器执行任务

EXP="/usr/bin/expect"

if [[ ! -x ${EXP} ]];then
    echo "expect不存在, 请安装: yum install  expect -y"
    exit 0
fi

for i in $(cat ../conf/rhes.cfg);do
    # 远程主机ip地址
    ipAddr=$(echo $i|awk -F':' '{print $1}')
    # 远程主机用户
    userName=$(echo $i|awk -F':' '{print $2}')
    # 远程主机用户密码
    passWord=$(echo $i|awk -F':' '{print $3}')

    # 上传脚本
    ${EXP} ../func/put.exp ${ipAddr} ${userName} ${passWord}
    # 执行上传脚本
    ${EXP} ../func/execute.exp ${ipAddr} ${userName} ${passWord}
    # 获取结果

    # 删除脚本
done
