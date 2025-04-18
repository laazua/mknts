#!/bin/bash

## 让脚本每秒执行一次

# STEP的值必须能被60整除
STEP=30

for((i=0;i<60;i++)); do
  $(/bin/bash /root/scripts/check_process.sh)
  sleep ${STEP}
done

exit 0
