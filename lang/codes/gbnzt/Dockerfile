# 项目编译
# CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

# 基础镜像
FROM alpine:3.12
# 维护者
MAINTAINER Sseve
# docker build时执行命令
RUN mkdir -p "/data/app/config" \
&& ln -sf /dev/stdout /data/app/bnzt.log
# 进入工作目录
WORKDIR "/data/app"
# 拷贝可执行文件
COPY bnzt /data/app/bnzt
COPY config/app.yml /data/app/config/app.yml
# docker run时执行命令
ENTRYPOINT ["./bnzt"]