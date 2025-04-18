#!/bin/bash


## 获取本机的ip
IP_ADDR=$(curl ip.sb)
DATA_FILE="/tmp/check_${IP_ADDR}.txt"

## 账号口令检查(/etc/login.defs)
## PASS_MAX_DAYS,PASS_MIN_DAYS,PASS_MIN_LEN,PASS_WARN_AGE
function check_count_secure(){
    echo "账号口令检测..."
    # 获取各个策略项数值
    local passmax=$(cat /etc/login.defs | grep PASS_MAX_DAYS | grep -v ^# | awk '{print $2}')
    local passmin=$(cat /etc/login.defs | grep PASS_MIN_DAYS | grep -v ^# | awk '{print $2}')
    local passlen=$(cat /etc/login.defs | grep PASS_MIN_LEN | grep -v ^# | awk '{print $2}')
    local passwan=$(cat /etc/login.defs | grep PASS_WARN_AGE | grep -v ^# | awk '{print $2}')
    
    if [ ${passmax} -le 90 -a ${passmax} -gt 0 ];then
        echo "口令有效期为${passmax}天,符合要求" >> ${DATA_FILE}
    else
        echo "口令有效期为${passmax}天,不符合要求,建议小于90天" >> ${DATA_FILE}
    fi

    if [ ${passmin} -ge 6 ];then
        echo "口令更改最小时间间隔为${passmin}天,符合要求" >> ${DATA_FILE}
    else
        echo "口令更改最小时间间隔为${passmin}天,不符合要求,建议设置大于6天" >> ${DATA_FILE}
    fi

    if [ ${passlen} -ge 12 ];then
        echo "口令最小长度${passlen},符合要求" >> ${DATA_FILE}
    else
        echo "口令最小长度${passlen},不符合要求,建议最小长度大于等于8天" >> ${DATA_FILE}
    fi

    if [ $passwan -ge 30 -a $passwan -lt $passmax ];then
        echo "口令过期警告时间天数为${passwan},符合要求" >> ${DATA_FILE}
    else
        echo "口令过期警告时间天数为${passwan},不符合要求,建议设置大于等于30并小于口令生存周期" >> ${DATA_FILE}
    fi

    sleep 1
}

## 检测主机重要文件的权限
## /etc/passwd,/etc/shadow,/etc/group,/etc/securetty,/etc/services
function check_file_privilege(){
    echo "重要文件权限检测..."
    local passfile=$(ls -l /etc/passwd | awk '{print $1}')
    local shadfile=$(ls -l /etc/shadow | awk '{print $1}')
    local groufile=$(ls -l /etc/group | awk '{print $1}')
    local secufile=$(ls -l /etc/securetty | awk '{print $1}')
    local servfile=$(ls -l /etc/services | awk '{print $1}')
    if [ "${passfile}" = "-rw-r--r--" ];then
        echo "${passfile}文件权限为644,符合要求" >> ${DATA_FILE}
    else
        echo 
    fi
    sleep 1
}

## ssh配置检测
## /etc/ssh/sshd_config
function check_ssh_con(){
    echo "ssh配置检测..."
    cat /etc/ssh/sshd_config | grep -v ^# |grep "PermitRootLogin no"
    if [ $? -eq 0 ];then
        echo "已经设置远程root不能登陆,符合要求" >> ${DATA_FILE}
    else
        echo "允许远程root登陆,不符合要求,建议/etc/ssh/sshd_config添加PermitRootLogin no" >> ${DATA_FILE}
    fi
    
    Protocol=`cat /etc/ssh/sshd_config | grep -v ^# | grep Protocol | awk '{print $2}'`
    if [ "$Protocol" = "2" ];then
        echo "openssh使用ssh2协议,符合要求" >> ${DATA_FILE}
    fi
    if [ "$Protocol" = "1" ];then
        echo "openssh使用ssh1协议,不符合要求" >> ${DATA_FILE}
    fi
}


check_count_secure
check_file_privilege
check_ssh_con
