#!/bin/bash
#参考 https://www.jianshu.com/p/5fd32e10cce3
#该脚本放在项目的根目录下,即../wechat, wechat为项目名
#src文件夹下必须有main包(文件夹),放程序入口
#编译完成之后可执行文件放在项目根路径下的bin文件夹下
#项目的根目录根路径下必须有bin,src这两个文件夹
#wechat
#|_ bin/
#|    |_main 程序编译后的可执行文件
#|
#|_ build.sh
#|_ pkg/
#|_ src/
#     |_main/
#     |    |_variable.go
#     |_study/
#            |_Constant.go
#            |_WeChatHander.go
#            |_test.go
#            |_test1/
#            |_test1.go
# build.sh脚本用于编译go项目代码

# 当前路径,也就是sh文件的路径
ROOT=$(cd $(dirname $0)/;pwd)

# src目录
SRC=$ROOT/src

# 列出src目录下的一级文件
SRCS=$(ls -l $SRC/ | awk '/^d/ {print $NF}')

# 将当前的源码目录导入到GOPATH
GOPATH=$GOPATH
for i in $SRCS
do
	tmp_dir=$SRC/$i
	GOPATH="$tmp_dir:$GOPATH"
done

# 获取GOPATH的最后一个字符,上面的循环会导致在路径最面加上':'符号
 Last_Char=${GOPATH: -1}
# 如果最后一个字符是':'符号
if [ "Last_Char" == ":" ];then
	# 去掉最后一个字符
	GOPATH=${GOPATH%?}
fi

echo $GOPATH

export GOPATH=$GOPATH
export GOBIN=$ROOT/bin
export TMPDIR="/tmp"

# 编译
cd "$SRC/main" && go install

exit 0
