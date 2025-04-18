### docker

* *安装*
```
- yum install -y yum-utils device-mapper-persistent-data lvm2
- yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
- yum install -y docker-ce
```

* *启动docker*
```
  - systemctl start docker
  - systemctl enable docker
```

* *docker-compose安装*
```
   - github/docker/compose下载稳定版本的docker-compose到指定服务器上.
   - 将docker-compose移动到/usr/bin/目录下
```