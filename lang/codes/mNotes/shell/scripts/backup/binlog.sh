#!/bin/bash

## 通过binlog恢复数据

##登录mysql: mysql -h xxx -u xxx -p
##刷新binlog: mysql> flush logs;
##查询binlog: mysql> show binary logs;
##查询当前posiiton位置: mysql> show master status;
##查询指定binlog内容: mysql> show binlog events IN 'bin.000063' \G;

##1 找到发生事故时间点之前的一个数据备份

##2 清空误操作的库(清空之前先备份)

##3 将步骤1的备份数据导入数据库

##4 在binlog中核查误操作的的起始和结束时间点

##5 mysqlbinlog --start-position=xxx --stop-position=xxx binlog | mysql -h xxx -u xxx -p xxx



####
## 清理bin-log文件
## 清理单个bin文件: PURGE MASTER LOGS TO 'bin.xxx';
## 清理某个事件点之前的bin文件: PURGE MASTER LOGS BEFORE '2022-05-31 00:00:00';
## 清理3天前的bin文件: PURGE MASTER LOGS BEFORE DATE_SUB( NOW(), INTERVAL 3 DAY);
