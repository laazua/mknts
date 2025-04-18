#!/bin/bash

## 数据恢复: mysql -S /data/mysql/mysql.sock -utest -ptest123 DBNAME <test_1-2021-11-25.sql

## MYSQL数据库备份

SQL_USER="gamedb"
SQL_PASS="@Gamedb123#x#"
SQL_SOCK="/data/mysql/mysql.sock"
SQL_HOST="127.0.0.1"
BACK_DIR="/data/back"
CUR_DATE=$(date +%Y-%m-%d)
DBS=($(MYSQL_PWD=${SQL_PASS} mysql -h ${SQL_HOST} -u${SQL_USER} -e "show databases;" 2>&1|grep -v "Warning*"|grep -E "^syf_tap@002dtest_*"))

if [[ ! -d ${BACK_DIR} ]];then
    mkdir -p ${BACK_DIR}
fi

for db in ${DBS[@]}
do
    echo "########${db}#########"
    mysqldump --opt -h ${SQL_HOST} -u${SQL_USER} -p${SQL_PASS} ${db} 2>&1|grep -v "Warning*"|gzip > ${BACK_DIR}/${db}-${CUR_DATE}.sql.gz
    if [[ $? -eq 0 ]];then
        echo "${db} 备份成功!"
    else
        echo "${db} 备份失败!"
    fi
    sleep 2
done