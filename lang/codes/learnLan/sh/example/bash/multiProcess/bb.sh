#!/bin/bash
# 'cat xxx | while read LINE' 不建议使用这种写法


while read line;do
    (
    	echo $line
    	sleep 2
    )&
done < $1
wait

echo 'dddd'
