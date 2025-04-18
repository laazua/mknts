#!/usr/bin/bash

## 项目管理脚本
EXECUTEBIN="$1"
EXICUTEOPS="$2"
ENVIREMENT=.venv

usage()
{
    echo "bash $0 NAME [run|stop|check]"
    echo "    NAME 可执行的项目文件"
    echo "    [run|stop|check] 何种操作"
    exit
}

[[ ! ${EXECUTEBIN} ]] && usage
[[ ! ${EXICUTEOPS} ]] && usage

run()
{
    nohup ${ENVIREMENT}/bin/${EXECUTEBIN} >/dev/null 2>&1 &
    if [ $? -eq 0 ];then
        echo "start success." && exit
    else
        echo "start failure." && exit
    fi
}

stop()
{
    local PID=$(pgrep ${EXECUTEBIN})
    kill ${PID}
    if [ $? -eq 0 ];then
        echo "stop success." && exit
    else
        echo "stop failure." && exit
    fi
}

check()
{
    local PID=$(pgrep ${EXECUTEBIN})
    if [[ ${PID} != "" ]];then
        echo "${EXECUTEBIN} running!" && exit
    else
        echo "${EXECUTEBIN} stopped!" && exit
    fi
}


if [ ! -d ${ENVIREMENT} ];then
    echo "Please init .venv!"
    echo "python -m venv .venv"
    exit
fi


[[ $2 == "run" ]] && run
[[ $2 == "stop" ]] && stop
[[ $2 == "check" ]] && check
