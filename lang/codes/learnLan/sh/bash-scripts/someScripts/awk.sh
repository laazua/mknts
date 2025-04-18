#!/bin/bash
# awk语句只能被单引号包裹

# 描述: 按行读取文本并进行相应的操作
# 用法: awk [option] '[pattern] + [action]' filename
# 不同动作之间最好用{}包裹，并用;隔开，如下示例
# 示例:
#    cat test |awk 'BEGIN{i=1;j=1};{if(NR%2==1){A[i]=$0;i++}};{if(NR%2==0){B[j]=$0;j++}};END{for(a=0;a<length(A);a++){print A[a], B[a]}}'
#    该示例用于将文本内的奇数行与偶数行放在同一行，用空格隔开.

# 内建变量
# $0         当前记录(这个变量中存放着整个行的内容)
# $1~$n      当前记录的第n个字段,字段间由FS分隔
# FS         输入字段分隔符,默认是空格或tab
# NF         当前记录中的字段个数,就是有多少列
# NR         已经读出的记录数,就是行号,从1开始,如果有多个文件的话,这个值也是不断累加中
# FNR        当前记录数,与NR不同的是,这个值会是各个文件自己的行号
# RS         输入的记录分隔符,默认为换行符
# OFS        输出字段分隔符,默认也是空格
# ORS        输出的记录分隔符,默认是换行符
# FILENAME   当前输入文件名

# 操作符：
#    算数操作符：
#        + - * / % ++ -- ^(**) += -= *= /= %= ^=(指数赋值运算)
#    关系运算符：
#        > < == != >= <=
#    逻辑运算：
#        && || !
#    三元运算符：
#        condition expression ? statement1 ：statement2

# 数组:
#    访问数组:  for(i in ARRAY)
#              如果要按数组下标进行索引，需要在定义数组的时候给定下标(ps:数组不是内联数组)

# 正则表达式:
#    同shell

# 控制流程:
# if(condition){action}
# if(condition){action}else(action)
# if(condition){action}else if(condition){action}...

# 循环:
#    for(initialisation;condition;increment/decrement){action}
#    while(condition){action}
#    do{action}while(condition)
#
#    break：结束循环
#    continue：循环体内结束本次循环

# awk '$2>0 {print $0}' test.txt
# awk '$4==1 && $5=="test" || NR==1' test.txt

# 格式化输出
# awk '$1==0 && $6=="test" || NR==1 {printf "%-20s %-20s %s\n", $4, $5, $6}' test.txt

# 指定分隔符
# awk 'BEGIN{FS=":"} {print $1, $3, $5}' /etc/passwd
# awk -F: '{print $1, $3, $5}' /etc/passwd
# awk -F '[;:]' 指定多个分隔符

# awk -F: '{print $1, $3, $5}' OFS=="\t" /etc/passwd

# 字符串匹配
# awk '$6 ~ /FIN/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" test.txt
# ~表示模式开始, //中的字符串是模式,这是个正则表达式的匹配
# awk '/test/' test.txt
# awk '/test|foo/' test.txt 匹配test或foo
# awk '!/test/' test.txt 取反

# $ 脚本方式: cat cal.awk
# 运行脚本: awk -f cal.awk score.txt

# 更多参考: http://www.gnu.org/software/gawk/manual/gawk.html
