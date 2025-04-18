#!/bin/bash

## 使用mysqldump+mysqlbinlog备份恢复数据
## 参考: https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog-backup.html
## 将以下备份加入定期执行任务

## binlog备份
# mysqlbinlog --read-from-remote-server --host=host_name \
#    --user=xxx --password=xxx --raw --stop-never binlog.0000001
# 或者
# 直接本机打包备份binlog文件,然后传送到指定主机上存储

## 数据库备份
# mysqldump --host=host_name --all-databases --events --routines --master-data=2> dump_file

## 数据恢复
# mysql --host=host_name -u root -p < dump_file
# 查看binlog文件事件发生的起始和终止位置(mysqlbinlog binlog.00001)
# mysqlbinlog --start-position=27284 binlog.001002 binlog.001003 binlog.001004
#  | mysql --host=host_name -u root -p
## 或者
# mysqlbinlog --start-datetime  "0000-00-00 00:00:00" --stop-datetime "0000-00-00 00:00:00"
#  | mysql --host=host_name -u root -p
