// 函数
#include <stdio.h>

// 函数声明
int add(int a, int b);
int pls(int a, int b);

// 定义一个函数指针别名fun
typedef int (*fun)(int, int);

int main(void) 
{
    // 函数普通调用
    int sum = add(1, 2);
    printf("%d\n", sum);

    // 函数指针(函数回调)
    // 声明函数指针时要提供函数的类型(返回类型和形参类型，不包括函数名和形参名)
    // int (*fn)(int, int);

    // add()回调示例
    int add_result = cnt(add, 1, 2);
    printf("%d\n", add_result);

    // pls()回调示例
    int pls_result = cnt(pls, 1, 2);
    printf("%d\n", pls_result);
    
    return 0;
}

// 函数定义
int add(int a, int b) 
{
    return a + b;
}

int pls(int a, int b) 
{
    return a * b;
}

int cnt(fun fn, int a, int b)
{
    int ret =  (*fn)(a, b);
    return ret;
}
