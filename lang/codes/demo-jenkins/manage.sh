#!/bin/bash

app_name=prometheus
app_path=$(cd `dirname $0`;pwd)
log_name=prometheus.log
excute_file=${app_path}/${app_name}

if [ ! -f ${excute_file} ];then
    echo "excute file not exist!"
    exit
fi

start_app() {
    local pid=$(ps aux|grep "${app_name}"|grep -v grep|awk '{print $2}')
    if [ ${pid} ];then
        echo "${app_name} is running"
        exit
    fi
    ${excute_file} >> ${app_path}/${log_name} 2>&1 &
    if [ $? -eq 0 ];then
        echo "start ${app_name} success"
    else
        echo "start ${app_name} failure"
    fi
}

stop_app() {
    local pid=$(ps aux|grep "${app_name}"|grep -v grep|awk '{print $2}')
    if [ "${pid}" ];then
        kill ${pid} && echo "stop ${app_name} success" || echo "stop ${app_name} failure"
    else
        echo "${app_name} not running"
    fi
}

restart_app() {
    stop_app
    sleep 2
    start_app
}

check_app() {
    local pid=$(ps aux|grep "${app_name}"|grep -v grep|awk '{print $2}')
    if [ ${pid} ];then
        echo "${app_name} is running"
    else
        echo "${app_name} is stopped"
    fi
}

case $1 in 
    start)
        start_app
        ;;
    stop)
        stop_app
        ;;
    check)
        check_app
        ;;
    restart)
        restart_app
        ;;
    *)
        echo "sh $0 [start|stop|restart|check]"
        ;;
esac
