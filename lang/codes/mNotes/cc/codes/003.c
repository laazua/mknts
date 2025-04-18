#include <stdio.h>

int main(void)
{
    // 函数
    int c = add(1, 2);
    printf("c = %d\n", c);
  
    return 0;
}

int add(int a, int b)
{
    return a + b;
}
