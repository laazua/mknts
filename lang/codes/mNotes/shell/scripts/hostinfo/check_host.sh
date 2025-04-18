#!/bin/bash

ips=('10.0.0.16')

printf "%-15s %-9s %-9s %-9s %-9s %-9s %-9s\n" "IP" "num(game)" "mem" "disk" "cpu(%)" "load" "conn"
for ip in ${ips[@]}
do
    ssh -q -tt ${ip} "sh ~/scripts/collector.sh"
    scp -q -p ${ip}:~/scripts/col.txt col.txt
    cip=$(cat col.txt|grep ip|awk -F':' '{print $2}')
    num=$(cat col.txt|grep num|awk -F':' '{print $2}')
    mem=$(cat col.txt|grep mem|awk -F':' '{print $2}')
    dsk=$(cat col.txt|grep dsk|awk -F':' '{print $2}')
    cpu=$(cat col.txt|grep cpu|awk -F':' '{print $2}')
    lod=$(cat col.txt|grep lod|awk -F':' '{print $2}')
    con=$(cat col.txt|grep con|awk -F':' '{print $2}')
    printf "\e[32m%-15s %-9s %-9s %-9s %-9s %-9s %-9s\n\e[0m" "${cip}" "${num}" "${mem}" "${dsk}" "${cpu}" "${lod}" "${con}"
done

rm ./col.txt -f
