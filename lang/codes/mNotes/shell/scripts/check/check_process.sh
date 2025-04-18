#!/bin/bash

## 检测业务进程是否正常启动

# 正式环境
GAM_DIR="/data/gameserv/"
WEB_URL=""
CUR_TIM=$(date "+%Y-%m-%d#%H:%M:%S")
WEB_KEY="SYF"
PID_ADR="10.0.0.16"
# 测试环境
#GAM_DIR="/data/game/"

# 获取业务进程
function GetPids(){
    local num=0
    local -a all_p
    local pid_dirs=$(ls $GAM_DIR | grep -o "[a-z]*_[a-z]*_[0-9]*")
    for d in ${pid_dirs[@]}
    do
        if [[ -f "${GAM_DIR}$d/tmp/gameserv.pid" ]]
        then
            local pid=$(cat ${GAM_DIR}$d/tmp/gameserv.pid)
            if [[ "${pid}" != "" ]]
            then
                all_p[${num}]=${d}
            fi
           
        fi
        let num+=1
    done
    echo ${all_p[@]}
}

# 消息通知
function SendMsg(){
    curl -s ${WEB_URL} \
         -H "Content-Type: application/json" \
         -X POST \
         -d "{'msgtype':'text','text':{'content':\"$1\"}}"
}

# 检测业务进程
function ChkPids(){
    local all_p=$(GetPids)
    for d in ${all_p[@]}
    do
        local pid=$(cat ${GAM_DIR}$d/tmp/gameserv.pid)
        if [[ ! -L /proc/${pid}/exe ]]
        then
            local msg="[${WEB_KEY}][${PID_ADR}][${CUR_TIM}][${d}][stopped]"
            SendMsg $msg
        fi
        sleep 1   
    done
}

# 检测磁盘
function ChkDisk(){
    local disk=$(df -h |grep '/data'|awk '{print $5}'|awk -F'%' '{print $1}')
    if [[ $disk -gt 80 ]]
    then
        local msg="[${WEB_KEY}][${PID_ADR}][${CUR_TIM}][disk:${disk}%]"
        SendMsg $msg
    fi
}

# 检测负载
function ChkLoad(){
    local load=$(w|awk NR==1|awk -F':' '{print $5}'|awk -F',' '{print $1}')
    echo $load
}

# 入口
function Main(){
    ChkPids
    ChkDisk
    ChkLoad
}

Main $@
