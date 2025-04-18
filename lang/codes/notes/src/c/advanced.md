# 高级

---

**函数指针**

```
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

typedef uint16_t (\*fun)(int8_t, uint8_t);

bool is_ok(char \*s);
uint16_t add(uint8_t a, uint8_t b);
uint16_t pls(uint8_t c, uint8_t d);
uint16_t cnt(fun, uint8_t a, uint8_t b);

int main(void)
{
    if (is_ok("a"))
        puts("yes");
    else
        puts("no");

    // add()回调
    uint16_t rea = cnt(add, 1, 2);
    printf("%d\n", rea);
    // pls()回调
    uint16_t rep = cnt(pls, 1, 2);
    printf("%d\n", rep);
    return 0;
}

uint16_t add(uint8_t a, uint8_t b)
{
    return a + b;
}

uint16_t pls(uint8_t c, uint8_t d)
{
    return c * d;
}

uint16_t cnt(fun fn, uint8_t a, uint8_t b)
{
    return fn(a, b);
}

bool is_ok(char \*s)
{
    bool flag;
    if (strcmp(s, "a") == 0)
       flag = true;
    else
       flag = false;
    return flag;
}
```

---

**条件宏**

```
#ifdef NUM
    do something
#else
    do something
#endif
```

_在头文件中定义宏在需要使用时引入该头文件, 如:_  
config.h  
#define NUM 1

源代码 num.c 中内容如下:

```
#include "config.h"
#ifdef NUM
    // do something
#else
    // do something
#endif
```

_编译时传递参数 gcc -DNUM=1 num.c_
