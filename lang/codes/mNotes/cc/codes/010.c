// 指针
#include <stdio.h>

int main(void) {
    int *p = NULL, num;
    p = &num;
    num = 100;
    printf("num = %d\n", num);
    printf("*p = %d\n", *p);
   
    printf("%p\n", p);
    *p = 200; /*警告*/
    printf("%p\n", p);

    return 0;
}

