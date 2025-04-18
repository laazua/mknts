#/bin/bash
# mysql主从
echo "
    原理: 
    master(binlog dump thread): master库中有数据更新时,将事件类型写入binlog日志;并创建log dump线程通知slave库存在数据更新.
    slave(I/O thread): 请求master,master返回binlog的名称以及当前数据更新的位置,binlog日志文件位置的副本;然后将binlog保存在
                       中继日志中(relay log, 记录数据更新信息)

    主从配置:
      -- master:
         搭建master并配置好相应的参数后启动
         查看master状态: show master status;
         登录master创建用户用于数据同步: create user 'backup'@'%' identified by'123456';
         授权: grant all on backupdatabase.* to 'backup'@'%';
      -- slave:
         创建同步的数据库: create database syncdatabase default character set utf8mb4 collate utf8mb4_general_ci;
         授权: grant all on syncdatabase.* to 'backup'@'%';
         配置slave并启动.
"