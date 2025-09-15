### golang

- **项目打包c静态依赖库为独立的二进制文件**
1. CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o OutName  
2. 减小编译文件体积: 
   - go build -ldflags "-w -s" -o optimizedApp  
   - strip optimizedApp  
   - upx --best optimizedApp  
3. 编译优化:  
   - go build -gcflags="all=-l -B" -o optimizedApp 

4. 标准库之外的核心库
   - https://pkg.go.dev/golang.org/x