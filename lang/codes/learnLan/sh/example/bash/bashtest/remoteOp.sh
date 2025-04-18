#!/usr/bin/bash
# Author: Sseve
dir="/home/bobo"    #该目录必须有权限

Help(){
    echo -e "\033[1;32mThis script used to upload script and execute it on remote host.\033[0m"
    echo -e "\033[1;32m -h    print help message.\033[0m"
    echo -e "\033[1;32m -t    execute sudo privilege on remote host yes|no.\033[0m"
    echo -e "\033[1;32m -s    the script you want to upload to the remote host.\033[0m"
    exit
}

if [ $# -ne 4 ];then
    echo -e "\033[1;32mUsage: sh $0 -t [yes|no] -s [*.sh]\033[0m"
    Help
    exit
else
    while test -n "$1";do
	case $1 in
	    -t | --type)
		op=$2
		shift
                ;;
	    -s | --script)
                SCRIPT=$2
 		shift
                ;;
	    *)
		exit
		;;
        esac
    shift
    done
fi

if [[ "${op}" == "yes" ]];then
    SUDO="sudo"
else
    SUDO=""
fi

ips=($(cat ip.txt|awk '{print $1}'))
echo ${ips[*]}
for ip in ${ips[*]};do
    #上传脚本
    echo -e "\033[1;32mcopy ${SCRIPT} to host:${ip} directory:${dir}\033[0m"
    scp ${SCRIPT} ${ip}:${dir}

    #执行脚本
    echo -e "execute sh ${SCRIPT} on ${ip}"
    ssh -t -q 'bobo'@${ip} "${SUDO} sh ${dir}/${SCRIPT}"
done
