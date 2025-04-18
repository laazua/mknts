#!/bin/bash

# 将elasticsearch解压后的bin目录加入环境变量

#限定es用户操作此脚本
user=$(whoami)
if [ "$user" != "es" ];then
  echo "使用es用户操作该脚本."
  exit 1
fi

es_st() {
  if [[ "$(es_ck)" == "2" ]];then
     echo "elasticsearch is running"
     exit 5
  else
    elasticsearch -d -p pid.txt
  fi
}

es_sp() {
  if [[ "$(es_ck)" != "2" ]];then
    echo "elasticsearch is stopped"
    exit 6
  else
    pid=$(cat ./pid.txt)
    kill $pid && rm ./pid.txt && echo "stopping elasticsearch..."
    sleep 3
  fi
}

es_ck() {
  if [ -f ./pid.txt ];then
    local pid=$(cat ./pid.txt)
    local pids=($(pgrep -u es))
    if [[ "${pids[@]}" =~ "$pid" ]];then
        echo 2
    else
        echo 3
    fi
  else
    echo 4
  fi
}


case "$1" in
    start)
        es_st
        ;;
    stop)
        es_sp
        ;;
    check)
        if [[ "$(es_ck)" == "2" ]];then
          echo "elasticsearch is running"
        else
          echo "elasticsearch is stopped"
        fi
        ;;
    *)
    echo $"Usage: $0 {start|stop|check}"
    exit 1
esac
