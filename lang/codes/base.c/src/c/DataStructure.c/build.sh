#!/usr/bin/bash

# 临时使用脚本编译
# SLIST_UP DLIST_UP CLIST_UP条件编译宏


#if [ "$1" = "slist" ];then
#    gcc -DSLIST_UP src/main.c src/slist.c -o slist
#    exit $?
#fi

#if [ "$1" = "dlist" ];then
#    gcc -DDLIST_UP src/main.c src/dlist.c -o dlist
#    exit $?
#fi

#if [ "$1" = "clist" ];then
#    gcc -DCLIST_UP src/main.c src/clist.c -o clist
#    exit $?
#fi

#echo "$0 [slist|dlist|clist]"


if [ ! -d build ];then
    mkdir build
fi

if [ ! -d bin ];then
    mkdir bin
fi

cd build

if [ "$1" = "slist" ];then
    cmake -DSLIST=on .. && make && mv slist ../bin && rm ../build -fr
    exit $?
fi

if [ "$1" = "dlist" ];then
    cmake -DDLIST=on .. && make && mv dlist ../bin && rm ../build -fr
    exit $?
fi

if [ "$1" = "clist" ];then
    cmake -DCLIST=on .. && make && mv clist ../bin && rm ../build -fr
    exit $?
fi

if [ "$1" = "stack" ];then
    cmake -DSTACK=on .. && make && mv stack ../bin && rm ../build -fr
    exit $?
fi

if [ "$1" = "map" ];then
    cmake -DMAP=on .. && make && mv map ../bin && rm ../build -fr
    exit $?
fi

echo "$0 [slist|dlist|clist|stack|map]"
