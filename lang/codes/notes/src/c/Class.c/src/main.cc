#include <stdio.h>
#include "calculate.h"

extern "C"
{
#include "person.h"
}

int main(void)
{
    Calculate c(200, 100);
    printf("%d\n", c.add());
    printf("%d\n", c.sub());
    printf("%d\n", c.mul());
    printf("%d\n", c.div());

    const Person person = {.num = 12, .name = "张三"};
    say_num(person);
    say_name(person);

    return 0;
}
