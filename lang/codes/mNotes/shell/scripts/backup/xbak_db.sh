#!/bin/bash

## xtrabackup备份单个数据库

## 数据库信息
DBHOST="127.0.0.1"
DBUSER="bkpuser"
DBPASS="bkpuser123"
DBPORT=3306
DBDEST="/data/back/mysql/"
DBSORC="/data/mysql/"
ALLDBS=$(ls ${DBSORC}|egrep "test_*")
## 日期
CURDAY=$(date +%Y%m%d)
ONEDAY=$(date -d "1 days ago" +%Y%m%d)
TOWDAY=$(date -d "2 days ago" +%Y%m%d)
CURWEEK=$(date +%w)
ONEWEEK=$(date -d "1 days ago" +%w)
TOWWEEK=$(date -d "2 days ago" +%w)
## 其他
LOGDIR="logs/"

## 帮助信息
function Help() {
    echo "
    Usage:
       sh $0 -t [all|inc]

       -h | --help    帮助信息
       -t | --target  执行操作[all|inc]
            *all      执行全量备份
            *inc      执行增量备份
    "
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

## 数据全量备份
function FuBack() {
    for db in ${ALLDBS[@]}
    do
        if [[ ! -d ${DBDEST}${CURDAY}-${CURWEEK}/${db} ]]
        then
            mkdir -p ${DBDEST}${CURDAY}-${CURWEEK}/${db}
        fi
        xtrabackup --host=${DBHOST} --user=${DBUSER} --password=${DBPASS} \
          --port=${DBPORT} --databases=${db} --backup --datadir=${DBSORC} \
          --target-dir=${DBDEST}${CURDAY}-${CURWEEK}/${db} \
          >>${LOGDIR}xbak-${CURDAY}.log 2>&1 &&
          echo ====${db}全量备份成功==== >>${LOGDIR}xbak-${CURDAY}.log ||
          echo ====${db}全量备份失败==== >>${LOGDIR}xbak-${CURDAY}.log
    done
}

## 数据增量备份
function InBack() {
    for db in ${ALLDBS[@]}
    do
        if [[ ! -d ${DBDEST}${CURDAY}-${CURWEEK}/${db} ]]
        then
            mkdir -p ${DBDEST}${CURDAY}-${CURWEEK}/${db}
        fi
        if [[ -d ${DBDEST}${ONEDAY}-${ONEWEEK}/${db} ]]
        then
            xtrabackup --host=${DBHOST} --user=${DBUSER} --password=${DBPASS} \
              --port=${DBPORT} --backup --target-dir=${DBDEST}${CURDAY}-${CURWEEK}/${db} \
              --incremental-basedir=${DBDEST}${ONEDAY}-${ONEWEEK}/${db} \
              >>${LOGDIR}xbak-${CURDAY}.log 2>&1 &&
              echo ====${db}增量备份成功==== >>${LOGDIR}xbak-${CURDAY}.log ||
              echo ====${db}增量备份失败==== >>${LOGDIR}xbak-${CURDAY}.log
        else
            xtrabackup --host=${DBHOST} --user=${DBUSER} --password=${DBPASS} \
              --port=${DBPORT} --databases=${db} --backup --datadir=${DBSORC} \
              --target-dir=${DBDEST}${CURDAY}-${CURWEEK}/${db} \
              >>${LOGDIR}xbak-${CURDAY}.log 2>&1 &&
              echo ====${db}全量备份成功==== >>${LOGDIR}xbak-${CURDAY}.log ||
              echo ====${db}全量备份失败==== >>${LOGDIR}xbak-${CURDAY}.log
        fi
    done
}
# 检查备份工具xtrabackup是否存在
function CheckTook() {
    if [[ ! -x /usr/bin/xtrabackup ]]
    then
        echo "xtrabackup工具未安装"
        return 1
    fi
}


function Main() {
     CheckTook 
     if [[ $? -eq 1 ]]
     then
         exit 1
     fi
     if [[ ! -d ${LOGDIR} ]]
     then
         mkdir ${LOGDIR}
     fi
     # 检查是否有数据库进行备份 
     if [[ ${#ALLDBS[@]} -eq 0 ]]
     then
         exit 1
     fi

     GetCmdArg $@
     if [[ -z "${TarGet}" ]]
     then
         Help
         exit 1
    fi
    # 数据备份
    if [[ "${TarGet}" == "all" ]]
    then
        FuBack
    elif [[ "${TarGet}" == "inc" ]]
    then
        InBack
    else
        Help
        exit 1
    fi
    if [[ -n `ls ${DBDEST}${CURDAY}-${CURWEEK}` ]]
    then
        tar -czPf ${DBDEST}${CURDAY}-${CURWEEK}.tar.gz \
          ${DBDEST}${CURDAY}-${CURWEEK}
        [ -d ${DBDEST}${TOWDAY}-${TOWWEEK} ] &&
          rm -rf ${DBDEST}${TOWDAY}-${TOWWEEK}
    fi  
}

Main $@


## 数据恢复说明
# 1. 准备数据
# 2. 备份要恢复的数据库
# 3. 停掉mysql服务
# 4. 删除要恢复的数据库(mysql服务实例目录下的数据库目录): rm dirname -rf 
# 5. 将准备好的数据拷贝至mysql实例所在目录: 
#    注意拷贝数据的名字(cp -r /data/back/mysql/20220606-1/test_2/test_2/ /data/mysql)
# 6. 修改mysql实例所在目录的所属用户和组
# 7. 启动mysql服务
