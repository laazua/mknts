### build

- 编译环境参数设置
1. export GOMEMLIMIT=250MiB     # 设置GC内存限制,防止程序被OOM
2. export CGO_ENABLED=0         # 设置将c库编译到二进制文件中,让程序不需要外部依赖就可以独立运行
3. export GOOS=linux            # 设置程序运行的目标系统为linux
4. export GOARCH=amd64          # 设置程序运行的目标架构为amd64

- 项目测试
1. go test -race        # 检测数据竞争是否有问题

- 编译参数设置
1. go build -ldflags="-s -w"                   # 减少编译后程序体积
2. go build -ldflags="-X main.version=0.1.1"   # 编译时传递变量值到程序中