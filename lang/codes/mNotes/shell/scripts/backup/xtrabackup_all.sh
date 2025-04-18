#!/bin/bash

## xtrabackup工具库备份数据库数据 ##
## 第一次运行此脚本时先mysqldump数据##
## 参考: https://www.percona.com/doc/percona-xtrabackup/8.0/backup_scenarios/full_backup.html

## 数据源目录权限:
## 需要有读和可执行权限
## 数据库实例权限
## mysql> CREATE USER 'bkpuser'@'localhost' IDENTIFIED BY 's3cr%T';
## mysql> GRANT BACKUP_ADMIN, PROCESS, RELOAD, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'bkpuser'@'localhost';
## mysql> GRANT SELECT ON performance_schema.log_status TO 'bkpuser'@'localhost';
## mysql> GRANT SELECT ON performance_schema.keyring_component_status TO bkpuser@'localhost'
## mysql> FLUSH PRIVILEGES;


## 定时周一到周六凌晨4点30增备
# 30 4 * * 1-6 sh $0 -t inc
## 定时周日凌晨4点30全备份
# 30 4 * * 0 sh $0 -t all


## 数据恢复流程:
##  - 准备数据
##  - 停mysqld服务
##  - 恢复数据

## 备份的是整个数据库实例 ##

##### 全局变量 #####
#每天增量备份时间
CURDAY=$(date +%Y%m%d)
PREDAY=$(date -d "1 days ago" +%Y%m%d)
TOWDAY=$(date -d "2 days ago" +%Y%m%d)
# 星期几(0为星期日,1-6为星期一至星期六)
WEEKDAY=$(date +%w)
PREPDAY=$(date -d "1 days ago" +%w)
TOWPDAY=$(date -d "2 days ago" +%w)
# 数据库用户
DBUSER="test"
# 数据库密码
DBPASS="test123"
# 数据库地址
DBHOST="127.0.0.1"
# 数据库端口
DBPORT=3306
# 源数据目录
DBSORC="/data/mysql/"
# 目标数据目录
DBDEST="/data/back/mysql/"
# 日志目录
LOGDIR="logs/"

## help message
function Help() {
    echo "Usage:"
    echo "    sh $0 -t [all|inc|pre]"
    echo
    echo "    -h | --help    帮助信息"
    echo "    -t | --target  执行操作[all|inc]"
}

## 数据全量备份
function FuBack() {
    echo "[== Run $FUNCNAME ==]" >> ${LOGDIR}xbak-${CURDAY}.log 2>&1
    if [[ ! -d ${DBDEST}xbak-${WEEKDAY}-${CURDAY} ]]
    then
        mkdir -p ${DBDEST}xbak-${WEEKDAY}-${CURDAY}
    fi
    xtrabackup --defaults-file=/etc/my.cnf --user=${DBUSER} --password=${DBPASS} \
        --host=${DBHOST} --port=${DBPORT} --backup \
        --target-dir=${DBDEST}xbak-${WEEKDAY}-${CURDAY} >>${LOGDIR}xbak-${CURDAY}.log 2>&1
    return $?
}

## 数据增量备份
function InBack() {
    echo "[== Run $FUNCNAME ==]" >>${LOGDIR}xbak-${CURDAY}.log 2>&1
    # 创建当前备份的目录
    if [[ ! -d ${DBDEST}xbak-${WEEKDAY}-${CURDAY} ]]
    then
        mkdir -p ${DBDEST}xbak-${WEEKDAY}-${CURDAY}
    fi
    # 判断是否是第一次备份
    if [[ -d ${DBDEST}xbak-${PREPDAY}-${PREDAY} ]]
    then
        xtrabackup --defaults-file=/etc/my.cnf --user=${DBUSER} --password=${DBPASS} \
            --host=${DBHOST} --port=${DBPORT} --backup --target-dir=${DBDEST}xbak-${WEEKDAY}-${CURDAY} \
            --incremental-basedir=${DBDEST}xbak-${PREPDAY}-${PREDAY} >>${LOGDIR}xbak-${CURDAY}.log 2>&1
        return $?
    else
        FuBack
        return $?
    fi

}

