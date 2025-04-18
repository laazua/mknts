#!/bin/bash

## centos7


## yum install
yum_init() {
    yum -y install  wget vim lrzsz.x86_64 ntpdate \
    net-tools.x86_64 bc.x86_64 subversion cyrus-sasl \
    cyrus-sasl-plain cyrus-sasl-ldap >/dev/null 2>&1
    if [[ $? -eq 0 ]];then
        return 0
    else
        return 1
    fi
}

## file description
fd_init() {
    echo "* hard nofile 65535" >>/etc/security/limits.conf
    echo "* soft nofile 65535" >>/etc/security/limits.conf
    echo "* soft nproc 65535" >>/etc/security/limits.conf
    echo "* hard nproc 65535" >>/etc/security/limits.conf
    echo "* soft core unlimited" >> /etc/security/limits.conf
    echo "* hard core unlimited" >>/etc/security/limits.conf
    echo "FILE desc init success."
}

## kernel
kernel_init() {
    echo "fs.file-max=65535" >> /etc/sysctl.conf
    # disable ipv6
    echo "net.ipv6.conf.all.disable_ipv6=1" >> /etc/sysctl.conf
    sysctl -p >/dev/null 2>&1
    if [[ $? -eq 0 ]]
    then
        return 0
    else
        return 1
    fi
}

## del user
del_user() {
    users=(lp sync halt operator nobody)
    for user in ${users[@]}
    do
        userdel ${user}
    done
    echo "DELETE user init success"
}

## main
main() {
    if [[ "$USER" != "root" ]]
    then
        echo "run this script with root"
        exit 0
    fi   
    echo "start init ..."
    sleep 2
    yum_init
    if [[ $? -eq 0 ]];then
        echo "YUM init success."
    else
        echo "YUM init failed."
    fi
    sleep 2
    fd_init
    sleep 2
    kernel_init
    if [[ $? -eq 0 ]]
    then
        echo "KERNEL init success."
    else
        echo "KERNEL init failed."
    fi
    sleep 2
    del_user  
}

main $@
