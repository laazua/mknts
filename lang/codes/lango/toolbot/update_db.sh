#!/usr/bin/env bash

# 更新数据库文件
# 该脚本依赖：wget和unzip工具
set -e

MY_KEY=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
GZIP_FILE=geoip.zip
GZ_FILE=geoip.tar.gz

#wget "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${MY_KEY}&suffix=zip" -O ${GZIP_FILE} >/dev/null 2>&1
wget "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=${MY_KEY}&suffix=tar.gz" -O ${GZ_FILE} >/dev/null 2>&1
if [ $? -eq 0 ];then
  echo "download db data success!"
else
  echo "download db data failure!"
  exit
fi

#unzip ${GZIP_FILE} -d csv >/dev/null 2>&1
tar -xzf ${GZ_FILE} -C ./ && rm db -fr && mv $(ls |grep GeoLite2*) db
if [ $? -eq 0 ];then
  echo "update db data success!"
else
  echo "update db data failure!"
fi

# 清理
if [ -f ${GZIP_FILE} ];then
  rm ${GZIP_FILE}
fi

if [ -f ${GZ_FILE} ];then
  rm ${GZ_FILE}
fi