#!/bin/bash
# 游戏服脚本配置

##zones##
if [[ "$#" = "1" ]] || [[ "$#" = "3" ]]; then
  GAME_PATH="/data/game/"
  SVN_URL="svn://gitee.com/banagame/dwy-wan-setup/tap_test"
  SVN_USER="wupan987"
  SVN_PASS=" kange944"
fi

##开服配置##
if [[ "$#" = "2" ]]; then
  GAME_DIR="/data/game/"
  GAME_ALIAS="syf"
  DB_USER="yunwei"
  DB_PASS="yunwei123"
  DB_URL="101.132.245.153"
  DB_PORT=3306
  DB_NAME="banams"
  SVN_URL="svn://gitee.com/banagame/dwy-wan-setup/tap_test"
  SVN_USER="wupan987"
  SVN_PASS="kange944"
fi

wrt_log() {
  if [[ ! -d "/home/gamecpp/.logs" ]];then
    mkdir /home/gamecpp/.logs
  fi
  d_time=$(date +"%Y%m%d")
  h_time=$(date +"[%Y-%m-%d %H:%M]")
  echo "${h_time} $1" >> /home/gamecpp/.logs/zones-${d_time}.log
}
