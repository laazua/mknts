#### golang学习

* *基础学习* 
    * [hello world](/go/codes/g001.go)
    * [变量](/go/codes/g002.go)     
    * [常量](/go/codes/g009.go)
    * [类型](/go/codes/g003.go)    
    * [数组,切片,字典,列表](/go/codes/g004.go)
    * [结构控制](/go/codes/g005.go)
    * [函数](/go/codes/g006.go)
    * [异常](/go/codes/g007.go)
    * [恢复异常](/go/codes/g014.go)
    * [结构体](/go/codes/g008.go)    
    * [接口方法](/go/codes/g010.go)
    * [管道](/go/codes/g012.go)
    * [管道监控](/go/codes/g013.go)
    * [并发](/go/codes/g011.go)
    * [泛型](/go/codes/g015.go)
    * [大文件下载服务器](/go/codes/g016.go)

* *github参考*
    * [基础语法](https://github.com/callicoder/golang-tutorials)

* *设计模式*
  * [参考](https://juejin.cn/post/6859015515344633863)
  * [参考](https://refactoringguru.cn/design-patterns/go)

* *标准库*
  * [参考](https://studygolang.com/pkgdoc)

* *书籍*
  * [golang](https://www.kancloud.cn/uvohp5na133/golang/933987)
  * [go语言设计与实现](https://draveness.me/golang/)
  * [go语言高级编程](https://chai2010.cn/advanced-go-programming-book/)
  * [书籍](https://www.topgoer.cn/)
  * [go教程](https://www.topgoer.com/)
  * [go语言编程之旅](https://golang2.eddycjy.com/)
  * [go-programming-tour-book](https://github.com/go-programming-tour-book/)
* [算法](https://github.com/TheAlgorithms/)

* *其他*
  * [各种教程](https://www.tizi365.com/)
  * [duoke360](https://www.duoke360.com)
* **工程目录结构**
```
  .
  |-- README.md
  |-- api/
  |-- cmd/
  |-- configs/
  |-- go.mod
  |-- go.sum
  |-- internal/
  |-- pkg/
  +-- test/
```

* *1.18vscode+环境配置*
```
  - vscode配置(settings.json)
    "gopls": {
        "build.experimentalWorkspaceModule": true
    },
    "go.inferGopath": true
  - GOPATH
    > go/
      - bin/
      - pkg/
      - src/
        - test1/
            - go.mod
        - test2/
            - go.mod
        - go.work
  
  go.work生成: cd src && go work init
```
