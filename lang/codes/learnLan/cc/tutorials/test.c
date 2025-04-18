#include <stdio.h>

int main(void)
{
    int a[10] = {0}, i;
    *a = 100;
    *(a+2) = 200;
    for(i=0;i<=9;i++){
        printf("%d\n", a[i]);
    }
    return 0;
}