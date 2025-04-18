#!/bin/bash
# linux(centos) + nginx + apache + mysql + php Web应用架构部署.
# 部署前请确认相关服务是否已经安装.
# 建议将经常要用到的服务版本下载到一个内网服务器,方便安装.

#清屏打印说明信息
clear
echo "-----------------------------------------------------------------"
echo "|  欢迎使用该脚本安装WebServer,提供三种架构选择和一种自由选择项 |"
echo "|    1  nginx + php + mysql                                     |"
echo "|    2  apache + php + mysql                                    |"
echo "|    3  nginx + apache + php + mysql                            |"
echo "|    4  select the server you need in (apachee nginx php mysql) |"
echo "-----------------------------------------------------------------"

## 加载变量&&函数
. libs/common.sh
. libs/getpkg.sh
. libs/server.sh

if [[ "${USER}" != "root" ]];then
	echo "请以root身份运行此脚本"
	exit 
fi

echo "start install..."
sleep 10

## 安装环境呢依赖
libs_install
pcre

## 创建安装日志记录目录
[ ! -d install_logs ] && mkdir install_logs

## 提供三种架构选择和一种自由选择项
echo "   1 [nginx + php + mysql + zend + pureftpd + phpmyadmin]
   2 [apache + php + mysql + zend + pureftpd + phpmyadmin]
   3 [nginx + apache + php + mysql + zend + pureftpd + phpmyadmin]
   4 [select the server you need in (apachee nginx php mysql)]
"

read -p "Select the server you need: " id
if [[ ${id} -eq 1 ]];then
	nginx; php; mysql
elif [[ ${id} -eq 2 ]];then
	apache; php; mysql
elif [[ ${id} -eq 3 ]];then
	nginx; apache; php; mysql
else
	read -p "输入要安装的server: " server
	for ser in ${server[@]}
	do
		if [[ "${ser}" == "apache" ]];then
			apache
		elif [[ "${ser}" == "nginx" ]];then
			nginx
		elif [[ "${ser}" == "php" ]];then
			php
		else
			mysql
		fi
	done
fi

