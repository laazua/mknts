#include <stdio.h>
#include "person.h"


void say_num(const Person p)
{
    printf("%d\n", p.num);
}

void say_name(const Person p)
{
    printf("%s\n", p.name);
}
