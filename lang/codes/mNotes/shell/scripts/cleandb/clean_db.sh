#!/bin/bash

### this script used to clean db

CUR_TME=$(date +%Y-%m-%d-%H-%M)
BAK_DIR="./"
DB_ADDR="127.0.0.1"
DB_PASS="test123"
DB_USER="test"

function Help(){
    echo "Usage: sh $0 -n dbname"
    echo "    -h | --help    print help message"
    echo "    -n | --dbname  back db name"
}

function AllDBS(){
    local dbs=$(mysql -h $DB_ADDR -u${DB_USER} -p${DB_PASS} -e "show databases;" \
                2>/dev/null)
    echo ${dbs[@]}
}


## db back
function DbBack(){
    #echo "[ Run: $FUNCNAME ]"
    # 判断是否存在要删除的数据库
    local dbs=$(AllDBS)
    if [[ "${dbs}" =~ "${DbName}" ]]
    then
        echo "back db: ${DbName}"
        mysqldump --opt -h $DB_ADDR -u$DB_USER -p$DB_PASS $DbName 2>/dev/null | \
            gzip > ${BAK_DIR}/${DbName}-${CUR_TME}.sql.gz
        if [[ $? -eq 0 ]]
        then
            echo "$DbName 备份成功!"
            return 0
        else
            echo "$DbName 备份失败!"
            return 1
        fi
    else
        echo "${DbName}数据库不存在"
        exit $?
    fi
}

## db clean
function DbClean(){
    #echo "[ Run: $FUNCNAME ]"
    echo "clean db: ${DbName}"
    
    read -p "确认是否要清库 $DbName [y|n]: " enter
    if [[ "${enter}" == "n" ]]
    then
        return
    fi
    mysql -h ${DB_ADDR} -u${DB_USER} -p${DB_PASS} -e "DROP database ${DbName};" 2>/dev/null &&
        echo "$DbName 清除成功!" ||
        echo "$DbName 清除失败!"
}

## get cmd args
function GetArgs(){
    # get cmd args
    while test -n "$1"
    do
        case "$1" in
            -h | --help)
                 Help
                 exit
                 ;;
            -n | --dbname)
                 DbName=$2
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

## entry point
function Main(){
    # check back dir
    if [[ ! -d $BAK_DIR ]]
    then
        echo "back dir not exisit."
        mkdir $BAK_DIR
    fi
    # check db addr(if str is empty return true)
    if [[ -z $DB_ADDR ]] || [[ -z $DB_USER ]] || [[ -z $DB_PASS ]]
    then
        echo "db addr or user or password is error"
        return
    fi
    
    GetArgs $@
    # check cmd args
    [ $DbName == "" ] && Help && exit $?

    # 备份数据库并删除
    DbBack && DbClean
}

Main $@
