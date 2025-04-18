#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-09
## 收集主机资源使用情况

COL_FILE="/home/gamecpp/col.txt"
IP_FILE="/data/game/myip.txt"
EXIT_CODE=1

help_msg() {
  echo "-h    帮助信息."
  echo "使用: sh $0"
  exit 0
}

### 检查脚本需要的工具是否存在
### 参数: 无
### 返回值: 无
ck_env() {
  if [[ ! -x /usr/bin/bc ]]; then
    yum install -y bc.x86_64 >/dev/null 2>&1
    if [[ $? -ne 0 ]];then
      echo -e "\e[31mbc工具不存在\e[0m"
      exit ${EXIT_CODE}
    fi
  fi
  if [[ ! -x /usr/bin/iostat ]]; then
    yum install -y sysstat.x86_64 >/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
      echo -e "\e[31miostat工具不存在\e[0m"
      exit ${EXIT_CODE}
    fi
  fi
}

### 获取当前主机开服数量
### 参数: 无
##  返回值: 主机开服数量
col_num() {
  local num
  num=$(pgrep -l game|wc -l)
  return ${num}
}

### 获取当前主机内存剩余量
### 参数: 无
### 返回值: 主机内存剩余量
col_mem() {
  local fe
  fe=$(free -h|awk 'NR==2'|awk '{print $7}'|cut -d 'M' -f1)
  return ${fe}
}

### 获取当前主机磁盘剩余量
### 参数: 无
### 返回值: 主机磁盘剩余量
col_dsk() {
  return 2
}

### 获取当前主机cpu使用百分比
### 参数: 无
### 返回值: cpu使用百分比
col_cpu() {
  local us
  local sy
  local su
  us=$(top -bn 1 -i -c|awk 'NR==3'|awk '{print $2}')
  sy=$(top -bn 1 -i -c|awk 'NR==3'|awk '{print $4}')
  su=$(echo "${us} + ${sy}"|bc|cut -d '.' -f1)
  return ${su}
}

### 获取已经建立网络连接数量
### 参数: 无
### 返回值: 无
col_net() {
  local ne
  ne=$(netstat -na|grep ESTABLISHED|wc -l)
  return ${ne}
}
### 获取当前主机load情况
### 参数: 无
### 返回值: load值
col_lod() {
  local lod
  lod=$(top -bn 1 -i -c|awk 'NR==1'|awk '{print $13}'|cut -d '.' -f1)
  return ${lod}
}
### 收集主机进程名
### 参数无
### 返回值无
col_pro() {
  pro="$(pgrep -l game|awk '{print $2}')"
  echo ${pro}
}

### 将获取的信息写入文件
### 参数: 无
### 返回值: 无
wrt_val() {
  local ip
  ip=$(cat ${IP_FILE})
  echo "${ip}" >> ${COL_FILE}
  col_num
  echo "num:$?" >> ${COL_FILE}
  col_mem
  echo "mem:$?" >> ${COL_FILE}
  col_dsk
  echo "dsk:$?" >> ${COL_FILE}
  col_cpu
  echo "cpu:$?" >> ${COL_FILE}
  col_lod
  echo "lod:$?" >> ${COL_FILE}
  col_net
  echo "net:$?" >> ${COL_FILE}
  echo -n "pro:" >> ${COL_FILE}
  col_pro >> ${COL_FILE}
}

### 脚本入口
### 参数: 无
### 返回值: 无
main() {
  if [[ "$1" = "-h" ]]; then
    help_msg
  fi
  >${COL_FILE}
  wrt_val
 # cat /home/gamecpp/col.txt
}

main "$@"

