#!/bin/bash

# svn数据备份脚本
daytme=$(date +"%Y-%m-%d")
curtme=$(date +"%H:%M")
svncmd="svn --username wupan --password 123456"
svnurl="http://172.16.9.125:8080/svn/"
dstdir="/data/svnbak/"
svndir="/data/datasvn/"
logdir=$(cd "$(dirname $0)"; pwd)"/logs/"


dstdirs=($(ls -l ${dstdir} | grep '^d' | awk '{print $NF}'))
srcdirs=($(ls -l ${svndir} | grep '^d' | awk '{print $NF}'))

if [[ ! -d ${logdir} ]];then
    mkdir -p ${logdir}
fi


for s in ${srcdirs[@]};do
    if [[ "${dstdirs[@]}" =~ "$s" ]];then
        echo $s "存在"
        ${svncmd} update ${dstdir}${s}
        if [[ $? -eq 0 ]];then
            echo "${curtme} ${s} 更新成功" >> ${logdir}${daytme}".log"
        fi
    else
        echo $s "不存在"
        ${svncmd} co ${svnurl}${s} ${dstdir}${s} >> ${logdir}"svn.log" 2>&1
        if [[ $? -eq 0 ]];then
            echo "${curtme} ${s} 拉取成功" >> ${logdir}${daytme}".log"
        fi
    fi
done


