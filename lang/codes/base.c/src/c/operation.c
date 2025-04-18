#include "operation.h"

int add(int a, int b)
{
    return a + b;
}

int sub(int a, int b)
{
    return a - b;
}

// gcc -shared -o operation.so -fPIC operation.c
