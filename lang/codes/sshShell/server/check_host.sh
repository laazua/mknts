#!/bin/bash

## 作者: Sseve
## 日期: 2021-09-14
## 检查主机是否存活

WEB_URL="https://oapi.dingtalk.com/robot/send?access_token=db7054b9a5c5a8fb1fe441f36044cf13d0cbc707ee963b0ab85526e06c5c9a70"

ping_host() {
  if ping -c 1 $1 &>/dev/null; then
    echo 1
  else
    echo 0
  fi
}

send_msg() {
  local msg=$1
  curl -s ${WEB_URL} -H "Content-Type: application/json" -d "{\"msgtype\": \"text\",\"text\": {\"content\": \"${msg}\"}}" >/dev/null 2>&1
}

main() {
  source ./mg.cnf
  for ip in ${ip_list[@]}; do
    for((i=1;i<=3;i++)); do
      export num"$i"=$(ping_host ${ip})
      sleep 2
    done
    if [[ ${num1} -eq ${num2} ]] && [[ ${num2} -eq ${num3} ]] && [[ ${num3} -eq 0 ]]; then
      send_msg "SYF: ${ip} is death!" 
    elif [[ ${num1} -eq ${num2} ]] && [[ ${num2} -eq ${num3} ]] && [[ ${num3} -eq 1 ]]; then
      echo &>/dev/null
    else
      send_msg "SYF: ${ip} network delay!"
    fi
  done
  unset num1 num2 num3
}

main "$@"

