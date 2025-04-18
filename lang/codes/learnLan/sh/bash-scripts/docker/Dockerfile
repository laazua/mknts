# 必须为第一个命令
FROM <image>:<tag>

# 维护者信息
MAINTAINER <name>

# 构建镜像时在容器中执行命令(一下时两种命令执行方式)
RUN <command>
RUN ["executable", "param1", "param2"]
# 例子
RUN yum update
RUN ["yum", "update"]

## 拷贝
# 将本地文件添加到容器中(tar类型的文件会自动解压)
ADD <src>... <dest>
ADD ["<src>"... "<dest>"]
#例子(添加所有以test.开头的文件到/mydir文件夹中):
ADD test.* /mydir
# 将本地文件添加到容器中(tar类型的文件不会自动解压)
COPY <src>... <dest>
COPY ["<src>",... "<dest>"]
# 注意: Docker Daemon会从编译目录寻找文件或目录;dest为镜像中的绝对路径或者相对于WORKDIR的路径

# 构建容器后调用,即在容器启动时才进行调用
CMD commadn param1 param2    # 执行shell内部命令
CMD ["executable", "param1", "param2"]    # 执行可执行文件,优先
CMD ["param1", "param2"]    # 设置了ENTRYPOINT,则直接调用ENTRYPOINT添加参数
# 例子
CMD ["/usr/bin/wc", "--help"]

# 为镜像添加元数据
LABEL <key>=<value> <key>=<value> <key>=<value> ...
# 例子
LABEL version="0.1" description="this is a example"

# 设置环境变量
ENV <key> <value>    # <key>之后的所有内容均会被视为<value>的组成部分.所以一次只能设置一个变量
ENV <key>=<value> ...    # 可以设置多个变量,每个变量为一个<key>=<value>键值对,如果<key>中包含空格用\来转义
# 例子
ENV name xiaoxiao xiaoli
ENV name=xiaoxiao age=12

# 指定外界交互的端口
EXPOSE <port> [<port>...]
# 例子
EXPOSE 80 443
EXPOSE 80
EXPOSE 2209/tcp 2209/upd
# 注意: EXPOSE并不会让容器的端口访问到主机。要使其可访问，需要在docker run运行容器时通过-p来发布这些端口，或通过-P参数来发布EXPOSE导出的所有端口

# 指定持久化目录
VOLUME ["/path/to/dir"]
# 例子
VOLUME ["/data"]
VOLUME ["/var/www", "/var/log/nginx", "/var/log/mysql"]
# 注意: 一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能:
# 1. 卷可以容器间共享和重用
# 2. 容器并不一定要和其它容器共享卷
# 3. 修改卷后会立即生效
# 4. 对卷的修改不会对镜像产生影响
# 5. 卷会一直存在，直到没有任何容器在使用它

# 工作目录,类似cd命令
WORKDIR /path/to/workdir
# 例子
WORKDIR /data    # 这是工作目录为/data
# 注意: 通过WORKDIR设置工作目录后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY等命令都会在该目录下执行。在使用docker run运行容器时，可以通过-w参数覆盖构建时所设置的工作目录

# 指定传递给构建运行时的变量
ARG <name>[=<default value>]
# 例子
ARG site
ARG user=nginx

# 设置镜像触发器
ONBUILD [INSTRUCTION]
# 例子
ONBUILD ADD . /app/src
ONBUILD RUN /usr/local/bin/python-build --dir /app/src
# 注意: 当所构建的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被钥触发