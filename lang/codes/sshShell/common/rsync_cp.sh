#!/bin/bash

# 拷贝目标文件和目标文件的MD5到远程主机上
dest_ips=("10.0.0.16")
TMP_FIFO="/tmp/$$.fifo"
THREAD_NUM=4


if [[ "$1" != "-f" ]] && [[ "$2" == "" ]];then
    echo -e "\033[31m $0 -f filename -u username -d dirname \033[0m"
    exit 0
fi

if [[ "$3" != "-u" ]] && [[ "$4" == "" ]];then
    echo -e "\033[31m $0 -f filename -u username -d dirname \033[0m"
    exit 0
fi

if [[ "$5" != "-d" ]] && [[ "$6" == "" ]];then
    echo -e "\033[31m $0 -f filename -u username -d dirname \033[0m"
    exit 0
fi

mkfifo ${TMP_FIFO}
exec 6<>${TMP_FIFO}

for((i=0;i<${THREAD_NUM};i++)); do echo; done >&6

for ip in ${dest_ips[@]};do
    read -u6
    {
       rsync $2 $4@${ip}:$6
       if [ $? -eq 0 ];then
           echo -e "\033[32m $2 => ${ip}成功! \033[0m"
       else
           echo -e "\033[31m $2 => ${ip}失败! \033[0m"
       fi
       echo >&6 
    }&
done
wait

exec 6>&-
rm -f ${TMP_FIFO}
