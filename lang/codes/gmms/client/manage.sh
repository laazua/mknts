#!/bin/bash

## start|stop|restart app

# 启动app
start_app() {
    if [[ -f "app.pid" ]];then
        echo "程序已经启动!"
        exit 0
    else
        gunicorn -c guncon.py app.main:app
        if [[ $? -eq 0 ]];then
            echo "程序启动成功!"
        else
            echo "程序启动失败!"
        fi
    fi
}

# 关闭app
stop_app() {
    if [[ ! -f "app.pid" ]];then
        echo "程序已经关闭!"
        exit 0
    fi
    app_pid=$(cat app.pid)
    if [[ ! -z ${app_pid} ]];then
        kill ${app_pid}
        sleep 1
        echo "程序关闭成功!"
    else
        echo "程序关闭失败!"
    fi
}

# 重启app
restart_app() {
    stop_app
    sleep 2
    start_app
}

####
case $1 in
    "start")
        start_app
        ;;
    "stop")
        stop_app
        ;;
    "restart")
        restart_app
        ;;
    *)
        echo "sh $0 [start|stop|restart]"
        exit 0
        ;;
esac
