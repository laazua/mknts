# 先安装docker并设置好国内镜像源

# docker search mysql[5|8]

# docker pull images

# docker images    查看镜像

# docker run -d -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 --privileged=true -v /data/mysql5:/opt/app-root/src --name mysql5 centos/mysql-57-centos7   启动

# docekr inspect  容器ID  查看容器信息

# docker logs   容器ID    查看容器启动日志

# docker exec -it 8cb1b7aafe0d bash

# docker exec -it 8cb1b7aafe0d bash && mysql -uroot -p 进入容器中的mysql

# navicat  mysql8
# update user set host='%' where user='root';&& flush privileges; && grant all privileges on *.*  to 'root'@'%'; && ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';