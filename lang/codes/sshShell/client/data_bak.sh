#!/bin/bash

## 作者: Sseve
## 日期: 2021-10-09
## 描述: 数据库备份
## 工具: xtrabackup
## 数据库用户权限: ...
## create user 'gamebk'@'localhost' identified by '#dKJ1L43jkl@ak84K3m#';
## REVOKE ALL PRIVILEGES  ON *.* FROM 'gamebk'@'localhost'; 回收权限
## GRANT SELECT,BACKUP_ADMIN,RELOAD,LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'gamebk'@'localhost';

## xtrabackup8.0安装
## wget https://downloads.percona.com/downloads/Percona-XtraBackup-LATEST/Percona-XtraBackup-8.0.26-18/binary/redhat/7/x86_64/percona-xtrabackup-80-8.0.26-18.1.el7.x86_64.rpm
## yum localinstall percona-xtrabackup-80-8.0.26-18.1.el7.x86_64.rpm

SQL_USER="gamebk"
SQL_PASS="#dKJ1L43jkl@ak84K3m#"
SQL_SOCK="/data/mysql/mysql.sock"
SQL_TOOL="/usr/local/mysql/bin/mysql"
TAR_DIR="/data/back"
XBK_TOOL="/usr/bin/xtrabackup"


## 检查备份工具是否存在
if [[ ! -x ${XBK_TOOL} ]];then
  echo "xtrabackup tools not exists!"
  exit 1
fi

bak_db=($(${SQL_TOOL} -S ${SQL_SOCK} -u${SQL_USER} -p${SQL_PASS} -e "show databases" 2>/dev/null |grep "back*"))

wrt_log() {
  if [[ ! -d logs ]];then
    mkdir logs
  fi
  d_time=$(date +"%Y%m%d")
  h_time=$(date +"%Y%m%d%H")
  echo "${h_time} $1" >> logs/bak-${d_time}.log
}

all_bak() {
  for db in ${bak_db[@]};do
    ${XBK_TOOL} --defaults-file=/etc/my.cnf --backup --user=${SQL_USER} --password=${SQL_PASS} \
                --socket=${SQL_SOCK} --target-dir=${TAR_DIR} --databases=${db} >/dev/null 2>&1
    if [[ $? -eq 0 ]];then
      wrt_log "${db} 备份成功"
    else
      wrt_log "${db} 备份失败"
    fi
  done
}

all_bak
