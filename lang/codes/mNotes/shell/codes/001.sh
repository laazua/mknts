#!/bin/bash

## 斜杠转圈

while :
do
    echo -n -e "\033[5m-\033[0m\b"
    sleep 0.25
    echo -n -e "\033[5m/\033[0m\b"
    sleep 0.25
    echo -n -e "\033[5m|\033[0m\b"
    sleep 0.25
    echo -n -e "\033[5m\\\\\033[0m\b"
    sleep 0.25
done
