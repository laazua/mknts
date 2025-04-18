#!/usr/bin/bash

## 项目管理脚本
## 项目依赖pdm工具进行管理
## 使用: bash manage.sh -h

PID="pid.txt"

run(){
    check
    if [ $? -eq 0 ];then
        nohup pdm run python -m src.count_es >/dev/null 2>&1 &
        echo $! >"${PID}"
    else
        echo "程序正在运行中"
    fi
}

check(){
    local pid=$(cat "${PID}")
    if [ "$pid" = "" ];then
	return 0
    else
        return 1
    fi
}

stop(){
    check
    if [ $? -eq 0 ];then
	echo "程序已停止运行"
    else
        kill $(cat "${PID}") && >"${PID}"
    fi
}

help(){
    echo "Usage: bash $0 [run|stop|check|help]"
    echo "        run        启动程序"
    echo "        stop       停止程序"
    echo "        check      状态检查"
}


# 第一次运行创建pid.txt文件
[ ! -f "${PID}" ] && touch "${PID}"

while true;do
    case "$1" in
	"run")
	    run
	    break
	    ;;
	"stop")
	    stop
	    break
	    ;;
	"check")
	    check && echo "程序已停止" || echo "程序运行中"
	    break
	    ;;
	*)
	    help
	    break
	    ;;
    esac
done