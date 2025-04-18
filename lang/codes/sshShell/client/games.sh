#!/bin/bash

GAME_PATH=$(cd "$(dirname $0)"; pwd)
PID_FILE=${GAME_PATH}/tmp/gameserv.pid
SERVER_ID=$(ls |grep gameserv|awk -F'v' '{print $2}')

# 检查游戏是否启动
gs_ck() {
  pid=$(cat ${PID_FILE})
  if [[ ${pid} ]] && [[ -L /proc/${pid}/exe ]]; then
    return 1
  else
    > ${PID_FILE}
    return 0
  fi
}

# 启动游戏
gs_st() {
  [[ ! -d ${GAME_PATH}/tmp ]] && mkdir -p ${GAME_PATH}/tmp && touch $PID_FILE
  gs_ck
  if [[ $? -eq 1 ]]; then
    echo -e "\033[31m${GAME_PATH} 运行中!\033[0m"
    return 
  fi
  ${GAME_PATH}/gameserv${SERVER_ID}
  sleep 2
  gs_ck
  if [[ $? -eq 1 ]]; then
    echo -e "\033[32m${GAME_PATH} 启动成功.\033[0m"
  else
    echo -e "\033[31m${GAME_PATH} 启动失败.\033[0m"
  fi
}

# 关闭游戏
gs_sp() {
  pid=$(cat ${PID_FILE})
  if [[ ! -n "${pid}" ]];then
      echo -e "\e[31m${GAME_PATH} 已经关闭.\e[0m"
      return
  fi
  kill -15 ${pid}
  while true; do
    gs_ck
    if [[ $? -eq 0 ]]; then
      break
    fi
  done
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m${GAME_PATH} 关服成功.\033[0m"
  else
    echo -e "\033[32m${GAME_PATH} 关服失败.\033[0m"
  fi
}

# 重启游戏
gs_rs() {
  echo "gameserver restart!!!"
  gs_sp
  gs_st
}

# 检查游戏状态
gs_ss() {
  gs_ck
  if [[ $? -eq 1 ]]; then
    echo -e "\033[31m${GAME_PATH} 运行中.\033[0m"
  else
    echo -e "\033[32m${GAME_PATH} 已关闭.\033[0m"
  fi
  return 0
}

sudo find ${GAME_PATH} -type f -not -name "games*" -exec chmod 644 '{}' \;

case "$1" in
  st)
    gs_st
    ;;
  sp)
    gs_sp
    ;;
  rt)
    gs_rs
    ;;
  ck)
    gs_ss
    ;;
  *)
    echo $"Usage: $0 {st|sp|ck|rt}"
    exit 1
esac

