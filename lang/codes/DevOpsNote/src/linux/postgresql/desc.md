### postgresql

[源码安装]  
1. 下载源码: wget https://ftp.postgresql.org/pub/source/v16.4/postgresql-16.4.tar.gz
2. 解压源码: tar -xf postgresql-16.4.tar.gz
3. 环境准备: apt install build-essential libreadline-dev zlib1g-dev && mkdir /usr/local/pgsql
4. 编译安装: cd postgresql-16.4 && ./configure --prefix=/usr/local/pgsql/ --without-icu && make && make install
5. 创建用户: useradd -m postgres -d /data/postgresql/ 
6. 创建数据目录: mkdir -p /data/postgresql && chown postgres:postgres -R /data/postgresql
7. 初始化数据库: sudo -i -u postgres && /usr/local/pgsql/bin/initdb -D /data/postgresql/
8. 创建启动数据库服务: vim /etc/systemd/system/postgresql.service
```
[Unit]
Description=PostgreSQL Database Server
After=network.target

[Service]
Type=forking
User=postgres
Group=postgres
ExecStart=/usr/local/pgsql/bin/pg_ctl start -D /data/postgresql -l /data/postgresql/logfile
ExecStop=/usr/local/pgsql/bin/pg_ctl stop -D /data/postgresql
ExecReload=/usr/local/pgsql/bin/pg_ctl reload -D /data/postgresql

[Install]
WantedBy=multi-user.target
```
9. sudo systemctl daemon-reload && sudo systemctl enable postgresql && sudo systemctl start postgresql
10. 备注：
```
项目配置: /data/postgresql/pg_hba.conf && /data/postgresql/postgresql.conf
```
11. 连接数据库: /usr/local/pgsql/bin/psql -h localhost -p 5432 -U postgres