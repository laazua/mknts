#!/usr/bin/bash

## 运行脚本
## 在实际部署时, 部署的路径中包如下文件:
##     1. .env
##     2. manage.sh
##     3. taoist-0.0.1-py3-none-any.whl

# 安装名字
project_name=taoist
# 安装路径
project_path=/opt/taoist
# 安装包名
project_packge=taoist-0.0.1-py3-none-any.whl
# 安装包源
pkg_source=http://mirrors.aliyun.com/pypi/simple

### 设置环境变量
# 可执行程序路径
export PATH=$PATH:$project_path/bin
# 程序的安装路径
export PYTHONPATH=$project_path
# 运行模式: dev|test|prod
export MODE=test

function run {
  check && echo "${project_name} is running ..." && exit
  if [ -f ${project_path}/bin/${project_name} ];then
    nohup ${project_path}/bin/$project_name >>logs/app.log 2>&1 &
    sleep 1
    echo "${project_name} start success"
  else
    echo "Please: pip install $project_packge -t $project_path -i $pkg_source"
  fi
}

function stop {
  pgrep ${project_name}
  if [ $? -eq 0 ];then
    pkill ${project_name} && sleep 2 && echo "${project_name} stop success"
  else
    echo "${project_name} is stopped ..."
  fi
}

function check {
  # gunicorn模块启动时,会存在该文件
  pgrep ${project_name} && return $?
}

function remove {
  if [ -d "${project_path}" ];then
    rm -fr ${project_path}/* && \
      echo "remove ${project_name} success ..."
  else
    echo "${project_name} already uninstall !"
  fi
}

## 输出红色
function echo_red(){
    echo -e "\e[31m$1\e[0m"
}

## 输出绿色
function echo_green(){
    echo -e "\e[32m$1\e[0m"
}

function help {
  echo
  echo "  Usage: bash $0 up|down|check"
  echo "          up         启动项目."
  echo "          down       关闭项目."
  echo "          check      检测项目."
  echo "          uninstall  卸载项目."
  echo
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
      uninstall)
        remove
        ;;
      *)
        help
    esac
}

main $@
