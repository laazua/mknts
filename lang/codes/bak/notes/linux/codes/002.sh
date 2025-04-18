#!/bin/bash


doing(){
    local i=0
    local str=""
    local arry=("\\" "|" "/" "-")
    while [ $i -le 100 ];do
        local index=$((i%4))
        if [ $i -le 20 ];then
            local color=44
            local bg=34
        elif [ $i -le 45 ];then
            local color=43
            local bg=33
        elif [ $i -le 75 ];then
            local color=41
            local bg=31
        else
            local color=42
            local bg=32
        fi
        printf "\033[${color};${bg}m%-s\033[0m %d %c\r" "$str" "$i" "${arry[$index]}"
        sleep 0.05
        _=$((i=i+1))
        str+="#"
        
    done
    printf "\n"
}

doing
