#!/bin/bash

GAME_PATH=$(cd "$(dirname $0)"; pwd)
PID_FILE=${GAME_PATH}/tmp/gameserv.pid
SERVER_ID=$(echo ${GAME_PATH}|awk -F'_' '{print $NF}')

# 检查游戏是否启动
gs_ck() {
    ret=$(pgrep -l "v${SERVER_ID}"|awk '{print $1}')
    if [[ "${ret}" ]] && [[ -L /proc/${ret}/exe ]]; then
        echo "{\"code\": \"0\", \"msg\": \"starting\"}"
        exit 1
    else
        echo "{\"code\": \"1\", \"msg\": \"stopped\"}"
    fi
}

# 启动游戏
gs_st() {
    [[ ! -d ${GAME_PATH}/tmp ]] && mkdir -p ${GAME_PATH}/tmp && touch $PID_FILE
    result=$(gs_ck)
    ret=$(echo ${result}|grep -o 'starting')
    if [[ "${ret}" ]]; then
        echo "{\"code\": \"0\", \"msg\": \"starting\"}"
        exit 1
    fi
    if [[ -f gameserv-beta ]];then
        mv gameserv-beta gameserv${SERVER_ID}
    fi
    chmod +x gameserv${SERVER_ID}
    #python config.py 'tap-test' "${SERVER_ID}"
    ${GAME_PATH}/gameserv${SERVER_ID}
    if [[ $? -eq 0 ]];then
        echo "{\"code\": \"0\", \"msg\": \"startSucess\"}"
    else
        echo "{\"code\": \"1\", \"msg\": \"startFailed\"}"
    fi
}

# 关闭游戏
gs_sp() {
    pid=$(cat ${PID_FILE})
    ret=$(pgrep -l "v${SERVER_ID}"|awk '{print $1}')
    if [[ "${ret}" ]] && [[ "${pid}" ]];then
        kill -15 ${pid} && >${PID_FILE}
        if [[ $? -eq 0 ]];then
            echo "{\"code\": \"0\", \"msg: \"stopSucess\"}"
        else
            echo "{\"code\": \"1\", \"msg\": \"stopFailed\"}"
        fi
    else
        echo "{\"code\": \"1\", \"msg\": \"stopped\"}"
    fi
}

# 检查游戏状态
gs_ss() {
    gs_ck
}


case "$1" in
    start)
        gs_st
        ;;
    stop)
        gs_sp
        ;;
    check)
        gs_ss
        ;;
    *)
    echo $"Usage: $0 {start|stop|check}"
    exit 1
esac
