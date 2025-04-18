#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-09
## 检查每个主机上的资源情况(只作粗略统计)

GAME_ALIAS="syf"
EXIT_CODE=0
GAME_USER="gamecpp"
MY_PATH=$(cd "$(dirname $0)"; pwd)
LIB_PATH=$(cd ${MY_PATH}; cd ./client; pwd)

help_msg() {
  echo "-h  打印帮助信息"
  echo "使用: sh $0"
  exit ${EXIT_CODE}
}

print_msg() {
  local result=$1
  local ip num mem dsk cpu lod net pro
  ip=$(echo ${result}|awk '{print $1}')
  num=$(echo ${result}|awk '{print $2}'|awk -F':' '{print $2}')
  mem=$(echo ${result}|awk '{print $3}'|awk -F':' '{print $2}')
  dsk=$(echo ${result}|awk '{print $4}'|awk -F':' '{print $2}')
  cpu=$(echo ${result}|awk '{print $5}'|awk -F':' '{print $2}')
  lod=$(echo ${result}|awk '{print $6}'|awk -F':' '{print $2}')
  net=$(echo ${result}|awk '{print $7}'|awk -F':' '{print $2}')
  pro=$(echo ${result}|awk -F':' '{print $NF}')
  if [[ ${num} -gt 6 ]] || [[ ${mem} -lt 2048 ]] || [[ ${dsk} -lt 10240 ]] || [[ ${cpu} -gt 90 ]] || [[ ${lod} -gt 80 ]];then
    printf "\e[31m%-15s %-9s %-9s %-9s %-9s %-9s %-9s %-10s\n\e[0m" "${ip}" "${num}" "${mem}" "${dsk}" "${cpu}" "${lod}" "${net}" "${pro}"
  else
    printf "\e[32m%-15s %-9s %-9s %-9s %-9s %-9s %-9s %-10s\n\e[0m" "${ip}" "${num}" "${mem}" "${dsk}" "${cpu}" "${lod}" "${net}" "${pro}"
  fi
}

rev_info() {
  local script
  script=$(ls ${LIB_PATH}|grep "collector")
  printf "%-15s %-9s %-9s %-9s %-9s %-9s %-9s %-10s\n" "IPAdress" "p_num" "f_mem" "f_disk" "cpu_us" "load" "net_con" "p_name"
  for ip in ${ip_list[@]}; do
    scp -rpq ${LIB_PATH}/${script} ${game_user}@${ip}:${remote_script}
    ssh -q -tt ${ip} "sh .bana/collector.sh" && scp -q -p ${GAME_USER}@${ip}:~/col.txt .
    if [[ $? -eq 0 ]]; then
      #result="$(grep -A 6 ${cur_tm} col.txt)"
      result="$(cat col.txt)"
      print_msg "${result}"
    fi
    rm -f ${MY_PATH}/col.txt
  done 
}

main() {
  [[ -f "${MY_PATH}/server/mg.cnf" ]] && source ${MY_PATH}/server/mg.cnf
  if [[ "$1" == "-h" ]] || [[ "$#" != "0" ]]; then
    help_msg    
  fi
  source ./server/mg.cnf
  rev_info
}

main "$@"
