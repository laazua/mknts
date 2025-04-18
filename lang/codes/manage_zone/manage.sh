#!/bin/bash

# @Time:        2022-08-04
# @Author:      Sseve
# @File:        manage.sh
# @Description: script to manage app


check_evn() {
    ret=$(echo $PATH | grep -o virtualenvs)
    if [ "$ret" != "virtualenvs" ];then
        echo "virtual evn not active, please run cmd: pipenv shell --anyway"
        echo "then run: sh $0 start"
        exit 1
    fi
}


start_app() {
    pid=$(pgrep -f "app/main.py")
    if [[ "$pid" ]];then
        echo "app is running, pid: $pid" && return 1
    else
        python app/main.py >> app.log 2>&1 &
        pgrep -f "app/main.py" > ./pid.txt && return 0
    fi
}


stop_app() {
    pid=$(cat pid.txt)
    if [[ "$pid" ]];then
        kill "$pid" && cat /dev/null >pid.txt && return 0
    else
        echo "app is stopped" && return 1
    fi
}


check_app() {
    pid=$(pgrep -f "app/main.py")
    if [[ "$pid" ]];then
        echo "app is running, pid: $pid"
        exit 1
    else
        echo "app is stopped"
    fi
}


case $1 in
    "start")
        check_evn
        start_app && echo "app start success!"
        ;;
    "stop")
        stop_app && echo "app stop success"
        ;;
    "check")
        check_app
        ;;
    *)
        echo "sh $0 [start|stop|check]"
        exit 0
        ;;
esac
