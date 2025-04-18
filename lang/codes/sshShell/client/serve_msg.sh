#!/bin/bash

## 作者: Sseve
## 日期: 2021-08-30
## 获取|更新区服信息

DB_USER="yunwei"
DB_PASS="yunwei123"
DB_URL="101.132.245.153"
DB_PORT=3306
DB_NAME="banams"
RIGHT_EXIT=0
ERROR_EXIT=1

help_msg() {
  printf "[*] Usage: sh $0 -f agent,serverId,serverIp -a syf_dev -z 1 -g syf t [query|update]\n"
  printf "[*] %-5s %-5s\n" "-h" "帮助信息"
  printf "[*] %-5s %-5s\n" "-f" "字段"
  printf "[*] %-5s %-5s\n" "-v" "字段值"
  printf "[*] %-5s %-5s\n" "-a" "平台名"
  printf "[*] %-5s %-5s\n" "-z" "区服"
  printf "[*] %-5s %-5s\n" "-g" "gameAlias"
  printf "[*] %-5s %-5s\n" "-t" "执行何种操作[query|update]"  
  exit ${RIGHT_EXIT}
}

query_data() {
  local qparament=$1
  local agent=$2
  local zone=$3
  local galias=$4
  local parament
  local sql
  parament=$(echo ${qparament}|sed 's/,/, /g')
  sql="
    SELECT ${parament} FROM serve_msg WHERE agent='${agent}' AND serverId=${zone} AND gameAlias='${galias}' ORDER BY id;
    "
  result=$(mysql -h ${DB_URL} -P ${DB_PORT} -u${DB_USER} -p${DB_PASS} -D ${DB_NAME} -e "${sql}" -A -N 2>/dev/null)
  echo ${result}
}

update_data() {
  local qparament=$1
  local value=$2
  local agent=$3
  local zone=$4
  local galias=$5
  local sql
  sql="
    UPDATE serve_msg SET ${qparament}='${value}' WHERE agent='${agent}' AND serverId=${zone} AND gameAlias='${galias}';
    "
  mysql -h ${DB_URL} -P ${DB_PORT} -u${DB_USER} -p${DB_PASS} -D ${DB_NAME} -e "${sql}" >/dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    echo "更新字段${qparament}成功."
  else
    echo "更新字段${qparament}失败!"
  fi
}

main() {
  if [[ $# -eq 8 ]] && [[ "$1" = "-f" ]] && [[ "$3" = "-a" ]] && [[ "$5" = "-z" ]] && [[ "$7" = "-g" ]]; then
    local qparament=$2
    local agent=$4
    local zone=$6
    local galias=$8
    query_data ${qparament} ${agent} ${zone} ${galias}
  elif [[ $# -eq 12 ]] && [[ "$1" = "-f" ]] && [[ "$3" = "-v" ]] && [[ "$5" = "-a" ]] && [[ "$7" = "-z" ]] && [[ "$9" = "-g" ]]; then
    local qparament=$2
    local value=$4
    local agent=$6
    local zone=$8
    local galias=${10}
    update_data ${qparament} ${value} ${agent} ${zone} ${galias}
  else
    help_msg
  fi
}

main "$@"

