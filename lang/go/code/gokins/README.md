### gokins

[描述]  
1. 自动发版工具
2. 发版模板如下:
```
task:
  name: taskName
  steps:
  - name: stepName
    cmd: execute command
  - name: stepName
    cmd: execute command
  - name: stepName
    cmd: execute command

  ...
```

[打包]
1. 安装statik工具: go install github.com/rakyll/statik@latest
2. statik 生成代码: ~/go/bin/statik -src=staticfiles   (staiticfiles为打包的静态资源文件)
3. main.go中引入: 具体参考main.go文件
4. 编译: make