### golang

- **项目打包c静态依赖库为独立的二进制文件**
1. CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o OutName