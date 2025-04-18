#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-03
## 描述: 操作客户端脚本

MY_PATH=$(cd "$(dirname $0)"; pwd)
LIB_PATH=$(cd ${MY_PATH}; cd ../client; pwd)
GAME_ALIAS="syf"
GAME_DIR="/data/game/"
RIGHT_EXIT=0
ERROR_EXIT=1
THREAD_NUM=4
TMP_FIFO="/tmp/$$.fifo"
FD=6

########################
# 此脚本的帮助函数
# 全局变量:
#   无
# 参数:
#   无
# 返回值:
#   无
#######################
help_msg() {
  echo "#######################################################"
  echo "-h         打印帮助信息."
  echo
  echo "######################开服使用说明#####################"
  echo "-i         IP地址"
  echo "-a         平台名"
  echo "-z         区服ID"
  echo "usage:sh $0 -i 127.0.0.1 -a dev_syf -z 1015"
  echo
  echo "########################全服操作#######################"
  echo "-t         [start|stop|update|check]启动|关闭|更新|检查"
  echo "usage:sh $0 -t check"
  echo
  echo "#######################离散服操作######################"
  echo "-a         平台名"
  echo "-z         区服ID[1015,1016,1018]"
  echo "-t         [start|stop|update|check]启动|关闭|更新|检查"
  echo "usage: sh $0 -a dev_syf -z 1015,1018 -t check"
}

#################################
# 在远程机器上开服
# 全局变量:
#   无
# 参数:
#   ip: 开服ip
#   agent: 开服平台
#   zone: 开服id
#   cms: 远程机器上运行的开服脚本
# 返回值:
#   无
################################
open_serve() {
  local ip=$1
  local agent=$2
  local zone=$3
  local cms=$4
  ret=$(sh ../client/serve_msg.sh -f serverId -a ${agent} -z ${zone} -g ${GAME_ALIAS})
  if [ ! "${ret}" ]; then
    ssh -q -tt ${ip} "sh ${remote_script}${cms} ${agent} ${zone}"
  else
    echo -e "\033[31m平台:${agent} 区服:${zone}已经存在\033[0m"
    exit ${ERROR_EXIT}
  fi
}

#############################
# 操作所有运行区服
# 全局变量:
#   无
# 参数:
#   opt: 执行何种操作
#   cms: 远程主机上执行的脚本
# 返回值:
#   无
############################
all_zones_opt() {
  local opt=$1
  local cms=$2
  # 新建一个FIFO类型的文件
  mkfifo ${TMP_FIFO}
  # 将FD=6的文件描述符指向TMP_FIFO
  exec 6<>${TMP_FIFO}
  # 在FD=6中放入回车符号(启动进程个数为:THREAD_NUM)
  for ((i=0;i<${THREAD_NUM};i++));do echo; done >&6
  if [[ "${opt}" ]]; then
    for ip in ${ip_list[@]}; do
      read -u6
      {
        ssh -q -tt ${ip} "sh ${remote_script}${cms} ${opt}"
      }&
    done
  fi
  # 等待所有进程退出
  wait
  # 关闭文件描述符FD=6,并删除管道文件TMP_FIFO
  exec 6>&-
  rm -f ${TMP_FIFO}
}

###########################
# 操作离散服
# 全局变量:
#   ip_list
# 参数:
#   agent: 平台名
#   zones: 区服列表
#   tg: 执行何种操作
#   cms: 远程主机执行的脚本
###########################
some_zones_opt() {
  local agent=$1
  local zs=$2
  local tg=$3
  local cms=$4
  zones=$(echo ${zs}|sed 's/,/ /g')
  local i=0
  declare ips
  for zone in ${zones[@]}; do
    ips[${i}]=$(sh ../client/serve_msg.sh -f serverIp -a ${agent} -z ${zone} -g syf)
    i=$(($i+1))
  done
  ips=($(echo ${ips[@]}| sed 's/ /\n/g' | sort|uniq))
  for ip in ${ips[@]};do
    ssh -q -tt ${ip} "sh ${remote_script}${cms} ${agent} ${zs} ${tg}"   
  done
}


main() {
  ## 脚本入口
  # 加载配置文件
  [[ -f "${MY_PATH}/mg.cnf" ]] && source ${MY_PATH}/mg.cnf

  ## 开服操作
  if [[ "$#" = "6" ]] && [[ "$1" = "-i" ]] && [[ "$3" = "-a" ]] && [[ "$5" = "-z" ]]; then
    echo -e "\033[32m=========参数确认==========\033[0m"
        
    read -e -p "请再次确认ip:" aip
    if [[ "${2}" != "${aip}" ]]; then
      echo -e "\033[31mIP不一致!!!\033[0m"
      exit ${ERROR_EXIT}
    fi

    read -e -p "请再次确认平台名:" aagent
    if [[ "${4}" != "${aagent}" ]]; then
      echo -e "\033[31m平台名不一致!!!\033[0m"
      exit ${ERROR_EXIT}
    fi

    read -e -p "请再次确认区服:" azone
    if [[ "${6}" != "${azone}" ]]; then
      echo -e "\033[31m区服ID不一致!!!\033[0m"
      exit ${ERROR_EXIT}
    fi

    local script=$(ls ${LIB_PATH}|grep "open_serve")
    # 上传脚本
    scp -rpq ${LIB_PATH}/${script} ${LIB_PATH}/client_cnf.sh ${game_user}@${aip}:${remote_script}

    echo -e "\033[32m===========================\033[0m"
    open_serve ${aip} ${aagent} ${azone} ${script}
    ## 全服启动|关闭|更新|检查
  elif [[ "$#" = "2" ]] && [[ "$1" = "-t" ]]; then
    local script=$(ls ${LIB_PATH}|grep "all_zones")
    for ip in ${ip_list[@]}; do
      scp -rpq ${LIB_PATH}/${script} ${LIB_PATH}/client_cnf.sh ${game_user}@${ip}:${remote_script}
    done
    all_zones_opt $2 ${script}
  ## 离散服操作
  elif [[ "$#" = "6" ]] && [[ "$1" = "-a" ]] && [[ "$3" = "-z" ]] && [[ "$5" = "-t" ]]; then
    local script=$(ls ${LIB_PATH}|grep "some_zones")
    # 上传脚本
    for ip in ${ip_list[@]}; do
      scp -rpq ${LIB_PATH}/${script} ${LIB_PATH}/client_cnf.sh ${game_user}@${ip}:${remote_script}
    done
    if [[ $? -eq 0 ]]; then
      some_zones_opt $2 $4 $6 ${script}
    fi
  else
    help_msg
  fi
}

main "$@"

