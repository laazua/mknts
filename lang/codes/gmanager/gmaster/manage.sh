#!/bin/bash

set -e
# gmaster应用管理脚本

start_app() {
    if [[ $(check_app) -eq 1 ]];then
        echo "gmaster app 正在运行中..."
        exit 1
    else
        pdm run python app/main.py >> logs/app.log 2>&1 &
        echo "gmaster app 启动成功"
    fi
}

stop_app() {
    if [[ $(check_app) -eq 2 ]];then
        echo "app 已停止运行..."
        exit 1
    else
        local pid
        pid=$(pgrep -f "pdm run python")
        kill -9 "$pid" && echo "gmaster app, pid: ${pid} 停止成功"
    fi
}

check_app() {
    local pid
    pid=$(pgrep -f "pdm run python")
    if [[ "$pid" ]];then
        echo 1
    else
        echo 2
    fi
}

case $1 in 
    "start")
        [ ! -d "logs" ] && mkdir logs 
        start_app
        ;;
    "stop")
        stop_app
        ;;
    "check")
        if [[ $(check_app) -eq 1 ]];then
            echo "gmaster app 正在运行中..."
        else
            echo "gmaster app 已经停止..."
        fi
        ;;
    *)
        echo "bash $0 [start|stop|check]"
        exit 0
        ;;
esac