#!/bin/bash

## 作者: Sseve
## 日期: 2021-08-28

DUMP_CMD="/usr/bin/mysqldump"
LOAD_CMD="/usr/bin/mysql"
SQL_HOST="101.132.245.153"
SQL_PORT=3306
SQL_USER="yunwei"
SQL_PASS="yunwei123"
EX_CODE=1
BAK_DIR="/data/back/"
GAME_DIR="/data/game/"
GAME_ALIAS="syf"

help_msg() {
  printf " ** 请在关服的情况下使用该脚本.\n"
  printf " ** 该脚本用于游戏合服\n"
  printf " ** %-20s %-20s\n" "-h|--help" "帮助信息"
  printf " ** %-20s %-20s\n" "-a|--agent" "平台名"
  printf " ** %-20s %-20s\n" "-d|--dest" "目标区服"
  printf " ** %-20s %-20s\n" "-s|--source" "源区服"
  printf " ** Usage: sh $0 -a syf_dev -d 1000 -s 1001\n"
}

ck_env() {
  if [[ ! -x "${DUMP_CMD}" ]] || [[ ! -x "${LOAD_CMD}" ]]; then
    echo "MySQL备份和导入工具不存在"
    exit ${EX_CODE}
  fi
  if [[ ! -d "${BAK_DIR}" ]]; then
    mkdir -p ${BAK_DIR}
  fi    
}
 
bakup_data() {
  echo -e "\033[32m正在备份源区数据库...\033[0m"
  local current_time
  current_time=$(date +%Y%m%d%H%M%S)
  ## backup source zone data
  ${DUMP_CMD} -h ${SQL_HOST} -P ${SQL_PORT} -u ${SQL_USER} -p${SQL_PASS} syf_syf_vie_test_${SourceZone} > ${BAK_DIR}back_pre_combine_${agent}_${SourceZone}_${current_time}.sql 2>/dev/null
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m备份源区数据库 ${agent}_${SourceZone} 成功.\033[0m"
  else
    echo -e "\033[31m备份源区数据库 ${agent}_${SourceZone} 失败.\033[0m"
    exit ${EX_CODE}
  fi
  echo -e "\033[32m正在备份目标区数据库...\033[0m"
  ${DUMP_CMD} -h ${SQL_HOST} -P ${SQL_PORT} -u ${SQL_USER} -p${SQL_PASS} syf_syf_vie_test_${DistZone} > ${BAK_DIR}back_pre_combine_${agent}_${DistZone}_${current_time}.sql 2>/dev/null
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m备份目标区数据库 ${agent}_${DistZone} 成功.\033[0m"
  else
    echo -e "\033[31m备份目标区数据库 ${agent}_${DistZone} 失败\033[0m"
    exit ${EX_CODE}
  fi
}
 
dump_source_data() {
  echo -e "\033[32m正在导出源区数据...\033[0m"
  ${DUMP_CMD} -h ${SQL_HOST} -P ${SQL_PORT} -u ${SQL_USER} -p${SQL_PASS} -t -c syf_syf_vie_test_${SourceZone} > ${BAK_DIR}${agent}_${SourceZone}.sql 2>/dev/null
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m导出源区数据 ${agent}_${SourceZone} 成功.\033[0m"
  else
    echo -e "\033[31m导出源区数据 ${agent}_${SourceZone} 失败.\033[0m"
    exit ${EX_CODE}
  fi
}

##
combine_zone() {
  echo -e "\033[32m正在将源区数据导入目标区...\033[0m"
  ${LOAD_CMD} -h ${SQL_HOST} -P ${SQL_PORT} -u${SQL_USER} -p${SQL_PASS} -D syf_syf_vie_test_${DistZone} < ${BAK_DIR}${agent}_${SourceZone}.sql 2>/dev/null
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m导入 ${agent}_${SourceZone} 到 ${agent}_${DistZone} 成功.\033[0m"
  else
    echo -e "\033[31m导入 ${agent}_${SourceZone} 到 ${agent}_${DistZone} 失败.\033[0m"
    exit ${EX_CODE}
  fi
}

remove_file() {
  sip=$(sh ./client/serve_msg.sh -f serverIp -a ${agent} -z ${SourceZone} -g ${GAME_ALIAS})
  ssh -q -tt ${sip} "cd ${GAME_DIR}${GAME_ALIAS}${agent}_${SourceZone} && rm gameserv${SourceZone} && echo 删除gameserv${SourceZone}成功. || 删除gameserv${SourceZone}失败."
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m合服完成.\033[0m"
  else
    echo -e "\033[31m合服未完成.\033[0m"
  fi 
  sh ./client/serve_msg.sh -f isCombined -v 1 -a ${agent} -z ${SourceZone} -g ${GAME_ALIAS} -t update
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m数据库更新成功.\033[0m"   
  else
    echo -e "\033[32m数据库更新失败.\033[0m"
  fi    
}

main() {
  ck_env
  if [[ $# -ne 6 ]];then
    help_msg
    exit ${EX_CODE}
  fi
  if [[ "$1" = "-a" ]] && [[ "$3" = "-d" ]] && [[ "$5" = "-s" ]]; then
    local agent=$2
    local DistZone=$4
    local SourceZone=$6
    read -e -p "请再次输入平台名: " aagent
    if [[ "${agent}" != "${aagent}" ]]; then
      echo -e "\033[31m两次输入的平台名不一致!!!\033[0m"
      exit ${EX_CODE}
    fi
    read -e -p "请再次输入目标区服: " adest
    if [[ "${DistZone}" != "${adest}" ]]; then
      echo -e "\033[31m两次输入的目标区服不一致!!!\033[0m"
      exit ${EX_CODE}
    fi
    read -e -p "请再次输入源区服: " asource
    if [[ "${SourceZone}" != "${asource}" ]]; then
      echo -e "\033[31m两次输入的源区服不一致!!!\033[0m"
      exit ${EX_CODE}
    fi
    bakup_data
    if [[ $? -ne 0 ]]; then
      exit ${EX_CODE}
    fi
    dump_source_data
    if [[ $? -ne 0 ]]; then
      exit ${EX_CODE}
    fi
    combine_zone
    if [[ $? -ne 0 ]]; then
      exit ${EX_CODE}
    fi
  else
    help_msg
  fi
  echo -e "\033[32m平台${agent}: 源区服${SourceZone} => 目标区服${DistZone} 成功.\033[0m"
  remove_file
}

main "$@"

