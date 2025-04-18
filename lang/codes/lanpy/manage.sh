#!/usr/bin/env bash

## 项目运行管理
## 根据实际情况调整此脚本

# 设置 PYTHONPATH
export PYTHONPATH=

# 项目状态检查
function check() {
  echo "check ..."
}

# 关闭项目
function stop() {
  echo "stop ..."
}

# 启动项目
function start() {
  echo "start ..."
}

function _help() {
  echo
  echo "Usage: $0 [check|stop|start]"
  echo
}

# 脚本入口
function main() {
  case $1 in
  "check")
    check
    ;;
  "stop")
    stop
    ;;
  "start")
    start
    ;;
  *)
    _help
    ;;
  esac
}

main "$@"