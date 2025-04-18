#!/bin/bash

# 参考：http://www.atguigu.com
echo "
    ## docker简介.
                              # # # # # # # # # # # # # # # # # # #
                              #                                   #       push       # # # # # # #     
                              #      images[tag]                  #   -------------> #           # 
                  build       #       ^    |                      #                  # registry  #
    Dockerfile ------------>  # commit|    |run                   #       pull       #           #
		              #       |	   |                      #   <------------- # # # # # # #
                              #       |    v                      # 
                              #     containers[stop,start,restart]#
                              # # # # # # # # # # # # # # # # # # #

    > 理念：一次构建,到处运行.
    > 官网：http://www.docker.com
    > 中文官网：https://www.docker-cn.com
    > 仓库：https://www.hub.docker.com

    ## docker安装
    > 系统内核版本2.6.32-431或者更高(uname -r)
    > 三要素：镜像，容器，仓库
            镜像 --> 类似面向对象中的类模板
	    容器 --> 类似面向对象中的类实例
	    仓库 --> 存放镜像的地方
    > centos6.8: yum install -y epel-release docker-io (/etc/sysconfig/docker)
    > centos7 :  参考官网(/etc/docker/daemon.json)

    ## 云加速
    https://dev.aliyun.com/search.html(注册一个帐号，并登陆,获取云加速地址)
    配置：
        mkdir -p /etc/docker && vim /etc/docker/daemon.json && echo  {"registry-mirrors": [""https://{自己的编码}.mirror.aliyuncs.com] } > /etc/docker/daemon.json

    ## 常用命令
    > 帮助命令
    	docker version
    	docker info
    	docker --help
    > 镜像命令
    	docker images    列出本机镜像
	docker images -a    列出本地所有镜像(含中间层)
	docker images -q    只显示镜像ID
	docekr images --digests    显示摘要信息
        docker images --digests --no-trunc    显示完整的
	docekr search [-s 30] NAME    在dockerhub上搜索镜像超过点赞数超过30的
	docekr pull NAME    在配置的公共仓库里拉取镜像
	docker rmi [NAME1|NAME2...|key-id1|key-id2...]
    > 容器命令
    	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
	    OPTIONS说明：
	    --name="容器新名字",为容器指定一个名字
	    -d: 后台运行容器,并返回容器ID,即启动守护式容器
	    -i: 以交互式运行容器,通常与-t同时使用
	    -t: 为容器重新分配一个伪输入终端,通常与-i同时使用
	    -P: 随机端口映射
	    -p: 指定端口映射,有以下形式：
	    	ip:hostPort:containerPort
		ip::containerPort
		hostPort:containerPort
		containerPort
        docker ps    列出本机运行的容器
	    -a: 列出当前运行的和过往运行过的所有容器
	    -l: 列出上一次运行的容器
	    -n 3: 列出上3次运行的容器
	exit: 登入运行的容器时，退出并停止运行的容器
	ctrl + P + Q: 退出容器,但不停止容器
	docker start containerID    启动容器
	docker stop  containerID    停止容器
	docker kill containerID    强制停止容器
	docker rm containerID    删除已经停止的容器(-f 强制删除容器)
	docker rm -f $(docker ps -a -q) | docker ps -a -q|xargs docker rm    一次删除多个容器
	docker logs -t -f --tail 3 containerID    查看运行容器的日志
	docker top containerID    查看运行容器中的进程情况
	docker ps   -q    查询运行容器的DI
	docker inspect containerID    查看运行容器的细节
	docker attach containerID    进入运行的容器(与docker exec -it containerID /bin/bash)
	docker exec -t containerID ls -l /tmp    不进入容器执行命令
	docker cp containerID:path/fileName  path    将容器中的文件拷贝到宿主机上

	docekr commit -a='作者' -m='提交信息' containerID 目标镜像名/标签:3.1    以运行的容器为基础，修改后提交为新的镜像模板


    ## 镜像
    	UnionFS(联合文件系统)：Union文件系统(UnionFS)是一种分层,轻量级并且高性能的文件系统,它支持对文件系统的修改作为一次提交来一层层的叠加,
                           同时可以将不同的目录挂载到同一个虚拟文件系统下,Union文件系统是docker镜像的基础。镜像可以通过分层来进行继承,基
			   于基础镜像(没有父镜像),可以制作各种具体的应用镜像。
    	加载原理：bootfs(boot file system)主要包含bootloader和kernel, bootloader主要引导加载kernel,linux刚启动时会加载bootfs文件系统,在docker
              镜像的最底层是bootfs。这一层与我们典型的linux/unix系统是一样的,包含boot加载器和内核。当boot加载完成之后整个内核就都在内存中
	      了，此时内存的使用权以由bootfs转交内核,此时系统也会卸载bootfs。bootfs包含的就是linux中典型的/dev,/proc,/bin,/etc等目录和文件
	      rootfs就是各种不同linux发行版。
    
    ## 容器数据卷
    	数据持久化&&数据共享+容器间继承
	docekr run -it 镜像名或镜像ID
	docker run -it -v 宿主机绝对路径目录:容器内目录路径:权限(rw,ro,wo) 镜像名

    ## Dockerfile
    Dockerfile是构建镜像的源码文件
    	FROM  基础镜像
	MAINTAINER  镜像的维护者和邮箱地址
	RUN  镜像构建时需要运行的命令
	EXPOSE  当前镜像生成容器时对外暴露的端口
	WORKDIR  指定在创建容器后，终端默认登陆时的工作目录
	ENV  构建镜像时设置环境变量
	ADD  将宿主机目录下的文件拷贝到镜像,并且ADD命令会自动处理RUL和解压tar压缩包
	COPY  拷贝文件和目录到镜像中。将从构建上下文目录中<源路径>的文件/目录复制到新的一层的镜像内的<目标路径>位置(COPY src dest,  COPY["src", "dest"])
	VOLUME  容器数据卷,用于数据保存和持久化
	CMD  指定容器运行是要执行的命令,Dockerfile中可以有多个CMD命令,但只有最后一个生效,CMD会被docker run之后的命令参数替换
	ENTRYPOINT  指定容器运行时要执行的命令,与CMD一样,都是指定容器启动程序及参数(容器启动时追加的参数不会覆盖镜像内最后执行的命令)
	ONBUILD  当构建一个被继承的Dockerfile时运行命令，父镜像在被子继承后父镜像的onbuild被触发
    docker build -f Dockerfile文件的绝对路径 -t 新镜像的名字:TAG .(建议到Dockerfile所在路径执行此命令)
	
    ## 镜像发布
    阿里云创建仓库
    docekr commit -a='作者' -m='提交信息' containerID 目标镜像名/标签:3.1    以运行的容器为基础，修改后提交为新的镜像模板
    docker login --username= 仓库地址(registry.cn-hangzhou.aliyuncs.com)
    docekr tag [imageID] registry.cn-hangzhou.aliyuncs.com/seve/mytest:[镜像版本号]
    docekr push registry.cn-hangzhou.aliyuncs.com/seve/test:[镜像版本号]
    注: seve/test --> 命名空间/镜像名字,需要在云仓库上创建
"

