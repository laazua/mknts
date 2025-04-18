// 规定:头文件中只能有声明

// 避免都文件内容重复引用
// 如果没有定义_MAX_H_宏
// 就定义_MAX_H_宏并声明相关对象
#ifndef _MAX_H_
#define _MAX_H_
// 变量声明
extern int num;

// 函数声明
extern int max(int a, int b);
#endif

