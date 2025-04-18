#include <stdio.h>

typedef struct
{
    /* data */
    char *name;
    double weght;
} Person;

int main(void)
{
    Person p = {.name = "zhangsan", .weght = 175.2};
    printf("%s\n", p.name);
    printf("%f\n", p.weght);
    return 0;
}