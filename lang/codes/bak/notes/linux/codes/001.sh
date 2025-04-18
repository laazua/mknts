#!/bin/bash

# ShellCheck检查脚本语法错误
# yum install ShellCheck
# 用法: shellcheck somescripts
# vscode: 搜索插件shellcheck并安装


# 一些shell编程中的错误与正确示例对比

# for file in $(ls *.sh) 错误
# 使用下面的方式循环文件列表
for file in *.a; do
    [ -e "$file" ] || continue
    echo "$file"
done

