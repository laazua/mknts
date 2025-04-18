#!/bin/bash

# 用s命令替换
# sed "s/foo/bar/g" test.txt    把test.txt中所有的foo替换成bar后输出,不会更改原文本
# sed -i "s/foo/bar/g" test.txt    直接在原文本上更改

# 在每行行首加上字符#
# sed 's/^/#/g' test.txt
#sed '/dog/,+3s/^/# /g test.txt    +3表示连续3行


# 在每行行尾加上字符 ---
# sed 's/$/ --- /g' test.txt

# 常用正则
# ^表示行首, 如：/^#/以#开头
# $表示行尾, 如: /}$/以}结尾
# \<表示词首, 如: \<abc以abc为首的词
# \>表示词尾, 如: abc\>以abc结尾的词
# .表示任何单个字符
# *表示某个字符出现了0次或者多次
# []字符集合, 如：[abc]表示匹配a或b或c, [a-zA-Z]匹配所以26个字符, [^a]匹配非a的字符

# 替换指定内容
# sed "3,6s/foo/bar/g" test.txt  替换3到6行的文本

# 替换每行的第一个a
# sed "s/a/A/1" test.txt
# 替换每行的第二个a
# sed "s/a/A/2" test.txt
# 替换第一行第3个以后的a
# sed "s/a/A/3g"

# 匹配多个模式
# sed '1,3s/my/your/g; 3,$s/This/That/g' test.txt
# sed -e '1,3s/my/your/g' -e '3,$s/This/That/g' test.txt

# 使用&来当做被匹配的变量，然后可以在基本左右加点东西
# sed "s/foo/[&]/g" test.txt

# 在第2行前插入内容
# sed "2 i bar" test.txt

# 在第3行后追加内容
# sed "3 a foo" test.txt

# 匹配到某行后就追加内容
# sed "s/bar/a foo" test.txt

# 替换匹配到的内容
# sed "/bar/c foo" test.txt
# sed "2 c test" test.txt

# 把匹配到的行删除
# sed "/bar/d" test.txt

# 删除指定行
# sed "2 d" test.txt
# sed "2, 10 d" test.txt

# 打印匹配到的行
# sed -n "/bar/p" test.txt

# 打印匹配到的两个模式之间的内容
# sed -n "/bar/, /foo/p" test.txt
# sed -n "1, /bar/p" test.txt


# 参考: http://www.gnu.org/software/sed/manual/sed.html
