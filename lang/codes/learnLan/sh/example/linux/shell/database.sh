#!/bin/bash

# 数据库连接
mysql=$(which mysql)

# 发送单个命令
${mysql} -h ${host} -u ${user} -p -e "show databases;"

# 发送多个命令
${mysql} -h ${host} -u ${user} -p <<EOF
show databases;
select * from test.test;
EOF
