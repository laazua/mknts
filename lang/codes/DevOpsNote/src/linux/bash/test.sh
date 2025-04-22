#!/usr/bin/bash
#
# trap 命令
#   SIGINT: 中断
#   SIGTERM: 终止
#   SIGQUIT: 终止并核心转储
#   EXIT: 正常或异常退出
#   ERR: 非零状态退出

clean() {
    echo "do some clean ..."
    exit
}

trap 'clean' SIGINT

while true;do
	sleep 1
	echo xxx
done

