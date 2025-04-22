#!/usr/bin/bash

## 运行脚本
## 在实际部署时, 部署的路径中包如下文件:
##     1. .env
##     2. run.bash
##     3. fksrv-0.0.1-py3-none-any.whl

# 安装名字
project_name=fksrv
# 安装路径
project_path=/opt/fksrv
# 安装包名
project_packge=fksrv-0.0.1-py3-none-any.whl
# 安装包源
pkg_source=http://mirrors.aliyun.com/pypi/simple

# 设置环境变量
export PATH=$PATH:$project_path/bin
export PYTHONPATH=$PYTHONPATH:$project_path

function run {
  check && echo "${project_name} is running ..." && exit
  if [ -f ${project_path}/bin/${project_name} ];then
    nohup $project_name >/dev/null 2>&1 &
    sleep 1
    echo "${project_name} start success"
  else
    echo "Please: pip install $project_packge -t $project_path -i $pkg_source"
  fi
}

function stop {
  if [ -f ${project_name}.pid ];then
    local pid=$(cat ${project_name}.pid)
    kill $pid && sleep 2 && echo "${project_name} stop success"
  else
    echo "${project_name} is stopped ..."
  fi
}

function check {
  if [ -f ${project_name}.pid ];then
    return 0
  else
    return 1
  fi
}

function main {
    case $1 in
      up)
        run
        ;;
      down)
        stop
        ;;
      check)
        check && echo "${project_name} running ..." || \
          echo "${project_name} is stopped ..."
        ;;
      *)
        echo
        echo "usage: $0 up|down|check"
        echo
        exit
    esac
}

main $@
