// 指针

// 在指针变量p上存储变量i的地址, 则p指向i

// 声明指针变量
int *p;  // 声明一个指向整型变量的指针
int a;
p = &a;  // 此时使用*p可以改变a的值
int *q;
q = p;   // 此时指针p和q都向a所在的内存地址

int m;
int *n;
n = p;
*n = *p  // 将指针p所指向的内存地址上的值拷贝到指针n所指向的内存地址

// 指针作为实际参数
void argument_pointer(int *a, int b)
{
    a = &b;
    *a = 10;
}

void const_pointer_arg(conts int *a)
{
    *a = 100;    // 错误
}

// 指针作为返回值
int *max(int *a, int *b)
{
    if (*a > *b)
        return a;
    else
        return b;
}

// 永远不会返回指向局部变量的指针
int *fun(void)
{
    int i;
    i = 100;
    return &i;  // 错误: 变量i在离开函数后失效,所以指向该变量的指针将失效
}

// 指针算术运算
// 指针加上整数
// 指针减去整数
// 两个指针相减

// 指针和数组
int arra_point(void)
{
    int *p, a[10] = {0}, i;
    p = &a[0]
    for(i=0; i<10;i++) {
        a[i] = i;
    }
    printf("%d\n", *p);
    p += 5;
    printf("%d\n", *p);
    ///////////////////////
    a[10] = {0};
    *a = 100;
    *(a+2) = 200;
    for(i=0;i<=9;i++){
        printf("%d\n", a[i]);
    }
}