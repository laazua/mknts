#!/bin/bash
# shell并发执行策略
# (cmd)& + wait
# {cmd}& + wait
# bash script.sh & 
# function &
# wait

pidlist=()

for i in {1..100};do
    (
	echo $i
        sleep 2
    )&
    pidlist+=("$!") #记录后台进程的pid
done
wait
#echo ${pidlist[@]}
