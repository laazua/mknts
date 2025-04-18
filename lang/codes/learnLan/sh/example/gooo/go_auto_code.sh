# 运行此脚本前先设置go代理
# 七牛云代理 https://github.com/goproxy/goproxy.cn, 设置方法如下:
# go env -w GO111MODULE=on
# go env -w GOPROXY=https://goproxy.cn,direct
# 阿里云代理 https/mirrors.aliyun.com/goproxy/, 设置方法如下:
# go env -w GO111MODULE=on
# go env -w GOPROXY=https//mirrors.aliyun.com/goproxy/,direct

# vscode
# vscode 中进行相关设置,参考：https://studygolang.com/articles/20219

#mkdir $HOME/go/{bin,pkg,src/{github.com, golang.org/x/}}
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct

go get -u -v github.com/josharian/impl
go get -u -v github.com/mdempsky/gocode
go get -u -v github.com/rogpeppe/godef
go get -u -v github.com/golang/lint/golint
go get -u -v github.com/lukehoban/go-find-references
go get -u -v github.com/lukehoban/go-outline
go get -u -v github.com/sqs/goreturns
go get -u -v golang.org/x/tools/cmd/gorename
go get -u -v github.com/tpng/gopkgs
go get -u -v github.com/newhook/go-symbols
go get -u -v github.com/peterh/liner github.com/derekparker/delve/cmd/dlv
go get -u -v golang.org/x/tools/cmd/guru

go env -w GO111MODULE=off
