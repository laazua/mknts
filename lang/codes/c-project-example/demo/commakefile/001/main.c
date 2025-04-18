#include <stdio.h>

extern void funca();
extern void funcb();

int main(void)
{
    funca();
    funcb();
    return 0;
}
