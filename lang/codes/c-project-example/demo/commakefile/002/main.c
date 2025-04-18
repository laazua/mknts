#include <stdio.h>

extern void funcx();
extern void funcy();

int main(void)
{
    funcx();
    funcy();
    return 0;
}
