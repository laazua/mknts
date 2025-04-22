#!/usr/bin/bash

set -e

declare -r service_name="DevOpsNote"

# 检查mdbook工具是否存在
mdbook_path=$(whereis mdbook)
if [[ "${mdbook_path}" == "mdbook:" ]];then
    exit 1
    echo "mdbook工具不存在"
    echo "如果安装了rust环境,运行: cargo install mdbook"
fi

stop_app() {
    local status=$(check_app)
    if [[ "${status}" == "stopped" ]];then
        echo "${service_name} is stopped."
        return
    fi
    local pid=$(pgrep "mdbook")
    kill "${pid}" && echo "Stop ${service_name} success."
}

start_app() {
    local status=$(check_app)
    if [[ "${status}" == "running" ]];then
        echo "${service_name} is runnung."
        return
    fi
    mdbook serve "../${service_name}" -n 0.0.0.0 -p 8886 >/dev/null 2>&1 &
    if [[ $? -eq 0 ]];then
        echo "Start ${service_name} success."
    else
        echo "Start ${service_name} failure."
    fi
}

check_app() {
    local pid=$(pgrep mdbook)
    if [[ "${pid}" == "" ]];then
        echo "stopped"
    else
        echo "running"
    fi
}

restart_app() {
    stop_app
    sleep 2
    start_app
}

main() {
    case $1 in 
        start)
            start_app
            ;;
        stop)
            stop_app
            ;;
        check)
            local status=$(check_app)
            if [[ "${status}" == "running" ]];then
                echo "${service_name} is running."
            else
                echo "${service_name} is stopped."
            fi
            ;;
        restart)
            restart_app
            ;;
        *)
            echo "bash $0 [start|stop|restart|check]"
            ;;
    esac
}

main "$@"
