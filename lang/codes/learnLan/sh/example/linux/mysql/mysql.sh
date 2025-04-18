#!/bin/bash

#https://www.kancloud.cn/devops-centos/centos-linux-devops/385181

echo '
  数据库同一个实例下考虑到并发操作
  # 两大存储引擎: MyISAM(不支持事务), InnoDB(支持事务)
    事务: 事务就是要保证一组数据库操作,要么全部成功,要么全部不成功.
    ACID(Atomicity, Consistency, Isolation, Durability, 即原子性, 一致性, 隔离性, 持久性)

  # sql语句在mysql各个功能模块中执行对过程:
                                     客户端
                                       |
             _ _ _ _ _ _ _ _ _ _ _ _ _\|/_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
            |                        连接器(管理连接,权限验证)             |
            |                       /     \                              |
            |                      /       \                             |
            |  (命中直接返回结果)查询缓存 --- 分析器(词法分析,语法分析)        |
            |                                |                           | --> server层
            |                               \|/                          |
            |                              优化器(执行计划生成,索引选择)    |
            |                                |                           |
            |                               \|/                          |
            |                              执行器(操作引擎,返回结果)        |
             - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                        |
                                       \|/
                                     存储引擎
  mysql> create table T(ID int primary key, c int);
  mysql> update T set c = c + 1 where ID = 2;

  ##索引##
    索引类比字典的目录
    常见索引模型:哈希表(键-值 结构), 适用memcached以及其他一些NoSQL引擎
	           二叉树,二叉树不适用与数据库引擎
               N叉树广泛用于数据库引擎中.
	           B+树

  ##锁##
    全局锁:给整个数据库加锁, 加全局读锁: Flush tables with read lock(FTWRL)或者set global readonly=true(不推荐使用); 释放锁： unlock tables
	表级锁:表锁:lock tables ... read/write,释放锁: unlock tables
	      metadata lock: 不需要显式使用,在访问一个表的时候会自动加上.保证读写的正确性.
	读锁之间不互斥,所以可以允许多个献策和嗯同时读一张表增删改查
	读写锁之间,写锁之间互斥,保证变更表结构操作的安全性;因此多个线程对同一张表加字段,同一时段只允许一个线程执行操作.
	行锁: 针对数据表中行记录的锁;
'

echo "
    # mysql系统配置优化,修改/etc/sysctl.conf
    # 增加tcp支持的队列数
    net.ipv4.tcp_max_syn_backlog = 65535
    # 减少断开连接时,资源回收
    net.ipv4.tcp_max_tw_buckets = 8000
    net.ipv4.tcp_tw_reuse = 1
    net.ipv4.tcp_tw_recycle =1 
    net.ipv4.tcp_fin_timeout =10
    # 打开文件数的限制，使用ulimit -a 查看目录的各位限制,可以修改/etc/security/limits.conf文件
    *soft nofile 65535 *hard nofile 65535
    
"




mysql_opt(){
	## create database
	create database tttt;

	## 授权
	CREATE USER 'test'@'%' IDENTIFIED BY '123456';
	grant all on tttt.* to 'test'@'%';

	## 查看用户权限
	#show grants for 'test'@'%';

	## 权限回收
	revoke all PRIVILEGES ON test.* from 'test'@'%';
	
	########################################################
	## mysql异步复制
	create user 'test'@'192.168.1.%' identified by '123456';
	grant replication slave on *.* to 'test'@'192.168.1.%';
	## 配置
	cat >>/etc/my.cnf<<EOF
	#Master 信息存储在表里
	master_info_repository = TABLE
	#Relaylog信息存储在表里
	relay_log_info_repository = TABLE
	#所有事务提交前,写入binlog
	sync_binlog = 1
	#角色是从库时,产生binlog。级联复制用
	log-slave-updates = 1
	#binlog日志开关及名字
	log-bin = mysql-bin
	#binlog日志格式
	binlog_format = ROW
	#server-id,唯一建议用ip地址
	server-id=168001230
EOF
	##查看主库position情况
	show master status \G;
	##从库执行
	change master to MASTER_HOST='192.168.2.2';

	######################################################
	## 备份 xtrabackup && innobackupex
	## Xtrabackup是一个对InnoDB做数据备份的工具，支持在线热备份（备份时不影响数据读写）,Xtrabackup有两个主要的工具：xtrabackup
	## innobackupex，其中xtrabackup只能备份InnoDB和XtraDB两种数据表，innobackupex则封装了xtrabackup，同时可以备份MyISAM数据表
	## Xtrabackup做备份的时候不能备份表结构、触发器等等.
	## 备注：xtrabackup不支持TokuDB的热备份，需要使用mysqldump或mysqlpump
	## 特点：
	## 备份过程快速、可靠；
	## 备份过程不会打断正在执行的事务；
	## 能够基于压缩等功能节约磁盘空间和流量；
	## 自动实现备份检验；
	## 还原速度快
	# 备份： ./xtrabackup --backup --target=/data/backup/ -uroot -p123.com -S /tmp/mysql3306.sock
	# 恢复：xtrabackup --prepare --target-dir=/tmp/backup
	#       xtrabackup --copy-back --target-dir=/tmp/backup --datadir=/data/mysql3306
	#       chown mysql.mysql  /data/mysql3306  -R && /etc/init.d/mysql.server start


	


}
