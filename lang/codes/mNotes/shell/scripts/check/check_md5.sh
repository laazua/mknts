#!/bin/bash

MPATH=$(cd "$(dirname $0)"; pwd)

while read line
do
    conFile=$(echo $line | awk '{printf $1}')
    remotem=$(echo $line | awk '{printf $2}')
    locatem=$(md5sum $conFile)
    if [[ $remotem != $locatem ]]
    then
        echo $MPATH
    fi
done <a.txt
