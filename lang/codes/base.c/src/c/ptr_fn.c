/*
// 指针函数: 实质是一个函数返回一个指针
*/
#include <stdio.h>

int *test_ptr_fn(void)
{
    int *ptr = NULL;
    int num = 250;
    ptr = &num;

    return ptr;
}

int main(void)
{
    int *r = test_ptr_fn();
    fprintf(stderr, "%d\n", *r);
    return 0;
}