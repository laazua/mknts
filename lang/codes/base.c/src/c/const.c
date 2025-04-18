#include <stdio.h>

int main()
{
    int a = 100;
    int const *p = &a; // *p = 300;  不能通过指针p来修改a的值

    a = 200;

    int *const q = &a; // 可以通过指针q来修改a的值, 但是指针q在指向a的地址后就不能修改了
    *q = 400;

    printf("%d  %d %d\n", a, *p, *q);

    int b = 250;
    const int *const o = &b;

    int c = 500;
    //o = &c;

    printf("%d  %d\n", c, *o);

    return 0;
}
