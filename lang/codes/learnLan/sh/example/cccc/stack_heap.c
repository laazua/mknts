/*
数据结构中堆栈（实际编程可实现）
数组:静态栈
链表：动态栈
堆：一种特殊的完全二叉树

内存中的堆栈(c语言中分配方式)
从静态存储区域分配：由编译器自动分配和释放，即内存在程序编译的时候就分配好了，这块内存在程序整个运行期间都存在，直到程序运行结束才释放;如：全局变量与static
在栈上分配: 由编译器分配和释放，即函数执行时，函数内局部变量的存储但愿都可以在栈上创建，函数执行完毕这些存储单元自动释放(效率高，容量有限)
在堆上分配: 程序员手动申请和释放，即生存周期由程序员决定(使用灵活,但是申请了必须释放) <--> 也称动态内存分配
*/

#include <stdio.h>
#include <malloc.h>

int main(void)
{
    //在栈上分配
    int a_stack = 100;
    int b_stack = 200;
    int c_stack = 300;
    printf("栈: 向下\n");
    printf("a_stack = 0x%08x\n", &a_stack);
    printf("b_stack = 0x%08x\n", &b_stack);
    printf("c_stack = 0x%08x\n", &c_stack);
    printf("--------------------\n");
    //堆上分配
    char *a_heap = (char *)malloc(4);
    char *b_heap = (char *)malloc(4);
    char *c_heap = (char *)malloc(4);
    printf("堆：向上\n");
    printf("a_heap = 0x%08x\n", a_heap);
    printf("b_heap = 0x%08x\n", b_heap);
    printf("c_heap = 0x%08x\n", c_heap);
    //释放堆内存
    free(a_heap);
    a_heap = NULL;
    free(b_heap);
    b_heap = NULL;
    free(c_heap);
    c_heap = NULL;

    return 0;
}