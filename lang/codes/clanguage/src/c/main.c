#include <demo.h>
#include <types.h>

u8 add(u8 a, u8 b);

int main()
{
    hello();
    printf("hello world\n");

    i8 num = 12;
    u8 max = 250;
    f32 heigh = 3.2;
    f64 width = 4.8;
    string s = "hello";
    printf("num = %d, max = %d\n", num, max);
    printf("heigh = %f, width = %f\n", heigh, width);
    printf("s = %s\n", s);
    printf("add = %d\n", add(1, 4));


    printf("======== 类型大小 ==========\n");
    printf("char size: %zu\n", sizeof(int8));
    printf("short size: %zu\n", sizeof(int16));
    printf("int size: %zu\n", sizeof(int32));
    printf("long size: %zu\n", sizeof(int64));
    printf("float size: %zu\n", sizeof(float32));
    printf("double size: %zu\n", sizeof(float64));

    return 0;
}

u8 add(u8 a, u8 b)
{
    return a + b;
}

// gcc -I./ *.c 
