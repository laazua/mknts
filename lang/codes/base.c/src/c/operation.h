#ifndef _OPERATION_H_
#define _OPERATION_H_

#include <stdio.h>

// 指针函数类型
typedef int (*Operation)(int, int);

// 实现指针函数类型
int add(int a, int b);
int sub(int a, int b);

#endif // _OPERATION_H_
