#!/bin/bash

## 数据恢复: mysql -S /data/mysql/mysql.sock -utest -ptest123 DBNAME <test_1-2021-11-25.sql

## MYDB数据库备份

DB_USER="test"
DB_PASS="test123"
DB_SOCK="/data/mysql/mysql.sock"
DB_HOST="127.0.0.1"
BACK_DIR="/data/back"
CUR_DATE=$(date +%Y-%m-%d-%H-%M)
DBS=($(mysql -h ${DB_HOST} -u${DB_USER} -p${DB_PASS} -e "show databases;" 2>&1|grep -v "Warning"|egrep "syf_[a-z]*_[0-9]*"))

if [[ ! -d ${BACK_DIR} ]];then
    mkdir -p ${BACK_DIR}
fi

for db in ${DBS[@]}
do
    echo "########${db}#########"
    mysqldump --opt -h ${DB_HOST} -u${DB_USER} -p${DB_PASS} ${db} 2>&1|grep -v "Warning*"|gzip > ${BACK_DIR}/${db}-${CUR_DATE}.sql.gz
    if [[ $? -eq 0 ]];then
        echo "${db}-${CUR_DATE}.sql.gz 备份成功!"
    else
        echo "${db}-${CUR_DATE}.sql.gz 备份失败!"
    fi
    sleep 2
done
