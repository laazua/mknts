#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-07
## 游戏进程监控

DATE=$(date "+%Y-%m-%d %H:%M:%S")
IP=$(curl ip.sb)
GAME_PATH="/data/gameserv/"
WEB_URL="https://oapi.dingtalk.com/robot/send?access_token=db7054b9a5c5a8fb1fe441f36044cf13d0cbc707ee963b0ab85526e06c5c9a70"
KEY="SYF"
GAME_ALIAS="syf"

send_msg() {
  local msg=$1
  curl -s ${WEB_URL} -H "Content-Type: application/json" -d "${msg}"
}

ck_pros() {
  local game_dirs
  game_dirs=$(ls -l ${GAME_PATH} | egrep -o "[a-zA-Z_]*_[0-9]*")
  for gd in ${game_dirs[@]};do
    zone=$(echo ${gd}|awk -F'_' '{print $3}')
    if [[ -f "${GAME_PATH}${gd}/gameserv${zone}" ]]; then
      pd=$(cat ${GAME_PATH}${gd}/tmp/gameserv.pid)
      if [[ -n "${pd}" ]]; then
        rd=$(pgrep -a game|grep -o ${pd})
        if [[ ! -n "${rd}" ]]; then
          send_msg "{\"msgtype\": \"text\",\"text\": {\"content\": \"${IP} ${DATE} ${KEY} ${gd} stopped!\"}}"
          cd ${GAME_PATH}${gd} && sudo -u gamecpp sh games.sh start
          sleep 1
          rt=$(pgrep -a game|grep -o ${zone})
          if [[ "${rt}" ]]; then
            send_msg "{\"msgtype\": \"text\",\"text\": {\"content\": \"${IP} ${DATE} ${KEY} ${gd} restarted!\"}}"
          fi
        fi
      fi
    fi
  done
}

ck_pros "$@"
