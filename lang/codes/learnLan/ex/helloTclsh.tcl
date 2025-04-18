#!/usr/bin/tclsh

# yum install tcl tk

####################################
#                                  #
# 算数运算符: +  -  *  /  %        #
# 关运运算符: ==  !=  >  <  >=  <= #
# 逻辑运算符: &&  ||  !            #
# 位运算符:   &  |  ^  <<  >>      #
# 三元运算符: ?:                   #
#                                  #
####################################
                                  
## 打印变量
puts "hello tclsh"
puts ${argc}
puts ${argv}

## 设置变量
set num 100
## 数组
set arra {1 2 3}
## 数组大小 puts [array size arra]

## 字典
set lang(python) 100
set lang(golang) 90
## 字典索引 [array names $lang]

## append arra 4
## lappend arra 0
## [llength $arra]

## 文件io
set  fd [open "fileName" r]

## if
# if {条件}elseif{}else{}

## switch
# switch string {
#     matchstring1 {
#         code1...
#     }
#     matchstring2 {
#         code2...
#     }
#     ...
#     matchstringn {
#         coden...   
#     }
# }

## while
# while {condition} {}

## for
# for {set i 0} {condition} {incr i++} {}

## foreach
# foreach index [array names lang] { puts "lang(${index})" }

## break continue