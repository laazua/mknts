package introducntion

/*
参考:https://github.com/hyper0x
特点:
	1.静态类型,编译型的开源语言(源码可见)
	2.脚本化的语法,支持多种编程范式(函数式&面向对象)
	3.原生的并发编程支持(语言层面就支持并发)

安装:
	1.下载安装包
	2.解压安装包到/usr/local
	3.环境变量设置
		GOROOT: go安装目录
		GOPATH: go工作目录,可以指定多个工作目录

go常用命令:
	1.go run
		-n: 打印编译过程中所需要运行的命令,但不真正执行它们
		-v: 列出所有被编译的代码包的名称
		-work: 显示编译时创建的临时工作目录的路径,并且不删除它
		-x: 打印编译过程中所需运行的命令
	2.go build
		-a: 强制编译相关代码,不论它们的编译结果是否已经是最新
		-p: 并行编译,n为并行数量(cpu核数)
	3.go install
	4.go get
		-d: 只执行下载动作,而不执行安装动作
		-fix: 在下载代码包后将老版本的go代码修正为当前使用的go版本语法,而后再进行编译和安装
		-u: 利用网络来更新已有的代码包及其依赖包

go程序实体:
	变量、常量、函数、结构体和接口被统称为“程序实体”，而它们的名字被统称为“标识符”。
	标识符可以是任何Unicode编码可以表示的字母字符、数字以及下划线“_”。不过，首字母不能是数字或下划线。

go关键字:
	程序声明:
		import, package
	程序实体声明:
		chan, const, func, interface, map, struct, type, var
	程序流程控制:
		go, select, break, case, continue, default, defer, else, fallthrough, for, goto, if, range, return, switch

go跨平台编译:
	SET CGO_ENABLED=0
	SET GOOS=linux
	SET GOARCH=amd64
	编译

go module:
	go mod init moduleName
	go mod graph  展示依赖
	go mod download   下载依赖
	go mod tidy  删除不需要的依赖包
	go mod verify  验证依赖包
	go mod why  展示一些指定的依赖包关系
	go mod edit
	go mod vendor
*/
