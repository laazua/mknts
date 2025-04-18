#!/bin/bash

:<<!
exec 6<>/dev/tcp/ip/port  --以文件描述符6打开一个可读写(<>)的socket通道,文件描述符必须大于2
echo -e "xxxx" >&6        --将xxxx信息，发送给socket连接
cat <&6			  --从socket读取返回信息,显示为标准输出
exec 6>&-		  --关闭写
exec 6<&-	          --关闭读
!

Help(){
	echo "Usage: sh checkhostPort.sh -i 127.0.0.1 -p '22 55'"
	echo "	-h|--help		print help message."
	echo "	-i|--ip			the host's ip you want to check."
	echo "	-p|--port		the host's port you want to check."
        exit
}


if [ $# -ne 4 ];then
	Help
else
	while test -n "$1";do
		case $1 in
			-h | --help)
				Help
				;;
			-i | --ip)
				IPS=$2
				shift
				;;
			-p | --port)
				PORT=$2
				shift
				;;
			*)
				exit
				;;
		esac
	shift
	done
fi

echo -e "\033[1;32m scanning,please wait... "
for P in ${PORT};do
	echo &> /dev/null > /dev/tcp/${IPS}/${P}
	if [[ $? -eq 0 ]];then
		echo -e "\033[1;32m[+]\033[0m IP:${IPS} --> ${P} open."
	else
		echo -e "\033[1;31m[-]\033[0m IP:${IPS} --> ${P} close."
	fi
done
