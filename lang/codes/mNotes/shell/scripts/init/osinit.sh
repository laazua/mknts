#!/bin/bash

#######centos7 init########

function EchoFail() {
    echo -e "\033[31m$1\033[0m"
}

function EchoSucc() {
    echo -e "\033[32m$1\033[0m"
}


function YumBase() {
    yum -y install net-tools,vim >/dev/null && \
    EchoSucc "yum install succ" || \
    EchoFail "yum install fail"
}

# 锁定不必要的用户
function LockUsers() {
    echo "========== Run: $FUNCNAME =========="
    local users=(dbus ftp mail shutdown adm)
    for user in ${users[@]}
    do
        passwd -l $user && \
        EchoSucc "lock $user succ" || \
        EchoFail "lock $user fail"
    done
}

# 修改主要文件的属性
function SetEtc() {
    echo "========== Run: $FUNCNAME =========="
    chattr +i /etc/passwd && \
    EchoSucc "chattr /etc/passwd succ" || \
    EchoFail "chattr /etc/passwd fail"
    chattr +i /etc/shadow && \
    EchoSucc "chattr /etc/shadow succ" || \
    EchoFail "chattr /etc/shadow fail"
    chattr +i /etc/group && \
    EchoSucc "chattr /etc/group succ"  || \
    EchoFail "chattr /etc/group fail"
    chattr +i /etc/gshadow && \
    EchoSucc "chattr /etc/gshadow succ" || \
    EchoFail "chattr /etc/gshasow fail"
}

# 内核参数配置
function SetKernel() {
    echo "========== Run: $FUNCNAME =========="
    local ctlFile="/etc/sysctl.conf"
    local limFile="/etc/security/limits.conf"
    echo "*  soft  nofile  52100" >>$limFile
    echo "*  hard  nofile  52100" >>$limFile
    echo "*  soft  nproc   32768" >>$limFile
    echo "*  hard  nproc   65536" >>$limFile
    echo "*  soft  core    10240" >>$limFile
    echo "*  hard  core    10240" >>$limFile
   # echo "*  soft  core    unlimited" >>$limFile
   # echo "*  hard  core    unlimited" >>$limFilea
 
    echo "fs.file-max = 4096000" >>$ctlFile
    echo "net.ipv4.tcp_syncookies = 1" >>$ctlFile
    echo "net.ipv4.tcp_tw_recycle = 1" >>$ctlFile
    echo "net.ipv4.tcp_syn_retries = 1" >>$ctlFile
    echo "net.ipv4.tcp_tw_reuse = 1" >>$ctlFile
    echo "net.core.wmem_default = 8388608" >>$ctlFile
    echo "net.core.rmem_default = 8388608" >>$ctlFile
    echo "net.core.rmem_max = 16777216" >>$ctlFile
    echo "net.core.wmem_max = 16777216" >>$ctlFile
    echo "net.ipv4.tcp_mem = 94500000 915000000 927000000">>$ctlFile
    sysctl -p >/dev/null 
}

function SshCon() {
    echo "========== Run: $FUNCNAME =========="
    # 禁止root远程登录
    sed -i 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config && \
    EchoSucc "Forbid root remote login succ" || \
    EchoFail "Forbid root remote login fail"
}

function AddUser() {
    echo "========== Run: $FUNCNAME =========="
    useradd gamecpp && echo "kKndfa23n9xmN8db79djlkG" |passwd --stdin gamecpp
}


function Main() {
    if [[ "$UID" != "0" ]]
    then
        EchoFail "Run This Script With Root!"
        return
    fi
    
    YumBase
    LockUsers
    SetEtc
    SetKernel
    SshCon
}   AddUser

Main $@
