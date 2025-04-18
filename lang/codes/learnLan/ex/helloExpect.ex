#!/usr/bin/expect -f

# yum -y install expect.x86_64

## 设置变量
set RightExit 0
set ErrorExit 1
set timeout 60
set user [lindex ${argv} 0]
set ip   [lindex ${argv} 1]

## 条件控制
# set num 1
# if {${num} < 5} {
#     puts "${num} < 5\n"
# } else {
#     puts "${num} > 5\n"
# }

# switch -- ${num} {
#  {}
#  {}
#  {}
# }

# while { ${num} < 10 } {}

# for { set i 0} { ${i} < 10 } { incr i } {}

# foreach i {1 2} {}

# function
# proc functionName { parament } {
#    set parament [expr ${parament} + 1]
#    return ${parament}
# }  
# 调用function: set fn [functionName ${fn}]

# 正则表达式
# if {[regexp {^[a-z]+$} ${num}]} {} else {}

if {${argc} != 2} {
    puts "命令行参数错误"
    exit ${ErrorExit}
}



# spawn 程序名(开启一个进程执行该程序)
# 启动一个进程执行ssh
spawn ssh ${user}@${ip}
expect {
    "connecting" {send "yes\r"}
    "password"   {send "123456\r"}
    "*#"         {send "echo aaa>/tmp/aaa.txt\r"}
    "*#"         {send "echo\r"}
}
