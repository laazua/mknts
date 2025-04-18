#!/bin/bash

## 作者: Sseve
## 日期: 2021-08-30
## 开服

MY_PATH=$(cd "$(dirname $0)"; pwd)
source ${MY_PATH}/client_cnf.sh
EX_CODE=1
IP=$(cat ${GAME_DIR}myip.txt)

help_msg() {
  printf " [*] Usage: sh $0 syf_dev 1\n"
  printf " [*] %-5s %-5s\n" "-h" "help message."
  exit ${EX_CODE}
}

open_serve() {
  local agent=$1
  local zone=$2
  echo -e "\033[32m正在开服 ${agent}: ${zone} ...\033[0m"
  # 创建进程目录
  if [[ ! -d ${GAME_DIR}${GAME_ALIAS}_${agent}_${zone} ]]; then
    sudo mkdir -p ${GAME_DIR}${GAME_ALIAS}_${agent}_${zone}
  else
    echo -e "\033[31m${GAME_DIR}${GAME_ALIAS}_${agent}_${zone}已经存在\033[0m"
    exit ${EX_CODE}
  fi
  # 导出游戏配置及二进制文件
  sudo svn --username ${SVN_USER} --password ${SVN_PASS} checkout ${SVN_URL} ${GAME_DIR}${GAME_ALIAS}_${agent}_${zone} --force >/dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m配置文件准备完毕.\033[0m"
  else
    echo -e "\033[31m配置文件准备失败!\033[0m"
    exit ${EX_CODE}
  fi
  # 更改文件所属用户和组
  sudo chown -R gamecpp:gamecpp ${GAME_DIR}
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m更改${GAME_ALIAS}_${agent}_${zone}所属用户和组成功.\033[0m"
  else
    echo -e "\033[31m更改${GAME_ALIAS}_${agent}_${zone}所属用户和组失败!\033[0m"
    exit ${EX_CODE}
  fi

  # 更改文件权限
  sudo chmod -R 644 ${GAME_DIR}${GAME_ALIAS}_${agent}_${zone}
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m${GAME_ALIAS}_${agent}_${zone}下文件权限更改成功.\033[0m"
  else
    echo -e "\033[31m${GAME_ALIAS}_${agent}_${zone}下文件权限更改失败!\033[0m"
    exit ${EX_CODE}
  fi
}

serv_msg_into_db() {
  local sql
  sql="
    INSERT INTO serve_msg(gameAlias, agent, serverId, serverIp, gamePort, gameDbUrl, gameDbPort, gameDbName, gameDir, isCombined, backEndVersion)
      VALUES('${GAME_ALIAS}', '${agent}', ${zone}, '${IP}', 3306, '${IP}', 3306, '${GAME_ALIAS}_${agent}_${zone}', '${GAME_DIR}${GAME_ALIAS}_${agent}_${zone}', 0, 0);
    "
  #echo ${sql}
  wrt_log "/usr/local/mysql/bin/mysql -h ${DB_URL} -P ${DB_PORT} -u${DB_USER} -p"${DB_PASS}" -D ${DB_NAME} -e "${sql}" -A -N >/dev/null 2>&1"
  /usr/local/mysql/bin/mysql -h ${DB_URL} -P ${DB_PORT} -u${DB_USER} -p"${DB_PASS}" -D ${DB_NAME} -e "${sql}" -A -N >/dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    echo -e "\033[32m区服信息写入数据库成功.\033[0m"
  else
    echo -e "\033[31m区服信息写入数据库失败.\033[0m"
  fi
}

main() {
  if [[ $# -eq 2 ]] && [[ -n  "$1" ]] && [[ -n "$2" ]]; then
    local agent=$1
    local zone=$2
    wrt_log "open zone: open_serve ${agent} ${zone}"
    open_serve ${agent} ${zone} 
  else
    help_msg
  fi
  serv_msg_into_db
}

main "$@"
