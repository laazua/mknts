#!/bin/bash

## author: Sseve
## date: 2021-08-25
## stop|start|update game
## game host script dir: /home/gamecpp/.bana/

MY_PATH=$(cd "$(dirname $0)"; pwd)
source ${MY_PATH}/client_cnf.sh
GAME_DIRS=($(ls -l ${GAME_PATH} | egrep -o "[a-zA-Z_]*_[0-9]*"))
ERROR_EXIT=1
THREAD_NUM=4
TMP_FIFO="/tmp/$$.fifo"

multi_thread() {
  local opt=$1
  # 新建一个FIFO类型的文件
  mkfifo ${TMP_FIFO}
  # 将FD=6的文件描述符指向TMP_FIFO
  exec 6<>${TMP_FIFO}
  # 在FD=6中放入回车符号(启动进程个数为:THREAD_NUM)
  for((i=0;i<${THREAD_NUM};i++)); do echo; done >&6
  for gd in ${GAME_DIRS[@]}; do
    read -u6
    {
        gs_op ${gd} ${opt}
        echo >&6
    }&
  done
  wait
  # 关闭文件描述符FD=6,并删除管道文件TMP_FIFO
  exec 6>&-
  rm -f ${TMP_FIFO}
}

gs_op() {
  local gd=$1
  local op=$2
  zone=$(echo ${gd}|awk -F'_' '{print $3}')
  if [[ -f "${GAME_PATH}${gd}/gameserv${zone}" ]]; then
    if [[ "${op}" != "update" ]];then
      wrt_log "cd ${GAME_PATH}${gd} && sh game_opt.sh ${op}"
      cd ${GAME_PATH}${gd} && sh game_opt.sh ${op}
    else
      wrt_log "svn --username ${SVN_USER} --password ${SVN_PASS} update ${SVN_URL} ${GAME_PATH}${gd} --force >/dev/null 2>&1"
      svn --username ${SVN_USER} --password ${SVN_PASS} update ${SVN_URL} ${GAME_PATH}${gd} --force >/dev/null 2>&1
      # if [[ $? -eq 0 ]]; then
      #   ck_md5 ${gd} ${zone}
      # else
      #   echo -e "\033[31m${GAME_PATH}${gd} svn export失败!\033[0m"
      # fi 
      # python checkFile.py "${GAME_PATH}${gd}
      echo "${gd} 更新完成."    
    fi
  fi
}

ck_md5() {
  local gd=$1
  local zone=$2
  cd ${GAME_PATH}${gd} && python svn_game_md5.py >/dev/null 
  if [[ $? -ne 0 ]]; then
    echo -e "\033[31m${GAME_PATH}${gd} 创建md5文件失败!\033[0m"
    exit ${ERROR_EXIT}
  fi
  cat ${GAME_PATH}${gd}/md5.txt | awk -F'/' '{print $NF}'|sort -u >cfmd5.txt
  cat ${GAME_PATH}${gd}/gmd5.txt |awk -F'/' '{print $NF}'|sort -u >gfmd5.txt
  cmd5=$(md5sum ${GAME_PATH}${gd}/cfmd5.txt|awk '{print $1}')
  gmd5=$(md5sum ${GAME_PATH}${gd}/gfmd5.txt|awk '{print $1}')
  if [[ "${cmd5}" = "${gmd5}" ]]; then
    #echo -e "\033[32m${GAME_PATH}${gd} 更新配置成功.\033[0m"
    mv -f gameser-beta gameserv${zone} && sudo chmod +x gameserv${zone}
    if [[ $? -eq 0 ]]; then
      echo -e "\033[32m${GAME_PATH}${gd} 更新成功.\033[0m"
    else
      echo -e "\033[32m${GAME_PATH}${gd} 更新失败.\033[0m"
    fi
    rm -rf ${GAME_PATH}${gd}/*md5.txt
  else
    echo -e "\033[31m${GAME_PATH}${gd} 更新配置失败!\033[0m"
    rm -rf ${GAME_PATH}${gd}/*md5.txt
    exit ${ERROR_EXIT}
  fi
}

main() {
  local op=$1
  if [[ "$#" = "1" ]] && [[ -n "${op}" ]]; then
    wrt_log "all zones: multi_thread ${op}"
    multi_thread ${op}
  else
    echo "Usage: sh $0 [start|stop|check|update] 启动|关闭|更新|检查"
    exit ${ERROR_EXIT}
  fi
}

main "$@"

