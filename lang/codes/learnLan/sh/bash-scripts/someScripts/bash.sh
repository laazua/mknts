#!/bin/bash
# name: bash.sh
# desc: bash script
# auth: Sseve
# date: xxxx-xx-xx

## 数据处理
# 变量: 变量命=值

function test_var() {
    # 字符串
    name="bobo"
    # 整型
    age=12
    # 浮点型
    score=90.5

    declare -i NUM   # 声明为整型变量
    declare -r NUM   # 声明为只读变量
    declare -x NUM   # 标记变量通过环境导出export
    declare -a NUM   # 声明数组
    declare -A NUM   # 声明为关联数组

    # 数组
    arr_a[0]=1
    arr_a[1]=2
    arr_a[2]=3
    echo ${arr_a[1]}
    echo ${arr_a[@]} ${arr_a[*]} ${arr_a[@]:1:2}
    
    declare -A asso1 asso2
    asso1[python]=one
    asso1[golang]=tow
    asso1[java]=three
    asso2=([python]=one [golang]=tow [java]=three)

    unset NUM    # 取消变量

    # 本地变量: 用户自定义的变量,定义在脚本或终端中,脚本或终端结束,变量失效.
    # 环境变量: 定义在用户家目录下的.bashrc或bash_profile文件中,用户私有变量,只能当前用户使用.
    # 内置变量: shell本身已经有的变量,有明确的名字和作用.
    echo ${name}

    return 0  # 默认返回函数最后一个命令执行完后的状态;也可给定一个0-256之间的数字
}

function test_echo() {
    echo -e "\033[30m 黑色 \033[0m"
    echo -e "\033[31m 红色 \033[0m"
    echo -e "\033[32m 绿色 \033[0m"
    echo -e "\033[33m 黄色 \033[0m"
    echo -e "\033[34m 蓝色 \033[0m"
    echo -e "\033[35m 紫色 \033[0m"
    echo -e "\033[36m 天蓝 \033[0m"
    echo -e "\033[37m 白色 \033[0m"

    return
}

function test_operation() {
    # 四则运算: + - * / % **
    expr 6 \* 2
    let a=5-3
    a=1; let a++
    r=$((100*3))
    echo "scale=2;5/3"|bc

    # 比较运算:
    # 整型: -eq -gt -lt -ge -le -ne
    # 字符串: == != -n -z 

    # 逻辑运算:
    # && 真真为真  真假为假  假假为假
    # || 真真为真  真假为真  假假为假
    # ！ 非假为真  非真为假
}

function test_if() {
    # if
    if [ conditon ]
      then
        commands
    fi

    # if...else
    if [ conditon ]
      then
        commands1
    else
        commands2
    fi

    # if...elif...else
    if [ conditon1 ]
      then
        commands1
    elif [ conditon2]
      then
        commands2
    else
        commands3
    fi

    ##
    if (( ... ))
      then
        commands1
    else
        commands2
    fi

    ## 
    if [[ ... ]]
      then
        commands
    fi

    ## 
    [ ... ] && commands
}

function test_for() {
    ##
    for var in {list}
      do
        commands
      done

    ##
    for var in a b c
      do
        commands
      done

    ## 
    for var in {1..10}
      do
        commands
      done

    ##
    for var in `seq 10`  # $(seq 10)
      do
        commands
      done

    ##
    for(( i=0;i<5;i++ ))
      do
        echo $i
      done

}

function test_while() {
    while [ conditon ]
      do
        commands
      done
}

function test_case() {
    case #var in
    pattern 1)
        commands1
        ;;
    pattern 2)
        commands2
        ;;
    pattern 3)
        commands3
        ;;
                 *)
        commands4
        ;;
    esac
}