## 全备份数据恢复步骤
function FuPrepare() {
    echo "[== Run $FUNCNAME ==]" >>${LOGDIR}xbak-${CURDAY}.log 2>&1
#    read -p "输入要恢复的备份目录: " dest
#    xtrabackup --user=${DBUSER} --password=${DBPASS} --prepare --target-dir=$dest
#    xtrabackup --defaults-file=/etc/my.cnf --user=${DBUSER} --password=${DBPASS} \
#        --copy-back --target-dir=$dest
#    chown -R mysql.mysql ${DBSORC}
#    return $?
}

# 增量备份数据恢复步骤
function InPerpare() {
    echo "[== Run $FUNCNAME ==]" >>${LOGDIR}xbak-${CURDAY}.log 2>&1
    ## 停止mysql服务
    ## 备份mysql数据目录(/data/mysql)
    ##基于全备份准备数据
    # xtrabackup --prepare --apply-log-only --target-dir="全备份目录"
    ## 准备第一次增量备份的数据
    # xtrabackup --prepare --apply-log-only --target-dir="全备份目录" \
    #    --incremental-dir="第一次增量备份的目录"
    ## 准备第二次增量备份的数据
    #  xtrabackup --prepare --apply-log-only --target-dir="全备份目录" \
    #    --incremental-dir="第二次增量备份的目录"
    # ......
    ## 准备第N次增量备份的数据
    #  xtrabackup --prepare --apply-log-only --target-dir="全备份目录" \
    #    --incremental-dir="第N次增量备份的目录"
    ## 数据恢复
    # xtrabackup --copy-back --target-dir="全备份目录"
    # chown -R mysql:mysql /data/mysql #(/data/mysql是mysql的数据目录)
}

## 获取命令行参数 
function GetCmdArg() {
    while test -n "$1"
    do
        case "$1" in
            -h | --help)
                Help
                exit
                ;;
            -t | --target)
                TarGet=$2
                shift
                ;;
            *)
                Help
                exit
                ;;
        esac
        shift
    done
}

## 脚本入口
function Main() {
    local current_time=$(date +%H:%M:%S)
    echo ===${current_time}=== >>${LOGDIR}xbak-${CURDAY}.log 2>&1
    if [[ $UID -ne 0 ]]
    then
        echo "run this script with root"
        exit
    fi
    if [[ ! -d ${LOGDIR} ]]
    then
        mkdir ${LOGDIR}
    fi
    # 获取命令行参数
    GetCmdArg $@
    if [[ -z "${TarGet}" ]]
    then
        Help
        return
    fi
    # 执行全量备份   
    if [[ "${TarGet}" == "all" ]]
    then
        FuBack && [ -d ${DBDEST}xbak-${WEEKDAY}-${CURDAY} ] &&
            tar -czPf ${DBDEST}xbak-${WEEKDAY}-${CURDAY}.tar.gz \
            ${DBDEST}xbak-${WEEKDAY}-${CURDAY}
        [ -d ${DBDEST}xbak-${TOWPDAY}-${TOWDAY} ] &&
            rm -rf ${DBDEST}xbak-${TOWPDAY}-${TOWDAY}
    fi
    # 执行增量备份
    if [[ "${TarGet}" == "inc" ]]
    then
        InBack && [ -d ${DBDEST}xbak-${WEEKDAY}-${CURDAY} ] &&
            tar -czPf ${DBDEST}xbak-${WEEKDAY}-${CURDAY}.tar.gz  \
            ${DBDEST}xbak-${WEEKDAY}-${CURDAY}
        [ -d ${DBDEST}xbak-${TOWPDAY}-${TOWDAY} ] &&
            rm -rf ${DBDEST}xbak-${TOWPDAY}-${TOWDAY}
    fi
}

Main $@

