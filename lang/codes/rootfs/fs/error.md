####

[注意]:  
    alpine基础镜像运行容器报错:  
        docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "bash": executable file not found in $PATH: unknown  
    只需要根据基础镜像制作新的镜像:  
    FROM alpine:3.20.0  
    RUN apk add --no-cache bash  
    导出镜像:  
    docker export 运行中的容器名称 >name.tar  
