#!/bin/bash

if [ -x /usr/bin/expect ];then
    yum -y install expect
fi

for i in $(cat host.txt);do
   # 获取远程ip地址
   ip=$(echo $i | awk -F":" '{print $1}')
   # 普通用户
   username=$(echo $i | awk -F":" '{print $2}')
   # 普通用户密码
   password=$(echo $i | awk -F":" '{print $3}')
   # root密码
   rootpass=$(echo $i | awk -F":" '{print $4}')
   # 上传脚本
   expect put_script.exp ${ip} ${username} ${password} ${rootpass}
   # 登录执行
   expect sh_cript.exp
   # 获取结果
   expect get_result.exp
   # 清理上传的脚本和结果
   expect del_data.exp
done
