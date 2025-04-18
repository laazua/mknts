#!/bin/bash
## 同步后端程序 ##

set -e

USERNAME="gamecpp"
PASSWORD=""
HOSTNAME=""
MYPATH=$(pwd)

function Help() {
    echo "usage: sh $0 -f gameserv-xxxx"
    echo "  -h | --help    帮助信息"
    echo "  -f | --file    指定文件"
}

function ChekMd5() {
    local LocalMd5=$(md5sum gameserv.zip|awk '{print $1}')
    local RemotMd5=$(sshpass -p $PASSWORD ssh -q -tt ${USERNAME}@${HOSTNAME} \
                     "md5sum /data/root/bnzt/bin/gameserv.zip"|awk '{print $1}')
    #echo "L" $LocalMd5
    #echo "R" $RemotMd5
    if [[ ${LocalMd5} == ${RemotMd5} ]]
    then
        return 0
    else
        return 1
    fi
}

if [[ ! -x /usr/bin/sshpass ]]
then
    echo "yum install sshpass"
    exit
fi

while test -n "$1"
do
    case "$1" in
        -h | --help)
            Help
            exit
            ;;
        -f | --file)
            FileName=$2
            shift
            ;;
        *)
            Help
            exit
            ;;
        esac
        shift
done


if [[ ! "${FileName}" ]]
then
    Help
    exit
fi
md5sum $FileName

# 更改上传文件名并压缩
cp $FileName gameserv && 
    chmod +x gameserv && 
    zip gameserv.zip gameserv >/dev/null

[ -f ${MYPATH}/gameserv ] && rm -rf ${MYPATH}/gameserv

# 上传文件
sshpass -p $PASSWORD rsync --compress-level=9 --backup \
    gameserv.zip ${USERNAME}@${HOSTNAME}:/data/root/bnzt/bin
if [[ $? -eq 0 ]]
then
    ChekMd5 && echo "$FileName 上传成功!" ||
        echo "md5值不一致!"
else
    echo "$FileName 上传失败!"
fi

[ -f ${MYPATH}/gameserv.zip ] && rm -rf ${MYPATH}/gameserv.zip
