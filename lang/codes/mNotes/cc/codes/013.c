#include <stdio.h>

int main(void)
{
    // 指针是const
    // 表示指针一旦初始化指向某个地址,就不能指向其他地址
    // p++ 会报错(指针运算报错)
    int *const p;
    // 指针所指向的地址是const
    // *q = 100报错
    const int *q;  

    int i;

    int *const p3 = &i; 

    const int* p1 = &i;
    int const* p2 = &i;

    return 0;
}
