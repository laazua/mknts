/*
函数指针: 实质是一个指针,指向一个函数地址
*/

#include <stdio.h>

// 定义一个接受两个整数参数并返回它们和的函数
int add(int a, int b)
{
    return a + b;
}

// 定义一个接受两个整数参数并返回它们差的函数
int subtract(int a, int b)
{
    return a - b;
}

int main()
{
    // 声明一个函数指针，该指针可以指向接受两个整数参数并返回整数的函数
    int (*operation)(int, int);

    // 指向 add 函数的函数指针
    operation = add;

    // 调用 add 函数
    int result_add = operation(5, 3);
    printf("Addition result: %d\n", result_add);

    // 指向 subtract 函数的函数指针
    operation = subtract;

    // 调用 subtract 函数
    int result_subtract = operation(5, 3);
    printf("Subtraction result: %d\n", result_subtract);

    return 0;
}
