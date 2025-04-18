#!/bin/bash

# some global variable

GAME_PATH=$(cd "$(dirname $0)"; pwd)
PID_FILE=${GAME_PATH}/tmp/gameserv.pid
GAME_ZONE=$(pwd|awk -F'_' '{print $NF}')

# game zone server check
game_check() {
    local pid=$(cat ${PID_FILE})
    if [[ -L /proc/${pid}/exe ]]; then
        echo "game starting"
        exit 1
    else
        echo "game stopped"
    fi
}

# game zone server start
game_start() {
    [[ ! -d ${GAME_PATH}/tmp ]] && mkdir -p ${GAME_PATH}/tmp && touch $PID_FILE
    result=$(game_check)
    ret=$(echo ${result}|grep -o 'starting')
    if [[ "${ret}" ]]; then
        echo "already started"
        exit 1
    fi
    if [[ -f gameserv ]];then
        chmod +x gameserv
    else
        echo "bin file not find"
        exit 1
    fi
    # replace config.json ServerId
    isInit=$(is_init)
    if [[ ${isInit} -eq 0 ]];then
        sed -i "s/zone/${GAME_ZONE}/" config.json
    fi
    ${GAME_PATH}/gameserv
    if [[ $? -eq 0 ]];then
        echo "game start success"
    else
        echo "game start failed"
    fi
}

# check game zone init
is_init() {
    hasZone=$(cat config.json|grep -o 'zone')
    if [[ "${hasZone}" ]];then
        echo 0
    else
        echo 1
    fi
}

# game zone server stop
game_stop() {
    local pid=$(cat ${PID_FILE})
    local apid=$(ps aux|grep "${GAME_PATH}"|grep -v 'grep'|awk '{print $2}')
    if [[ "${apid}" ]] && [[ "${pid}" ]];then
        kill -15 ${pid} && >${PID_FILE}
        if [[ $? -eq 0 ]];then
            echo "game stop success"
        else
            echo "game stop failed"
        fi
    else
        echo "already stopped"
    fi
}
game_reload() {
    local pid=$(cat ${PID_FILE})
    local apid=$(ps aux|grep "${GAME_PATH}"|grep -v 'grep'|awk '{print $2}')
    if [[ ${pid} = ${apid} ]];then
        kill -10 ${pid} && >${PID_FILE}
        if [[ $? -eq 0 ]];then
            echo "game reload success"
        else
            echo "game reload failed"
        fi
    else
        echo "game already stopped"
    fi
}


# game status check
game_status() {
    game_check
}


case "$1" in
    start)
        game_start
        ;;
    stop)
        game_stop
        ;;
    reload)
	    game_reload
   	    ;;
    check)
        game_status
        ;;
    *)
    echo $"Usage: $0 {start|stop|check}"
    exit 1
esac
