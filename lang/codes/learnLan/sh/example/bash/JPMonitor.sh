#!/bin/bash
# 此脚本用于监控云主机的负载及进程cpu的情况

set -e

WEBHOOK="https://oapi.dingtalk.com/robot/send?access_token=0108a668284d90a39b6a292812fa19b863a84a4ab4984e3fdf214a9ebb993c0c"

# 判断脚本是否运行
run_jpm(){
    if [ $(ps aux | grep 'JPMonitor.sh' | grep -v grep | wc -l) -gt 2 ];then
        echo 'JPMonitor.sh is running'
        exit 0
    fi
}

get_ip(){
    ip=$(cat /data/game/wanip.txt)
    echo ${ip}
}

# 获取机器负载
get_load(){
    sload=0
    ip=$(get_ip)
	for((i=0;i<5;i++));do
        load1=$(cat /proc/loadavg |awk '{print $3}' |awk -F'.' '{print $1}')
        sload=$((${sload} + ${load1}))
		sleep 2
	done
	aload=$((${sload}/5))
	echo ${aload}
    #if [[ ${aload} -gt 150 ]];then
    #    curl -H 'Content-Type: application/json' -d "{'msgtype': 'text','text':{'content': 'GameName=yyzb&&IP: ${ip}&&load: ${aload} && 当前负载过高'}}" ${WEBHOOK} > /dev/null 2>&1
    #fi

}

# 获取机器进程cpu情况
get_cpu(){
    #负载
    load=$(get_load)
	if [[ ${aload} -gt 150 ]];then
        curl -H 'Content-Type: application/json' -d "{'msgtype': 'text','text':{'content': 'GameName=yyzb&&IP: ${ip}&&load: ${aload} && 当前负载过高'}}" ${WEBHOOK} > /dev/null 2>&1
    fi
	
	#进程cpu
    >/tmp/pss.txt
    ip=$(get_ip)
	pids=$(ps -eo user,pid|grep 'javapro'|grep -v 'grep'|awk '{print $2}')
	for((i=0;i<3;i++));do
		ps -eo user,pid,%cpu|grep 'javapro'|grep -v 'grep' 1>> /tmp/pss.txt
		sleep 5
	done
	for pid in ${pids[@]};do
	    sum=$(cat /tmp/pss.txt |grep ${pid}|awk '{sum += $3};END{print sum}'|awk -F'.' '{print $1}')
		echo $sum
		asum=$((${sum}/3))
		echo ${pid} ${asum}
		if [[ ${asum} -gt 400 ]];then
            curl -H 'Content-Type: application/json' -d "{'msgtype': 'text','text':{'content': 'GameName=yyzb&&IP: ${ip}&&异常PID:${pid} -> CPU: ${asum}'}}" ${WEBHOOK} > /dev/null 2>&1
		fi
		if [[ ${load} -gt 100 ]] && [[ ${asum} -gt 300 ]];then
		    curl -H 'Content-Type: application/json' -d "{'msgtype': 'text','text':{'content': 'GameName=yyzb&&IP: ${ip}&&load: ${aload} && 异常PID:${pid} -> CPU: ${asum}'}}" ${WEBHOOK} > /dev/null 2>&1
		fi
	done
}

main(){
    #run_jpm
    #load=$(get_load)
    get_cpu
}

main "$@"
