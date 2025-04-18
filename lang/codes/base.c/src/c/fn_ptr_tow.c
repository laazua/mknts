/*
* 动态选择函数
* 函数指针数组
*/
#include <stdio.h>

// 类型枚举
typedef enum { 
    add = 1,
    sub,
    mul,
    div,
} Arithmetic;

// 函数指针类型
typedef int (*Operation)(int, int);

// 实现函数指针类型(加法)
int addition(int a, int b)
{
    return a + b;
}

// 实现函数指针类型(减法)
int subtraction(int a, int b)
{
    return a - b;
}

// 实现函数指针类型(乘法)
int multiplication(int a, int b)
{
    return a * b;
}

// 实现函数指针类型(除法)
int division(int a, int b)
{
    return a / b;
}

int main()
{
    /* 动态选择函数 */
    Operation operation;
    Arithmetic arithmetic = add;

    switch (arithmetic) {
        case add:
            operation = addition;
            break;
        case sub:
            operation = subtraction;
            break;
        case mul:
            operation = multiplication;
            break;
        case div:
            operation = division;
            break;
    }

    fprintf(stdout, "operation result: %d\n", operation(14, 11));

    /* 函数指针数组 */
    Operation operations[] = {addition, subtraction, multiplication, division};
    switch (arithmetic) {
        case add:
            fprintf(stderr, "operation add: %d\n", operations[0](10, 2));
            break;
        case sub:
            fprintf(stderr, "operation sub: %d\n", operations[1](10, 2));
            break;
        case mul:
            fprintf(stderr, "operation mul: %d\n", operations[2](10, 2));
            break;
        case div:
            fprintf(stderr, "operation div: %d\n", operations[3](10, 2));
            break;
    }
    
    return 0;
}
