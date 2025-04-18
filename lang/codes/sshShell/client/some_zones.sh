#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-06
## 离散区服操作[关闭|更新|启动|检查]

MY_PATH=$(cd "$(dirname $0)"; pwd)
# 添加配置
source ${MY_PATH}/client_cnf.sh
RIGHT_EXIT=0
ERROR_EXIT=1
THREAD_NUM=4
TMP_FIFO="/tmp/$$.fifo"

help_msg() {
  echo "useage: sh $0 agent zones target"
  echo "agent    平台名"
  echo "zones    区服列表"
  echo "target   执行的动作[start|stop|update|check]"
}

ck_md5() {
  local gd=$1
  cd ${GAME_PATH}${gd} && python svn_game_md5.py >/dev/null 
  if [[ $? -ne 0 ]]; then
    echo -e "\033[31m${GAME_PATH}${gd} 创建md5文件失败!\033[0m"
    exit ${ERROR_EXIT}
  fi
  cat ${GAME_PATH}${gd}/md5.txt |awk -F'/' '{print $NF}'|sort -u >cfmd5.txt
  cat ${GAME_PATH}${gd}/gmd5.txt |awk -F'/' '{print $NF}'|sort -u >gfmd5.txt
  cmd5=$(md5sum ${GAME_PATH}${gd}/cfmd5.txt|awk '{print $1}')
  gmd5=$(md5sum ${GAME_PATH}${gd}/gfmd5.txt|awk '{print $1}')
  if [[ "${cmd5}" = "${gmd5}" ]]; then
    echo -e "\033[32m${GAME_PATH}${gd} 更新成功.\033[0m"
    rm -rf ${GAME_PATH}${gd}/*md5.txt
  else
    echo -e "\033[31m${GAME_PATH}${gd} 更新失败!\033[0m"
    rm -rf ${GAME_PATH}${gd}/*md5.txt
    exit ${ERROR_EXIT}
  fi
}

multi_thread() {
  local agent=$1
  local zs=$2
  local op=$3
  zones=$(echo ${zs}|sed 's/,/ /g')
  # 新建一个FIFO类型的文件
  mkfifo ${TMP_FIFO}
  # 将FD=6的文件描述符指向TMP_FIFO
  exec 6<>${TMP_FIFO}
  # 在FD=6中放入回车符号(启动进程个数为:THREAD_NUM)
  for((i=0;i<${THREAD_NUM};i++)); do echo; done >&6
  for zone in ${zones[@]}; do
    read -u6
    {
      gs_op ${agent} ${zone} ${op}
      echo >&6
    } &
  done
  wait
  # 关闭文件描述符FD=6,并删除管道文件TMP_FIFO
  exec 6>&-
  rm -f ${TMP_FIFO}
}

gs_op() {
  local agent=$1
  local zone=$2
  local tg=$3
  z=$(ls -l ${GAME_PATH} |egrep -o "[a-zA-Z_]*_[0-9]*"|grep "${agent}_${zone}")
  if [[ -f "${GAME_PATH}${z}/gameserv${zone}" ]]; then
    if [[ "${tg}" != "update" ]]; then
      wrt_log "cd ${GAME_PATH}${z} && sh game_opt.sh ${tg} && exit ${RIGHT_EXIT}"
      cd ${GAME_PATH}${z} && sh game_opt.sh ${tg} && exit ${RIGHT_EXIT}   
    else
      wrt_log "svn --username ${SVN_USER} --password ${SVN_PASS} export ${SVN_URL} ${GAME_PATH}${z} --force >/dev/null 2>&1"
      svn --username ${SVN_USER} --password ${SVN_PASS} export ${SVN_URL} ${GAME_PATH}${z} --force >/dev/null 2>&1
      # if [[ $? -eq 0 ]]; then
      #   ${z}ck_md5
      # else
      #   echo -e "\033[31m导出版本库文件失败.\033[0m"
      # fi
      echo "${z} 更新完成"
    fi
  fi
}

main() {
  if [[ "$#" = 3 ]] && [[ -n "$1" ]] && [[ -n "$2" ]] && [[ "$3" = "start" ]] || [[ "$3" = "stop" ]] || [[ "$3" = "check" ]] || [[ "$3" = "update" ]]; then
    wrt_log "some zones: multi_thread $1 $2 $3"
    multi_thread $1 $2 $3
  else
    help_msg
  fi
  exit ${RIGHT_EXIT}
}


main "$@"

