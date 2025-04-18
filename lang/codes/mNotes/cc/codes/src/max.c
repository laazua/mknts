#include <stdio.h>
#include "max.h"

int num = 100;

int max(int a, int b)
{
    return a>b?a:b;
}


// static定义的对象只能在本文件中使用
static int age = 18;
static int getAge(int a)
{
    return a;
}

void print(void)
{
    printf("%d\n", getAge(age));
}
