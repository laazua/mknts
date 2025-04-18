#!/bin/bash

# gameops工具开发时的管理脚本

master_ops(){
  cd cmd/master && go build
  cp -f master ../../release/master
  cp ../../config/master.yaml ../../release/master
}

servant_ops(){
  cd cmd/servant && go build
  cp -f servant ../../release/servant
  cp ../../config/servant.yaml ../../release/servant
}


case "$1" in
  master)
    master_ops
    ;;
  servant)
    servant_ops
    ;;
  *)
  echo "gameops工具开发时的管理脚本"
  echo "usage: $0 [master|servant]"
  echo "   master  构建并运行master程序"
  echo "   servant 构建并运行servant程序"
esac