#!/bin/bash

# gservant应用管理脚本

mpython=.venv/bin/python

start_app() {
    if [[ "$(check_app)" == "1" ]];then
        echo "gservant app 正在运行中..."
        exit 1
    else
        "${mpython}" app/main.py >> logs/app.log 2>&1 &
        echo "gservant app 启动成功"
    fi
}

stop_app() {
    if [[ "$(check_app)" == "2" ]];then
        echo "gservant app 已停止运行..."
        exit 1
    else
        local pid
        pid=$(pgrep -f "app/main.py")
        kill "$pid" && echo "gservant app 停止成功"
    fi
}

check_app() {
    local pid
    pid=$(pgrep -f "app/main.py")
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
        if [[ "$(check_app)" == "1" ]];then
            echo "gservant app 正在运行中..."
        else
            echo "gservant app 已经停止..."
        fi
        ;;
    *)
        echo "bash $0 [start|stop|check]"
        exit 0
        ;;
esac