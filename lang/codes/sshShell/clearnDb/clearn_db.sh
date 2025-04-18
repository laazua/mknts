#!/bin/bash

## 此脚本用于游戏game库清档

MYSQL_CMD="/usr/bin/mysql"
MYSQL_DUP="/usr/bin/mysqldump"
MYSQL_HOST="127.0.0.1"
MYSQL_PORT="3306"
MYSQL_USER="gamedb"
MYSQL_PASS="@Gamemysql123"
MY_PATH="$(cd "$(dirname $0)"; pwd)"
GAME_ALIAS="syf"
SERVER_NAME=$2
SERVER_ID=$4

DAY_TIME=$(date +"%Y-%m-%d")

help_msg() {
    echo
    echo "## 此脚本用于game库清库" 
    echo "## sh $0 -a serverName -z serverId"
    echo
    exit 1
}
### 检查环境
chk_env() {
    if [[ ! -x ${MYSQL_CMD} ]] && [[ ! -x ${MYSQL_DUP} ]];then
        echo -e "\e[33m mysql tools not exists.\e[0m"
        exit 1 
    fi
}

### 清库
clearn_data() {
    if [[ ! -d ${MY_PATH}/back ]];then
        mkdir ${MY_PATH}/back
    fi
    
    bak_db=`mysql -h ${MYSQL_HOST} -u${MYSQL_USER} -p"${MYSQL_PASS}" -P3306 -e"show databases;" 2>&1 | grep -v "Warning: Using a password"|grep "${GAME_ALIAS}_${SERVER_NAME}_${SERVER_ID}" 2>/dev/null`
    
    if [ ! "${bak_db}" ];then
        echo -e "\033[31m您要删除的数据库不存在,请确认输入的serverName和serverId是否正确!!\033[0m"
        exit 1
    fi
    
    echo -e "\033[32m您要删除的数据库是: ${bak_db}\033[0m"
    read -e -p "请确认是否真的要删除[yse|no]: " enter
    if [ "${enter}" != "yes" ];then
        exit 1
    fi   
    
    echo -e "\033[31m正在备份数据库: ${bak_db} ..."
    mysqldump -h -h ${MYSQL_HOST} -u${MYSQL_USER} -p"${MYSQL_PASS}" -P3306 --database ${bak_db} >${MY_PATH}/back/${bak_db}-${DAY_TIME}.sql
    if [ $? -ne 0 ];then
        echo -e "\033[31m数据库: ${bak_db} 备份失败!"
        exit 1
    fi

    echo -e "\033[31m数据库备份完成,正在删除数据库..\033[0m"
    mysql -h ${MYSQL_HOST} -u${MYSQL_USER} -p"${MYSQL_PASS}" -P3306 -e"drop database ${bak_db};" 2>&1 | grep -v "Warning: Using a password"
    if [ $? -ne 0 ];then
        echo -e "\033[31m数据库: ${bak_db} 删除失败!\033[0m"
        exit 1
    fi
    echo -e "\033[32m数据库: ${bak_db} 删除成功.\033[0m"
}

chk_env

if [ "$#" != "4" ] && [ "$1" != "-a" ] && [ "$3" != "-z" ] ;then
    help_msg
fi

#clearn_data